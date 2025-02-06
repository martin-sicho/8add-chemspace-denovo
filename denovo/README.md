# De Novo Design of Potential Binders of [Serotonin 1A (5-HT1A) Receptor](https://gpcrdb.org/protein/5ht1a_human/)

**G-protein coupled receptor for 5-hydroxytryptamine (serotonin) ([PubMed:22957663](https://pubmed.ncbi.nlm.nih.gov/22957663/), [PubMed:3138543](https://pubmed.ncbi.nlm.nih.gov/3138543/), [PubMed:33762731](https://pubmed.ncbi.nlm.nih.gov/33762731/), [PubMed:37935376](https://pubmed.ncbi.nlm.nih.gov/37935376/), [PubMed:37935377](https://pubmed.ncbi.nlm.nih.gov/37935377/), [PubMed:8138923](https://pubmed.ncbi.nlm.nih.gov/8138923/), [PubMed:8393041](https://pubmed.ncbi.nlm.nih.gov/8393041/)). Also functions as a receptor for various drugs and psychoactive substances ([PubMed:22957663](https://pubmed.ncbi.nlm.nih.gov/22957663/), [PubMed:3138543](https://pubmed.ncbi.nlm.nih.gov/3138543/), [PubMed:33762731](https://pubmed.ncbi.nlm.nih.gov/33762731/), [PubMed:38552625](https://pubmed.ncbi.nlm.nih.gov/38552625/), [PubMed:8138923](https://pubmed.ncbi.nlm.nih.gov/8138923/), [PubMed:8393041](https://pubmed.ncbi.nlm.nih.gov/8393041/)).** Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase ([PubMed:22957663](https://pubmed.ncbi.nlm.nih.gov/22957663/), [PubMed:3138543](https://pubmed.ncbi.nlm.nih.gov/3138543/), [PubMed:33762731](https://pubmed.ncbi.nlm.nih.gov/33762731/), [PubMed:8138923](https://pubmed.ncbi.nlm.nih.gov/8138923/), [PubMed:8393041](https://pubmed.ncbi.nlm.nih.gov/8393041/)). HTR1A is coupled to G(i)/G(o) G alpha proteins and mediates inhibitory neurotransmission: signaling inhibits adenylate cyclase activity and activates a phosphatidylinositol-calcium second messenger system that regulates the release of Ca2+ ions from intracellular stores ([PubMed:33762731](https://pubmed.ncbi.nlm.nih.gov/33762731/), [PubMed:35610220](https://pubmed.ncbi.nlm.nih.gov/35610220/)). Beta-arrestin family members regulate signaling by mediating both receptor desensitization and resensitization processes ([PubMed:18476671](https://pubmed.ncbi.nlm.nih.gov/18476671/), [PubMed:20363322](https://pubmed.ncbi.nlm.nih.gov/20363322/), [PubMed:20945968](https://pubmed.ncbi.nlm.nih.gov/20945968/)).Plays a role in the regulation of 5-hydroxytryptamine release and in the regulation of dopamine and 5-hydroxytryptamine metabolism ([PubMed:18476671](https://pubmed.ncbi.nlm.nih.gov/18476671/), [PubMed:20363322](https://pubmed.ncbi.nlm.nih.gov/20363322/), [PubMed:20945968](https://pubmed.ncbi.nlm.nih.gov/20945968/)). **Plays a role in the regulation of dopamine and 5-hydroxytryptamine levels in the brain, and thereby affects neural activity, mood and behavior ([PubMed:18476671](https://pubmed.ncbi.nlm.nih.gov/18476671/), [PubMed:20363322](https://pubmed.ncbi.nlm.nih.gov/20363322/), [PubMed:20945968](https://pubmed.ncbi.nlm.nih.gov/20945968/)).**
**Plays a role in the response to anxiogenic stimuli ([PubMed:18476671](https://pubmed.ncbi.nlm.nih.gov/18476671/), [PubMed:20363322](https://pubmed.ncbi.nlm.nih.gov/20363322/), [PubMed:20945968](https://pubmed.ncbi.nlm.nih.gov/20945968/)).** (Credit: [UniProt](https://www.uniprot.org/uniprotkb/P08908/entry))

In this tutorial, we will try to use different tools to automatically generate theoretical structures of novel 5-HT1A ligands. We will use a pretrained QSAR model for optimization of the predicted structures using two distinct strategies, CReM-ML and DrugEx.

## [DrugEx](https://pubs.acs.org/doi/10.1021/acs.jcim.3c00434)

You will use the DrugEx pretrained models and other data in this tutorial, which you can download with the following command:

```bash
drugex download # execute in current directory
````

You can start the tutorial by following the [drugex](./drugex.ipynb) notebook.

## CReM

See [here](../crem).
