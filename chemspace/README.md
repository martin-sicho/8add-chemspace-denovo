
# Comparison of Distinct Chemical Spaces

In this tutorial, we are going to use data from a [diploma thesis](https://github.com/fulopjoz/diploma_thesis) (see [attached PDF](./tx-45604-fulop-jozef.pdf)), which focused on the development of data sets and machine learning models to distinguish RNA binders from protein binders. Both proteins and RNA are pharmaceutically relevant targets, but are chemically distinct. Therefore, it is expected that small molecule ligands targetting these distinct macromolecules come from distinct chemical spaces. In this analysis, we will try to look at different visualization techniques that will help us judge the similarities or dissimilarities between protein and RNA binders on a larger scale.

Before you begin, you will need to download and unzip the data sets from the thesis:

```bash
curl https://owncloud.cesnet.cz/index.php/s/juPLpmojqktq0IU/download --output data.zip && unzip data.zip && rm data.zip
```

If this command does not work, you can also just use the download link from your browser and unzip manually in this folder. When the data is ready, open the [tutorial notebook](./tutorial.ipynb).