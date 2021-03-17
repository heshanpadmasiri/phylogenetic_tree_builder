import os
import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import argparse


def build_gene_sequence(gene: str, data_dir: str) -> None:
    gene = gene.replace('_', ' ')
    species = list(
        map(lambda each: each.strip('.csv'),
            filter(lambda each: '.csv' in each, os.listdir(data_dir))))
    sequences = []
    for each in species:
        df = pd.read_csv(os.path.join(data_dir, f'{each}.csv'))
        data = df[df['gene'] == gene]
        start = int(data['start'])
        stop = int(data['stop'])
        for record in SeqIO.parse(os.path.join(data_dir, f"{each}.fasta"),
                                  "fasta"):
            sequence = record.seq[start:stop]
        sequences.append(SeqRecord(sequence, each, gene, ""))
    SeqIO.write(sequences, f"output/{gene.replace(' ','_')}.fasta", "fasta")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=
        "Create input file for the clustal Omega multiple sequence alignment")
    parser.add_argument('gene',
                        type=str,
                        help='Name of the gene. Use _ insted of spaces')
    parser.add_argument(
        '--data',
        type=str,
        help="Optional localtion of the data files default data",
        default='data')
    args = parser.parse_args()
    build_gene_sequence(args.gene, args.data)
