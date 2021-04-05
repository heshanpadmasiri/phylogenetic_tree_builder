from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
import matplotlib.pyplot as plt
import matplotlib
import argparse


def build_tree(alignment_file: str) -> Phylo.BaseTree.Tree:
    alignemt = AlignIO.read(alignment_file, 'fasta')
    calculator = DistanceCalculator('identity')
    tree_counstructor = DistanceTreeConstructor()
    tree = tree_counstructor.upgma(calculator.get_distance(alignemt))
    return tree


def to_nexus_file(tree: Phylo.BaseTree.Tree, output_name: str) -> None:
    Phylo.write([tree], f'{output_name}_tree.nex', 'nexus')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Create phylogenetic tree using the alignment output")
    parser.add_argument('alignment_file',
                        type=str,
                        help='FASTA alignment file from clustal Omega')
    parser.add_argument('--silent',
                        type=bool,
                        help="Don't show any outputs",
                        default=False)
    args = parser.parse_args()
    tree = build_tree(args.alignment_file)
    output_name = args.alignment_file.strip('_alignment.fasta')
    if not args.silent:
        matplotlib.rc('font', size=6)
        fig = plt.figure(figsize=(10, 80), dpi=100)
        axes = fig.add_subplot(1, 1, 1)
        Phylo.draw(tree, do_show=False, label_func=lambda x: None if 'Inner' in str(x) else str(x))
        plt.savefig(f'{output_name}.png', dpi=100)
    to_nexus_file(tree, output_name)
