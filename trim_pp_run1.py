# coding=utf-8
#
# removes adaptors from amplicons
#

#from Bio import SeqIO
import os
from subprocess import call

dout  = "/home/Art/Without_primers/"
din = "/home/Art/trim/"

# for all files in the directory
for f in os.listdir(din):
    # only fasta files
    if f[-5:] == 'fasta':
        # input and output complete filenames
        filein = din + f
        fileout = dout + f
        # whileich kind of file?
        type = f[3:]
        type = type.replace(".fasta", "")
        #assign values for trimming the 5' and 3' end depending on the type of the file
        if type == '-art1':
            c5 = 30
            c3 = 24
            ok = True
        elif type == '-art6':
            c5 = 26
            c3 = 26
            ok = True
	       # elif type == 'pl1':
            #c5 = 20
            #c3 = 20
            #ok = True
        #elif type == 'pl4':
            #c5 = 30
            #c3 = 30
            #ok = True
        else:
            ok = False
            print('ERROR:')
            print('ERROR: Wrong type ' + type)
            print('ERROR:')
        if ok:
            # run cutadapt
            cmd = "cutadapt -u "+ str(c5) + " -u -" + str(c3) + " -o " + fileout + " " + filein
            ret = call(cmd, shell=True)

print("Bye, bye!!")
