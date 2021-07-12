# MMAP
Metabarcoding Multiprimer approach pipeline for sequences from Illumina platform 
#MMAP
Metabarcoding Multiprimer approach pipeline for Illumina platform - by Iván Batuecas- 

MMAP is a metabarcoding pipeline used to sequences obtained from illumina platform used to study the gut content from predator insect (https://biorxiv.org/cgi/content/short/2021.05.19.444782v1). The pipile is integrating by different functions from , VSEARCH, BIOPYTHON, CUTADAPT and other programs. 

The pipeline is run as Bash that automatically generates the output in differents folders and the logfile from each execute script that contain a complete output from the console.

For a a short tutorial on analysed sequences from metabarcoding datasets obtained from https://biorxiv.org/cgi/content/short/2021.05.19.444782v1

# Citing MMAP
If you like BASTA and use it for publications please cite it as "Kahlke T and Ralph PJ (2018), BASTA–Taxonomic classification of sequences and sequence bins using Last Common Ancestor estimations. Meth. Ecol. Evol. doi:10.1111/2041‐210X.13095"


About MMAP
Please keep in mind that MMAP needs differnt software (Vsearch , Cutadapt...) installed to work properly. For it, the best way is the use of two Anaconda enviroment.
The pipeline was tested in Linux based systems (Ubuntu 20.04 LTS), so I recommend strongly its use in this operating systmem.


To install MMAP locally
Install Anaconda 
https://docs.anaconda.com/anaconda/install/

-Select your own operating systems (linux Ubuntu 20.04, in my case)

-We have to create a two diffent enviroments:
conda create -n Env_1 python=3.6;

conda create -n Env_2 python=2.7
# Install independencies needed from MMAP

git clone https://github.com/Ivanbh214/MMAP

# Active python 3 envirment and execute requeriments
conda activate Env_1

./Requeriments_python_3.sh


# Active python 2 enviroment and execute requeriments
conda activate Env_2

./Requeriments_python_2.sh


# Initialling MMAP
-Adjust the parameters in the scritps to the need of your experiments, by default is included the parameters used in https://biorxiv.org/cgi/content/short/2021.05.19.444782v1 (for it, see the tools description).

In script_1:
	-Fix the working directory
	-Fix the merged parameters
	-Number of samples
	-Number of primers for the split

In script_2:
	-Fix similarity % for the clustering
	-Fix the chimera algorith detection
	-Fix the blast parameters
	
In script_3 
	-Fix the LCA algoriths parameters

-Execute the script in secuential order firstly for the samples amplified with arthorpod primers and the for plant samples:

conda activate Env_1

./Script_1_Art.sh

./Script_2_Art.sh

conda deactivate Env_1

conda activate Env_2

./Script_3_Art.sh


