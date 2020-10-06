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

#python vcf2count_hetero.py vcf pop_list

import linecache
import sys
import math

num_line = -1 #Define line counters

for num_line2, line in enumerate(open(sys.argv[2], 'rU')):
	pass
num_line2 += 1 #Count lines of pop file

sample=[]

for x2 in range(1, num_line2 + 1):
#	print line
	line = linecache.getline(sys.argv[2], x2)
	line = line.rstrip("\n")
	line = line.split("\t")
	sample.append(line) #make population list

num_line = -1 #Define line counters

for num_line, line in enumerate(open(sys.argv[1], 'rU')):
 pass
num_line += 1 #Count lines of vcf

data0 = []

for x1 in range(1, num_line + 1):
	line = linecache.getline(sys.argv[1], x1) #Note: linecache start get line of 1, not 0 as in list.
	line = line.rstrip('\n')
	if line[0] == '#':
		line = line.split('\t')
		if line[0] == '#CHROM':
			data0 = line

data_index0 = []

for x2 in range(0, len(sample)):
	data_index0.append([])
	for x3 in range(0, len(sample[x2])):
		data_index0[x2].append(data0.index(sample[x2][x3]))

cnt=0
cnt0=0 #biallelic
cnt1=0 #missing

data_het=[]

for x1 in range(1, num_line + 1):
	line = linecache.getline(sys.argv[1], x1) #Note: linecache start get line of 1, not 0 as in list.
	line = line.rstrip('\n')
	
	if not line[0] == '#':
		cnt += 1
		site0=[]
		site1=[]
		line = line.split('\t')
		
		if len(line[4]) == 1:
			cnt0 += 1
		
			pop=[]
			for y1 in range(len(data_index0)):
				pop.append([])
				for y2 in range(len(data_index0[y1])):
					pop[y1].append(line[data_index0[y1][y2]])
			het=[]
			for z1 in range(len(pop)):
				pop[z1] = [s for s in pop[z1] if s != "./."]
				if not len(pop[z1]) == 0:
					freq=float(pop[z1].count("1|0")+pop[z1].count("0|1"))/len(pop[z1])
					het.append(str(freq))
				else:
					het.append("NA")
					cnt1 += 1
					
			data_het.append(het)
			print cnt,het[0],het[1]
			het=[]
			pop=[]

#cnt
#cnt0 biallelic
#cnt1 missing

print "N", cnt
print "biallelic", cnt0
print "missing", cnt1
print "shared heterozygote:", data_het.count(['1.0', '1.0'])

cnt2=0
cnt3=0

for x in range(len(data_het)):
	if data_het[x][0] == "1.0":
		if not data_het[x][1] == "1.0" and (not data_het[x][1] == "NA"):
			cnt2 += 1
	
	if data_het[x][1] == "1.0":
		if not data_het[x][0] == "1.0" and (not data_het[x][0] == "NA"):
			cnt3 += 1

print "fixed hetero in pop1:", cnt2
print "fixed hetero in pop2:", cnt3
