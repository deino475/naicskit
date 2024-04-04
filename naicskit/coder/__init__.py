from transformers import pipeline
from transformers import AutoTokenizer
from naicskit.taxonomies import load_taxonomy

class IndustryCoder:
	def __init__(self, taxonomy, level, device: str = "cpu"):
		assert device in ['cpu','cuda:1','mps'], "Device must be either 'cpu', 'cuda:1', or 'mps'"
		self.taxonomy = taxonomy
		self.level = level
		self.taxonomy_data = load_taxonomy(taxonomy, level)
		self.tokenizer = AutoTokenizer.from_pretrained('google-t5/t5-small')
		self.pipeline = pipeline(
			'text-classification', model = 'ndixon104/naicskit-v1', device = device,
			tokenizer = self.tokenizer
		)


	def code_records(self, descriptions):
		results = []
		if type(descriptions) == str:
			descriptions = [descriptions]

		for description in descriptions:
			prompts = [
				f"identify industry: industry: {code['name']}\n\n description: {description}"
				for code in self.taxonomy_data
			]
			scores = self.pipeline(prompts)
			description_results = []
			for x in range(len(self.taxonomy_data)):
				description_results.append({
					'id' : self.taxonomy_data[x]['id'],
					'name' : self.taxonomy_data[x]['name'],
					'match_score' : scores[x]['score'] if scores[x]['label'] == 'POSITIVE' else 1 - scores[x]['score']
				})
			description_results = sorted(
				description_results, key = lambda d: d['match_score'], reverse = True
			)

			results.append({
				'descriptions' : description,
				'taxonomy_system' : self.taxonomy,
				'codes' : description_results
			})

		return results
