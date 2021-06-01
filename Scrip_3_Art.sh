#!/bin/bash
#Basta 
cd /home/MMAP/Basta/
(echo 

echo basta

for i in *.blast; do basta sequence $(basename $i .blast).blast Basta_$(basename $i .blast).lca_97.out gb -x True -l 70 -m 1 -i 97; done)|& tee output_Basta.log 






