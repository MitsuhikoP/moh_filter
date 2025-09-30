# moh_filter

Locus filtering software based on Maximal Observed Heterogeneity from VCF file.  
This emulates "--max-obs-het" option in Stacks.


```
python3 moh_filter.py -i input.vcf -o output.vcf -m 0.8
```

optional arguments:  
  -h, --help  show this help message and exit  
  -i str      input vcf file  
  -o str      output vcf file name  
  -m float    max observed heterozygosity (default < 0.8)  