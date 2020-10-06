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

#python vcf2specific_loci.py vcf ind1_ind2_list 0.5[max heterozygosity]
#ind1, heterozygosity excess
#ind2, heterozygote in haploid

import linecache
import sys
import math

lim = sys.argv[3]

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

name=str(sys.argv[1]).rstrip(".vcf")
name=name+"_chosen.vcf"
f=open(name, "a")

cnt=0
cnt0=0 #biallelic
cnt1=0 #putative paralog
cnt2=0 #hetero in male

for x1 in range(1, num_line + 1):
	line = linecache.getline(sys.argv[1], x1) #Note: linecache start get line of 1, not 0 as in list.
	line = line.rstrip('\n')
	if line[0] == '#':
		f.write(line)
		f.write('\n')
	
	if not line[0] == '#':
		cnt += 1
		site0=[]
		site1=[]
		line = line.split('\t')
		
		if len(line[4]) == 1:
			cnt0 += 1
		
			for y1 in range(len(data_index0[0])):
				site0.append(line[data_index0[0][y1]])
			het0=float(site0.count("0|1")+site0.count("1|0"))
			nsite = len(site0) - site0.count("./.")
			
			if not nsite == 0 and float(het0)/nsite <= float(lim):
				cnt1 += 1
			
				if len(data_index0) == 1:
					het1 = 0.0
				
				
				else: 
					for y2 in range(len(data_index0[1])):
						site1.append(line[data_index0[1][y2]])
					het1=float(site1.count("0|1")+site1.count("1|0"))

				if het1 == 0.0:
					cnt2 += 1
				
					f.write(line[0])
				
					for z in range(1, len(line)):
						f.write('\t')
						f.write(line[z])
					f.write('\n')
				
				site1=[]
				het1=[]
			site0=[]

f.close

print "N of Loci:", cnt
print "Biallelic site:", cnt0
print "Putative paralog:", cnt1
print "Hetero in male:", cnt2
