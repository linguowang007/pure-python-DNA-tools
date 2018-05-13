#! /data/home/lingw/anaconda3/bin/python
# -*- coding: utf-8 -*-
import sys

fasta = sys.argv[1]  # input a fasta file
target_ids = sys.argv[2:]  # input one or many want to extracted fasta IDs

with open(fasta) as f:
    at_body = False
    for line in f:
        if line.startswith('>'):  # header line
            header = line.split()[0][1:]
            if header not in target_ids:
                at_body = False
                continue
            print(line, end='')
            at_body = True
        elif at_body:  # body line
            print(line, end='')
