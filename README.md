# Phylogenetic Tree Builder
## Setting up dependencies
1. In order to setup python dependencies install all the packages specified in requirements.txt file (project tested on a ubuntu 20.04 machine running python 3.8 but could work on other software configurations)
```bash
pip install -r requirements.txt
```
2. Obtain the clustal omega distribution for you operation system from 
[link](http://www.clustal.org/omega/). We have included the clustal destribution
for ubuntu with the code.

## How to build the phylogenetic Trees
1. We have included the data files (gene sequences and start stop postions) in 
data directory.
2. You can use the make build automation tool(typically included with most
operating systems) and simply give the `make` command which will populate the 
output directory with build artifacts including
	* Homologous gene sequences : These will have the name `<gene>.fasta`
	* Multple sequence alignment results on that gene sequence: These will 
	have the name `<gene>_alignment.fasta`
	* Phylogenetic trees : Each tree will have an image name `<gene>.png` and 
	nexus file representing the tree named `<gene>.nex`
