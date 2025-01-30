# CReM-based de novo appraoches

These are the set of examples for CReM-based approaches for structure enumeration

##Installtion of an environment

```
# cremdock
conda create -n cremdock -c conda-forge python=3.9 numpy rdkit dask distributed scipy scikit-learn -y
source activate cremdock
pip install prolif vina meeko easydock==0.3.2 crem
pip install cremdock
conda deactivate
``

## Basic examples

`crem_example.ipynb` - jupyter notebook with basic operations using Python API

`crem_ml.ipynb` - jupyter notebook with an example of greedy structure generation using CReM and ML model

## CReM-dock

Directory cremdock contains files relevant to the de novo generation using CReM and molecular docking
