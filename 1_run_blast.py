import Bio
from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio.Alphabet import IUPAC, Gapped
from Bio.Blast.Applications import NcbiblastnCommandline
import numpy as np
import sqlite3
import re
import csv
import itertools
import os
import subprocess

# sql_db_location = '/u/home/a/akarlsbe/scratch/db.microbiome/Fungi/data/refSeqFungiStats.db'
sql_db_location = '/Users/aaronkarlsberg/Desktop/199/db.microbiome/Fungi/data/refSeqFungiStats.db'

def get_taxids(sql_db_location):
	conn = sqlite3.connect(sql_db_location)
	c = conn.cursor()
	c.execute("SELECT DISTINCT SPECIESTAXID FROM SPECIESDB")
	query = [row[0] for row in c.fetchall()]
	conn.close()
	speciesTaxids = []
	for taxId in query:
		speciesTaxids.append(taxId)
	return speciesTaxids

def get_filepaths(sql_db_location, taxId):
	conn = sqlite3.connect(sql_db_location)
	c = conn.cursor()
	c.execute("SELECT FILEPATH FROM SPECIESDB where SPECIESTAXID = ?", (taxId,))
	query = [row[0] for row in c.fetchall()]
	conn.close()
	filepaths = []
	for filepath in query:
		filepaths.append(filepath)
	return filepaths, taxId


def blast_combos(filepaths, taxId):
    blast_combos = []
    for path in itertools.combinations(filepaths, 2):
        blast_combos.append([path[0], path[1]])
    return blast_combos


def blast_scripts(blast_combos, taxId):
# make directory for for taxID
	if len(blast_combos) > 1:
		os.makedirs(taxId+"/blast_dbs")
		os.makedirs(taxId+"/blast_results")
		os.makedirs(taxId+"/single_seq_fastas")
		os.makedirs(taxId+"/xmfa")
		os.makedirs(taxId+"/consensus_fastas")

	x=1
	# run blast on each combo within new taxid directory and store results.
	for combo in blast_combos:
		makeblastdb = "makeblastdb -in "+ combo[0] +" -dbtype nucl -parse_seqids -out "+taxId+"/blast_dbs/combo"+x+"db"
		process1 = subprocess.Popen(makeblastdb.split(), stdout=subprocess.PIPE)
		output, error = process1.communicate()
		blastn = "blastn -db "+taxId+"/blast_dbs/combo"+x+"db -query "+ combo[1] +" -out "+taxId+"/blast_results/combo"+x+"results.out -outfmt '7 qseqid sseqid pident qlen length mismatch'"
		process2 = subprocess.Popen(blastn.split(), stdout=subprocess.PIPE)
		output, error = process2.communicate() 
		x+=1
