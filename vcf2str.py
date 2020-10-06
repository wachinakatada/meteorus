# -*- coding: UTF-8 -*-
# Copyright (C) 2020 Nakatada Wachi
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

#python vcf2str.py vcf

import linecache
import sys
import math

num_line = -1 #Define line counters

num_line = -1 #Define line counters

for num_line, line in enumerate(open(sys.argv[1], 'rU')):
 pass
num_line += 1 #Count lines of vcf

data = []

for x1 in range(1, num_line + 1):
	line = linecache.getline(sys.argv[1], x1) #Note: linecache start get line of 1, not 0 as in list.
	
	line = line.rstrip('\n')
	line = line.split('\t')
	line = [s for s in line if s != ""]
	
	locus = []
	
	if line[0] == '#CHROM':
		sample = line[9:]
	if not line[0][0] == '#':
		
		#A:0,T:1,G:2,C:3,-:-9
		if line[3] == "A":
			REF = "0"
		if line[3] == "T":
			REF = "1"
		if line[3] == "G":
			REF = "2"
		if line[3] == "C":
			REF = "3"
		
		if line[4] == "A":
			ALT = "0"
		if line[4] == "T":
			ALT = "1"
		if line[4] == "G":
			ALT = "2"
		if line[4] == "C":
			ALT = "3"
		
		line = line[9:]
		
		for x in range(len(line)):
			if line[x]=='./.':
				locus.append(["-9","-9"])
			if line[x]=='0|0':
				locus.append([REF,REF])
			if line[x]=='0|1':
				locus.append([REF,ALT])
			if line[x]=='1|0':
				locus.append([ALT,REF])
			if line[x]=='1|1':
				locus.append([ALT,ALT])
		print len(locus),locus
		data.append(locus)
		locus=[]

name=str(sys.argv[1]).rstrip(".vcf")
name=name+".str"
f=open(name,"a")

for y in range(len(sample)*2):
	if int(y)%2 == 0:
		f.write(sample[int(y)/2])
		f.write("   					")
		
		for z1 in range(len(data)):
			f.write("\t")
			f.write(data[z1][int(y)/2][0])
		f.write("\n")
		
	if int(y)%2 == 1:
		f.write(sample[int(y-1)/2])
		f.write("   					")
		
		for z2 in range(len(data)):
			f.write("\t")
			f.write(data[z2][int(y-1)/2][1])
		f.write("\n")
f.close