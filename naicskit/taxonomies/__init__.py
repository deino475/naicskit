import pkgutil
import json 

def load_taxonomy(taxonomy: str, level: str) -> dict:
	taxonomy = taxonomy.replace(".","_")
	data = pkgutil.get_data(__name__, f"{taxonomy}.json")
	return json.loads(data)['taxonomies'][level]