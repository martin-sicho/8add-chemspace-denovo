# CReM-based de novo approaches

These are the set of examples for CReM-based approaches for structure enumeration

## Setup an environment

Activate the previously created environment and add `crem` Python module there by
```
conda activate denovo
pip install crem
```

Download and unpack the precompiled fragment library

```
curl https://qsar4u.com/files/cremdb/chembl22_sa2_hac12.db.gz --output chembl22_sa2_hac12.db.gz && gunzip chembl22_sa2_hac12.db.gz
```

## Basic examples

`crem_example.ipynb` - jupyter notebook with basic operations using Python API

`crem_ml.ipynb` - jupyter notebook with an example of greedy structure generation using CReM and ML model

## CReM-dock

Directory cremdock contains files relevant to the de novo generation using CReM and molecular docking. A specific README file is inside.
