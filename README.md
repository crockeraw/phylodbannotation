# phylodbannotation
Small script and sample data to merge phylodb data with Kallisto output for gene and taxonomy annotation. Will update in the future to include other quantification/count tools (Salmon, samfiles) and greater i/o capabilities. Also planning on adding support for contig annotation assembled from Trinity.  


## How to use
- Note: Phylodb must be downloaded for this, it contains the taxonomy and gene annotation data to go with the database fasta file. It can be downloaded as a zip file [here.](https://drive.google.com/folderview?id=0B-BsLZUMHrDQfldGeDRIUHNZMEREY0g3ekpEZFhrTDlQSjQtbm5heC1QX2V6TUxBeFlOejQ&usp=sharing)
- Clone this repository into a directory of choice using `$ git clone https://github.com/Lswhiteh/phylodbannotation`

### For aligning reads against PhyloDB with Kallisto (Tagseq protocol) - No Assembly
1. Create PhyloDB Kallisto index and map reads against the database.
2. Copy the `abundances.tsv` file from the Kallisto output dir, preferably with a more specific name, to a directory containing `taxonomymatcher.py`. 
3. Copy the PhyloDB gene and taxonomy annotation tsv files to the same directory.
4. Run `taxonomymatcher.py` either one at a time or with bash scripting, a simple example where C{number}abundances.tsv represents multiple files with this name pattern of Kallisto output:
 
```
for i in `ls C*abundances.tsv`
do

python taxonomymatcher.py -i ${i} -o ${i}_annotated
done
```
- Note that the script is run with a specified input tsv and a specified output tsv, if these are not given the script will not run (for now). 

### For merging data from Trinity output
- Coming soon!
