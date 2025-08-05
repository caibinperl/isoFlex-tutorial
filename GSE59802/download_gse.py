import os

data_dir = 'GSE59802'
with open(os.path.join(data_dir, 'SRR_Acc_List.txt'), 'rt') as fin:
    for line in fin:
        line = line.strip()
        if line:
            fq_dir = os.path.join(data_dir, 'raw')
            cmd = f"fasterq-dump --split-3 {line} -O {fq_dir}"
            print(cmd)
            os.system(cmd)