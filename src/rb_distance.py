from dendropy import Tree
import dendropy
from dendropy.calculate import treecompare
import os
import pandas as pd

def load_tree_from_file(file_name:str, namespace)->Tree:
    return Tree.get(path=file_name,
        schema="nexus",
        collection_offset=0,
        tree_offset=0, taxon_namespace=namespace)

def distance(left:Tree, right:Tree)-> int:
    return treecompare.symmetric_difference(left, right)

def __file_name_extraction__()->dict:
    tree_files = list(filter(lambda file_name: '.nex' in file_name, os.listdir('output')))
    data = {}
    ds = dendropy.DataSet()
    namespace = ds.new_taxon_namespace()
    for each in tree_files:
        tree_name = each.strip('.nex')
        file_path = f'output/{each}'
        tree =load_tree_from_file(file_path,namespace)
        data[tree_name] = tree
    return data

def build_dataframe():
    trees = __file_name_extraction__()
    tree_names = list(trees.keys())
    for left in tree_names:
        for right in tree_names:
            print(left, right, distance(trees[left], trees[right]))

if __name__ == '__main__':
    build_dataframe()
