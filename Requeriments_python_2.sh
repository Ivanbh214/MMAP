#!/bin/bash
conda install -c bioconda -c bnoon -c timkahlke basta

# set up NCBI taxonomy database
basta taxonomy

# download and set up genbank and uniprot mappings
# NOTE: this might not be needed for you. See Wiki for details (Selecte the database that you want use, gb in my case)
basta download gb

