#!/bin/bash
#Install fastx_toolkit
 git clone https://github.com/agordon/fastx_toolkit
 cd fastx_toolkit
 ./reconf
 ./configure
  make

#Install vsearch
conda install -c bioconda vsearch

#Install biopython
conda update -c conda-forge biopython

#Install blast
conda install -c bioconda blast
