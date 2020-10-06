# !/usr/bin/env python
# python 

# Copyright (C) 2018  Nakatada Wachi
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

# python TrimFASTA_180404.py consensus(fasta)

import linecache
import sys
import re

num_line = -1 #Define line counters

for num_line, line in enumerate(open(sys.argv[1], 'rU')):
	pass
num_line += 1 #Count lines of pop1

#name = str(sys.argv[1]).rstrip(".fa")
#name = re.sub("\\s|\(|\)","",name)
#name = re.sub("-","_",name)
#name = name.split("_")
#print name

list=[]
seq1=""
seq2=""
cnt = -1
for x in range(1, num_line + 1):
	line1 = linecache.getline(sys.argv[1], x) #Note: linecache start get line of 1, not 0 as in list.
	line2 = linecache.getline(sys.argv[1], x-1)
	if not line1[0] == '#':
		#print line1
		
		line1=line1.split("\t")
		line2=line2.split("\t")
		
		if x == 1:
			#print line1_1[0]
			#line1[0] = "1"
			line1 = "\t".join(line1)
			print line1,
		else:
			if not line1[0] == line2[0]:
				#print line1_1[0]
				#line1[0] = "1"
				line1 = "\t".join(line1)
				#print line1[0]
				print line1,
	
	else:
		print line1,
			
		
		
		
		
		
		