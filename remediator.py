#!/usr/bin/python
# remediator_python.py - version 1.55 9/13/07
# Copyright 2007, Jeffrey J. Headd and Robert Immormino

# revision 1.55 - JJH 070808 - added support for DU DNA base
#               - JJH 070808 - added compiled RE object for HN2 RES special case
#		- JJH 070815 - updated name of hash dictionary file
#		- JJH 070823 - added support for CNS Xplor and Coot RNA names
#		- JJH 070908 - added REMARK   4 comment addition
#               - JJH 070913 - added support for left-justified RNA/DNA old names
#		- JJH 070913 - added support for all left-justified residue names
#
# SAS - corrected 22.01.2008 to fix an error: the original script stripped spaces 
#       at the ends of all raws
# SAS - corrected 04.06.2008 to fix an error: the original script did not change 
#       coordinate lines with alter codes

import sys
import getopt
import os
import string
import re

masterhash="master_hash.txt"

def usage():
	print """
	************************************
	remediator_python.py: version 1.55 8/8/07
	Copyright 2007, Jeffrey J. Headd and Robert Immormino
	remediator.py: bug fixes by Sergei Spirin (2008)
	For a log of changes, view remediator.py in your favorite text editor 

	USAGE: remediator_sas.py [--options] input_file > output_file

	options:
	  --help	outputs this help message
	  --pdb		takes a .pdb formatted file as input
	  --old	 	output file will use the PDBv2.3 naming conventions
	  --remediated 	output file will use the remediated naming conventions (default)

	remediator is generally inteded to convert from PDBv2.3 to PDBv3.0. 
	This changes files from the pre-wwPDB format into the wwPDB remediated format.
	Output is directed to standard out.

	EXAMPLE:   remediator_sas.py --pdb --old 404D.pdb > 404D_old.pdb 
        """

try:
	opts, args = getopt.getopt( sys.argv[1:], 'hpor',['help', 'pdb', 'old', 'remediated'] )
except getopt.GetoptError:
	usage()
	sys.exit()

old_out = False
remediated_out = False
dopdb = False
#dokin = False

for o, a in opts:
	if o in ("-h", "--help"):
		usage()
		sys.exit()
	if o in ("-p", "--pdb"):
		dopdb = True
	#if o in ("-k", "--kin"):
	#	dokin = True
	if o in ("-o", "--old"):
		old_out = True
	if o in ("-r", "--remediated"):
		remediated_out = True

if len(args) < 1:
	sys.stderr.write("\n**REMEDIATOR ERROR: User must specify input filename\n")
	sys.exit(usage())
if len(args) > 1:
	sys.stderr.write("\n**REMEDIATOR ERROR: too many input files specified\n")
	sys.exit(usage())

#if dopdb == True and dokin == True:
#	usage()
#	sys.exit("REMEDIATOR ERROR: specify only one input file type")
if old_out == True and remediated_out == True:
	sys.stderr.write("\n**REMEDIATOR ERROR: cannot output old and remediated names simultaneously\n")
	sys.exit(usage())

if dopdb == False:
	#print "REMEDIATOR:  Assuming PDB input file"
	dopdb = True
if old_out == False and remediated_out == False:
	remediated_out = True

filename = args[0]
assert os.path.isfile(filename),\
	"\n**REMEDIATOR ERROR:  cannot find %s" %(filename)
basename = os.path.basename(filename)

#--Build Hash Table------------------------------------------------
atom_exch = {}
f = open(masterhash)
#f = open("master_hash.txt")
if remediated_out == True: #converting to remediated
	for line in f:
		line=line.rstrip()
		new, old = line.split(':')
		atom_exch[old] = new
	remark4 = "REMARK   4 REMEDIATOR VALIDATED PDB VERSION 3.0 COMPLIANT"
else: #converting to old
	for line in f:
		new, old = line.split(':')
		atom_exch[new] = old
	remark4 = "REMARK   4 REMEDIATOR VALIDATED PDB VERSION 2.3 COMPLIANT"
f.close()
#------------------------------------------------------------------


#----PDB routine---------------------------------------------------

previous = None
current = None
print_line = ""
remark_flag = False

pdb_file = open(filename)

aa_re = re.compile(' HN2 (ALA|ARG|ASN|ASP|ASX|CSE|CYS|GLN|GLU|GLX|GLY|HIS|ILE|LEU|LYS|MET|MSE|PHE|PRO|SER|THR|TRP|UNK|TYR|VAL)')

