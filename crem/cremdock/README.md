## Installtion of an environment

```
# cremdock
conda create -n cremdock -c conda-forge python=3.9 numpy rdkit dask distributed scipy scikit-learn -y
source activate cremdock
pip install prolif vina meeko easydock==0.3.2 crem
pip install cremdock
```

# Running an example

To run the example unvoke the following command line

```
cremdock -i input.sdf -o 1.db -d ../chembl22_sa2_hac12.db --nclust 2 --max_replacements 10 --program vina --config vina_config.yml -c 2 --plif leu83.ahbdonor leu83.ahbacceptor --plif_cutoff 0.5 --plif_protein 2btr.pdb
```
