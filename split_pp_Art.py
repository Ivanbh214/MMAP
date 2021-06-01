# coding=utf-8

# J Piñol, 4-May-2018
#
# Splits a FASTA file into several ones depending on the primer set
# Used to generate the amplicons
#

from Bio import SeqIO
import os

din  = "/home/ivan/Escritorio/Material_vigente_septiembre/Run1/Art/split_pp/"
dout = "/home/ivan/Escritorio/Material_vigente_septiembre/Run1/Art/trim/"
for f in os.listdir(din):
    #print(f)
    #if f != 'A.fasta':
    #    continue
    last5 = f[-5:]
    if last5 == 'fasta':
        if f != 'prepped.fasta':
            filein = din + f
            #print(filein)
            root = f.replace(".fasta", "")

            fileout_art1 = dout + root + "-art1.fasta"  # includes pl4
            fileout_art6 = dout + root + "-art6.fasta"
            #fileout_pl1  = dout + root + "-pl1.fasta"
            fileout_oth  = dout + root + "-oth.fasta"

            # accounting
            n      = 0
            n_art1 = 0
            n_art6 = 0
            #n_pl1  = 0
            n_oth  = 0
            for record in SeqIO.parse(filein, "fasta"):
                n = n + 1
                am = len(record.seq)
                #print(am)
                if am >= 180 and am < 240:
                    n_art1 = n_art1 + 1
                    if not os.path.exists(fileout_art1):
                        fart1 = open(fileout_art1, "a")
                    fart1.write(record.format("fasta"))
                elif am >=350 and am < 375:
                    n_art6 = n_art6 + 1
                    if not os.path.exists(fileout_art6):
                        fart6 = open(fileout_art6, "a")
                    fart6.write(record.format("fasta"))
                #elif am >=375 and am < 420:
                    #n_pl1 = n_pl1 + 1
                    #if not os.path.exists(fileout_pl1):
                        #fpl1 = open(fileout_pl1, "a")
                    #fpl1.write(record.format("fasta"))
                else:
                    #print("{} length = {}".format(root, am))
                    n_oth = n_oth + 1
                    if not os.path.exists(fileout_oth):
                        foth = open(fileout_oth, "a")
                    foth.write(record.format("fasta"))
            
            print("{}   n = {}     n_art1 = {}     n_art6 = {}     n_oth = {}".format(root, n, n_art1, n_art6, n_oth))

# close output files
fart1.close()
fart6.close()
foth.close()

print("Bye, bye!!")
