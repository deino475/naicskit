# Automatically Assigning Industry Classifications to Company Descriptions – An Entailment Based Approach

## Description
naicskit is a Python package which assigns industry classification codes to 

## How To Use naicskit
```{python}
from naicskit.coder import IndustryCoder
description = '...'
coder = IndustryCoder('naics.2022','2')
results = coder.code_records(description)
```

## Supported Taxonomies
- International Standard of Industrial Classification Rev 5.0 (ISIC 2024) `isic.2024` 
- International Standard of Industrial Classification Rev 4.0 (ISIC 2006) `isic.2006` 
- International Standard of Industrial Classification Rev 3.1 (ISIC 2002) `isic.2002` 
- International Standard of Industrial Classification Rev 3.0 (ISIC 1989) `isic.1989` 
- International Standard of Industrial Classification Rev 2.0 (ISIC 1968) `isic.1968` 
- North American Industry Classification System 2022 (NAICS 2022) `naics.2022` 
- North American Industry Classification System 2017 (NAICS 2017) `naics.2017` 
- North American Industry Classification System 2012 (NAICS 2012) `naics.2012` 
- North American Industry Classification System 2007 (NAICS 2007) `naics.2007` 
- Standard Industrial Classification (SIC 1987) `sic.1987` 
