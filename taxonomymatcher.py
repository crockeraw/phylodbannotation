#!/usr/bin/python

import pandas as pd 
import sys, getopt

'''
Usage: taxonomymatcher.py -i <kallisto_abundance_file.tsv> -o <output.tsv>
taxonomymatcher.py compiles Kallisto output with PhyloDB taxonomy and annotation databases.
'''

def get_databases(kallisto_abundance_file, annotations, taxonomies):
    '''
    Loads files from databases and input file, preps for merging
    '''
    abundances = pd.read_csv(kallisto_abundance_file, sep='\t')

    gene_database = pd.read_csv(annotations, sep='\t', \
        names=["gene_id", "idstring", "strain_name", "gene_name"])
    

    taxonomy_database = pd.read_csv(taxonomies, sep='\t')


    return abundances, gene_database, taxonomy_database

    
def data_merger(abundances, gene_database, taxonomy_database):
    '''
    Merges data using joins, cleans up unnecessary columns and 0 TPM rows
    '''
    print(taxonomy_database)

    abundances = abundances.merge(gene_database, left_on = abundances["target_id"], right_on = gene_database["gene_id"])
    
    abundances = abundances.merge(taxonomy_database, left_on = abundances["strain_name"], right_on = taxonomy_database["strain_name"])
    
    abundances = abundances.drop(['strain_name_y', 'idstring', 'gene_id', 'peptide_count'], axis=1)

    abundances = abundances.drop(abundances[abundances['tpm'] == 0].index)



    return abundances

def output_writer(merged_dataframe, outputfile):
    merged_dataframe.to_csv(path_or_buf=outputfile, index=False)


def main(argv):
    
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print("taxonomymatcher.py -i <kallisto_abundance_file.tsv> -o <output.tsv>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: taxonomymatcher.py -i <kallisto_abundance_file.tsv> -o <output.tsv> \n \n" 
                "taxonomymatcher.py compiles Kallisto output with PhyloDB taxonomy and annotation databases. \n")
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
        

    abundances, gene_database, taxonomies = get_databases(inputfile, "/pine/scr/l/s/lswhiteh/phylodbannotation/phylodb_1.076.annotations.txt", "/pine/scr/l/s/lswhiteh/phylodbannotation/phylodb_1.076.taxonomy.txt")

    merged_table = data_merger(abundances, gene_database, taxonomies)
    output_writer(merged_table, outputfile)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("No input/output files specified. \n Usage: taxonomymatcher.py -i <kallisto_abundance_file.tsv> -o <output.tsv> \n")
    else:
        main(sys.argv[1:])    
