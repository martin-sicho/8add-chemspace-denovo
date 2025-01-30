# Chemical Space and De Novo Drug Design Tutorial

*Martin Šícho*

*Pavel Polischuk*

## Install the Tools

Run the following commands in your terminal to set up and activate the environment:

```bash
sudo apt-get install libxrender1 # WSL users, can end with an error but it does not matter
conda create -n denovo python=3.12 -y
conda activate denovo
pip install -r requirements.txt
```

## Follow Tutorials

Follow the `README.md` file directions in each folder:

- [Chemical Space Visualization](./chemspace/README.md)
- [De Novo Drug Design](./denovo/README.md)

You may have to run some extra commands to download and set up data for each tutorial. It is recommended that you run the Jupyter Lab/Notebook server in the current folder (repository root) for easy navigation through files and command line access:

```bash
jupyter-lab
```

or

```bash
jupyter-notebook
```
