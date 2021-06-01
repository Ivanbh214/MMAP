#!/bin/bash

cd /home/MMAP/Art/Without_primers/

cp *.fasta /home/MMAP/Art/Vsearch/

#Vsearch por muestra
(echo Vsearch

cd /home/MMAP/Art/Vsearch/

###Cluster 1 
echo Vsearch cluster1

for i in *.fasta; do vsearch --cluster_size $(basename $i .fasta).fasta --id 0.97 --strand plus --sizein --sizeout --fasta_width 0 --centroids $(basename $i .fasta)_s_tr_clust.fasta;done 

mv *_s_tr_clust.fasta /home/MMAP/Art/Vsearch/cluster1/

cd /home/MMAP/Art/Vsearch/cluster1/

#Chimera
echo Vsearch chimera

for i in *.fasta; do vsearch --uchime_denovo $(basename $i .fasta).fasta  --chimeras $(basename $i)chimera.out.fasta --nonchimeras  $(basename $i .fasta)_s_tr_clust_non_chimera.fasta;done


mv *_s_tr_clust_non_chimera.fasta /home/MMAP/Vsearch/chimera/

#Cluster2
echo Vsearch cluster2

cd /home/MMAP/Art/Vsearch/chimera/

for i in *.fasta; do vsearch --cluster_size $(basename $i .fasta).fasta --id 0.97 --strand plus --sizein --sizeout --fasta_width 0 --biomout $(basename $i .fasta)_2_clus.biom --relabel OTU_ --relabel_keep --centroids $(basename $i .fasta)_2_clus.fasta;done 

mv *_2_clus.fasta /home/MMAP/Vsearch/cluster2/

cd /home/MMAP/Art/Vsearch/cluster2/

#Headers

echo headers

for i in *.fasta; do cut -f1 -d ":" $(basename $i .fasta).fasta  > $(basename $i .fasta)_.fasta;done


mv *_.fasta /home/MMAP/Art/rename/

cd /home/Art/rename/

for i in *.fasta; do sed 's, ,_,g' $(basename $i .fasta).fasta > $(basename $i .fasta)_rename.fasta;done

cat *-art1_s_tr_clust_s_tr_clust_non_chimera_2_clus__rename.fasta > Art1_run1_rename.fasta 

cp Art1_run1_rename.fasta  /home/MMAP/Art/Blast/

cat *-art6_s_tr_clust_s_tr_clust_non_chimera_2_clus__rename.fasta > Art6_run1_rename.fasta 

cp Art6_run1_rename.fasta  /home/MMAP/Art/Blast/

echo blast 

python /home/MMAP/Art/Blast/blast_pp_Art1_Run1.py)|& tee output_run1_vsearch.log 






