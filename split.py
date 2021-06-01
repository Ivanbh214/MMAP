# coding=utf-8
#
# J Piñol, 2-May-2018
#
# this program reads the prepped.fasta file produced by PIPITS
# then it  creates as many files as diferent characters are in the
# first two positions of the sequnece id
#
# in the example there were the libraries A B C --- L
# if more than one character is used to differentiate the individual libraries,
# then the program has to be changed accordingly
from Bio import SeqIO
i = 0
fnold = "xxx"
for record in SeqIO.parse("/home/Art/split/Run1_artropodos.fasta", "fasta"):
   i = i + 1
   fn = "/home/Art/split_pp/" + record.id[:3] + ".fasta"
   # a different file
   if (fn != fnold):
       print(i)
       print(fn)
       i = 0
   # write to the file
   # I UserWarninged write instead SeqIO:write because it cannot append to a file
   with open(fn, "a") as myfile:
       myfile.write(record.format("fasta"))
   fnold = fn
