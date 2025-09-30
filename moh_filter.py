#!/usr/bin/env python3
# copyright (c) 2025 Mitsuhiko P. Sato. All Rights Reserved.
# Mitsuhiko P. Sato ( E-mail: mitsuhikoevolution@gmail.com )
#coding:UTF-8

def main():
    import collections, re
    from argparse import ArgumentParser
    parser=ArgumentParser(description="",usage="python3 moh_filter.py -i input.vcf -o output.vcf -m 0.8", epilog="")
    parser.add_argument("-i",required=True, type=str, metavar="str", help="input vcf file")
    parser.add_argument("-o",required=True, type=str, metavar="str", help="output vcf file name")
    parser.add_argument("-m",default=0.8, type=float, metavar="float", help="max observed heterozygosity (default < 0.8)")
    args = parser.parse_args()

    fhr=open(args.i, "r")

    out=""
    total=0
    passed=0
    gt_list = set()
    for line in fhr:
        if line.startswith("##"):
            out += line
            continue            
        elif line.startswith("#CHR"):
            out+="##python3 moh_filter.py -i "+args.i+" -o "+args.o+" -m "+str(args.m)+"\n"
            out += line
            continue

        lines = line.rstrip().split()
        total += 1
        gts = [gt.split(":")[0] for gt in lines[9:]]
        gt_cnt = collections.Counter(gts)
        gt_list = gt_list | set(gts)

        HOMO=0
        HETERO=0
        for gt in gt_cnt:
            if gt == "./.":
                continue
            haps = re.split("[/\|]",gt)            
            if haps[0] == haps[1]:
                HOMO += 1
            else:
                HETERO += 1

        if HETERO/(HOMO+HETERO) < args.m:
            passed+=1
            out+=line

    fhr.close()
    fhw=open(args.o, "w")
    fhw.write(out)
    fhw.close()
    print("Total variants = ",total, "Passed variants = ", passed)
    print("Used alleles", gt_list)
        
	
if __name__ == '__main__': main()
