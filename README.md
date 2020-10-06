# meteorus

## Scripts for filtering and converting of the vcf file of hymenoptera

### requirements
python 2.7

vcftools

### example data
toy.vcf, 20 loci, 50 SNPs from 20 individuals

ind01-ind06: haploid male

ind07-ind20: diploid female

### 1. checking missing data (using vcftools)
vcftools --vcf toy.vcf --missing-indv --out toy

vcftools --vcf toy.vcf --missing-site --out toy

### 2. remove loci with the excess missing data (using vcftools)
vcftools --vcf toy.vcf --max-missing 0.7 --recode --recode-INFO-all --stdout > toy.l07.vcf

### 3. remove samples with the excess missing data and rearrange the samples
python vcf2rearrange.py toy.l07.vcf rearr_ind.txt

rearr_ind.txt: tab-separated list of the sample names, ind03 and ind17 are not in the list because of the excess missing data

line 1: ind10	ind11	ind12	ind13	ind14	ind15	ind16	ind18	ind19	ind20	ind01	ind02	ind04	ind05	ind06	ind07	ind08	ind09

### 4. count and remove the loci with the excess of heterozygosity (putatively paralogs) and heterozygous loci in haploid males
python vcf2specific_loci.py toy.l07_rearr.vcf female_male.txt 0.5

female_male.txt: tab-separated list of sample names of population to count loci with the excess of heterozygosity (the first line), and list of sample  names of males to count heterozygote in haploid male (the second line; can be omitted)

line 1: ind10	ind11	ind12	ind13	ind14	ind15	ind16	ind18	ind19	ind20	ind07	ind08	ind09

line 2: ind01	ind02	ind04	ind05	ind06

0.5: max heterozygosity in the population defined in the first line of "female_male.txt".

45 sites were retained after the paralog filtering, 32 sites were retained after filtering for heterozygote in haploid male from toy.l07_rearr.vcf
 
N of Loci: 47
 
Biallelic site: 47
 
Putative paralog: 45
 
Hetero in male: 32

### 5. extract the first snp from each locus
python vcf2unlinked.py toy.l07_rearr_chosen.vcf > toy.l07_re_ch_unlink.vcf

### 6. convert to the STRUCTURE format
python vcf2str.py toy.l07_re_ch_unlink.vcf

### 7. obtain the frequency of heterozygote in the defined two populations 
python vcf2count_hetero.py toy.l07_re_ch_unlink.vcf population.txt

population.txt: tab-separated list of the sample names in two populations (population 1: first line, population 2: second line)

first column: snp #

second column: the frequency of heterozygote in population 1

third column: the frequency of heterozygote in population 2

1 0.0 0.0

2 0.0 0.142857142857

3 0.0 0.0

4 0.0 0.0

5 0.0 0.0

6 0.0 0.166666666667

7 0.0 0.0

8 0.0 0.0

9 0.0 0.0

10 0.0 0.142857142857

11 0.0 0.0

12 0.0 0.0

13 0.0 0.0

N 13

biallelic 13

missing 0

shared heterozygote: 0

fixed hetero in pop1: 0

fixed hetero in pop2: 0