for line in pdb_file:
#	line=line.rstrip()
	type_test = line[0:6]
	if remark_flag == False:
		if type_test == "REMARK":
			if re.search(remark4,line):
				remark_flag = True
			elif re.match('REMARK   4 REMEDIATOR',line):
				continue
			elif int('0' + line[6:10].strip()) > 4:
				print_line += remark4 + "\n"
				remark_flag = True
			
	if type_test in ("ATOM  ", "HETATM", "TER   ", "ANISOU", "SIGATM", "SIGUIJ", "LINK  "):
		if remark_flag == False:
			print_line += remark4 + "\n"
			remark_flag = True
		#--pre-screen for CNS Xplor RNA base names and Coot RNA base names--------
		if re.match(r'.{17}(GUA|ADE|CYT|THY|URI)',line):
			line = re.sub(r'\A(.{17})(.)..',r'\g<1>  \g<2>',line)
		elif re.match(r'.{17}(OIP| Ar| Gr| Cr| Ur)',line):
			line = re.sub(r'\A(.{17}).(.).',r'\g<1>  \g<2>',line)
		#-------------------------------------------------------------------------

		#REMOVED FROM THE CODE IN FAVOR OF THE GENERIC BLOCK BELOW
                #--pre-screen for left-justified RNA/DNA base names-----------------------
		#if re.match(r'.{17}(G  |A  |C  |T  |U  |I  )',line):
		#	line = re.sub(r'\A(.{17})(.)\s\s',r'\g<1>  \g<2>',line)
                #-------------------------------------------------------------------------
		
		#--make any left-justified residue names right-justified------------------
		if re.match(r'.{17}([a-zA-Z])  ',line):
			line = re.sub(r'\A(.{17})(.)\s\s',r'\g<1>  \g<2>',line)
		elif re.match(r'.{17}([a-zA-Z][a-zA-Z]) ',line):
			line = re.sub(r'\A(.{17})(..)\s',r'\g<1> \g<2>',line)
		#-------------------------------------------------------------------------
		entry = line[12:20]
		previous = current
		current = line[18:26]
		clean_entry = entry[0:4] + " " + entry[5:8]
		if atom_exch.has_key(clean_entry):
			line = string.replace(line,clean_entry[0:4],atom_exch[clean_entry][0:4])
	if previous == None:
		previous = current
	if previous == current:
		print_line += line
	elif previous != current:
		if re.search(r'.\S..[A-Z ] .[ACTGIU]',print_line):
			if re.search(r'O2[\'|\*]   .',print_line) == None:
				DNA_base = previous[1]
				if remediated_out == True:
					print_line = re.sub(r'(.\S..[A-Z ])  '+DNA_base+' ',r'\g<1> D'+DNA_base+' ',print_line)
					print_line = re.sub(r'(TER.{15}) '+DNA_base+' ',r'\g<1>D'+DNA_base+' ',print_line)
				elif old_out == True:
					print_line = re.sub(r'(.\S..[A-Z ]) D'+DNA_base+' ',r'\g<1>  '+DNA_base+' ',print_line)
					print_line = re.sub(r'(TER.{15})D'+DNA_base+' ',r'\g<1> '+DNA_base+' ',print_line)
		
		if old_out == True:
			m = aa_re.search(print_line)
			if m:
				res = m.group(1)
				if re.search('1H   '+res,print_line) or re.search('2H   '+res,print_line):
					print_line = re.sub(' HN2 '+res,'2H   '+res,print_line)
#		print_line=print_line.rstrip()
		print_line=print_line.rstrip("\r\n")
		print print_line
#		print print_line[0:-2]
		print_line = line
pdb_file.close()

if re.search(r'.\S..[A-Z ] .[ACTGIU]',print_line):
	if re.search(r'O2[\'|\*][A-Z ]  .',print_line) == None:
		DNA_base = previous[1]
		if remediated_out == True:
			print_line = re.sub(r'(.\S..[A-Z ])  '+DNA_base,r'\g<1> D'+DNA_base,print_line)
			print_line = re.sub(r'(TER.{15}) '+DNA_base+' ',r'\g<1>D'+DNA_base+' ',print_line)
		elif old_out == True:
			print_line = re.sub(r'(.\S..[A-Z ]) D'+DNA_base,r'\g<1>  '+DNA_base,print_line)
			print_line = re.sub(r'(TER.{15})D'+DNA_base+' ',r'\g<1> '+DNA_base+' ',print_line)
	
	if old_out == True:
		m = aa_re.search(print_line)
		if m:
			res = m.group(1)
			if re.search('1H   '+res,print_line) or re.search('2H   '+res,print_line):
				print_line = re.sub(' HN2 '+res,'2H   '+res,print_line)

print_line=print_line.rstrip("\r\n")
print print_line
