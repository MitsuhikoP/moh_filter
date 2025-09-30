# moh_filter

filtering software based on max observed heterogeneity from VCF file.

```
python3 moh_filter.py -i input.vcf -o output.vcf -m 0.8
```

optional arguments:
  -h, --help  show this help message and exit
  -i str      input vcf file
  -o str      output vcf file name
  -m float    max observed heterozygosity (default < 0.8)