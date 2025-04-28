# LELM
This project utilizes the following three publicly available Chinese Named Entity Recognition (NER) datasets:

### 1. CLUENER2020
- **Description**: A fine-grained named entity recognition dataset containing 10 entity categories (e.g., person, location, organization), annotated in BIO format.    
- **Link**: [CLUENER2020 GitHub Repository](https://github.com/CLUEbenchmark/CLUENER2020)
- **Example**:
  ```text
  浙 B-company
  商 I-company
  银 I-company
  行 E-company
  企 O
  业 O
  信 O
  贷 O
  部 O
  叶 B-name
  老 I-name
  桂 E-name
  博 O
  士 O
 ### 2. MSRA
- **Description**: A Chinese NER dataset released by MSRA, focusing on three entity types: locations, organizations, and person names, annotated in BIO format.  
- **Link**: [MSRA GitHub Repository](https://github.com/bytetopia/nlp_datasets)  
- **Example**:
  ```text
  历	B-LOC
  博	I-LOC
  、	O
  古	B-ORG
  研	I-ORG
	所	I-ORG
 ### 3. Weibo
- **Description**：A Chinese NER dataset released by MSRA, focusing on three entity types: locations, organizations, and person names, annotated in BIO format.  
- **Link**：[Weibo GitHub Repository](https://github.com/hltcoe/golden-horse/blob/master/data)  
- **Example**：
  ```text
  南	B-GPE.NAM
  都	I-GPE.NAM
  深	B-GPE.NAM
  圳	I-GPE.NAM
  读	O
  本	O
  发	O
  起	O

# bio2sen-label-entity.py

A utility tool for converting **BIO/BIOES-annotated** NER datasets into **plain text format**. Execute with:  
```bash
python bio2sen-label-entity.py \
    --input_file input.txt \
    --output_file output.txt

Conversion Example：
Input file (train.bioes):
  浙 B-company
  商 I-company
  银 I-company
  行 E-company
  企 O
  业 O
  叶 B-name
  老 I-name
  桂 E-name

Output file (output.txt):
company 浙江商业银行 企 业 name 叶老桂
