import os

in_dir = "raw"
out_dir = "fastqs"

with open(os.path.join(in_dir, "SRR_Acc_List.txt"), "rt") as fin:
    for line in fin:
        sample = line.strip()
        if sample:
            in_fq = os.path.join(in_dir, sample + ".fastq")
            out_fq = os.path.join(out_dir, sample + ".fastq")
            html = os.path.join(out_dir, sample + ".html")
            json = os.path.join(out_dir, sample + ".json")
            cmd = f"fastp -i {in_fq} -o {out_fq} -h {html} -j {json} -l 13 -a TGGAATTCTCGGGTGCCAAGGAACTCC"
            print(cmd)
            os.system(cmd)

    