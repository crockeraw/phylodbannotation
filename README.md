# phylodbannotation
Small scripts and sample data to merge phylodb data with Kallisto output or Trinity Fasta output for gene and taxonomy annotation.  


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
- Note that the script is run with a specified input tsv and a specified output tsv, if these are not given the script will not run.

### For merging data from Trinity output
- Get Trinity.fasta output from assembling transcriptomes/genomes
- Using DIAMOND OR BLAST get an m8 tabular file by aligning your contigs against phyloDB, only report 1 hit per contig
- Edit `fastaannotation.py` to include the path to the phylodb gene and taxonomy annotation tabular files
- Run `python3 fastaannotation.py <trinityoutput.fa> <diamondoutput.m8> <annotatedfastaoutput.fa> <mappingfile.tsv>`
  - The script will write `<annotatedfastaoutput.fa>`, a fasta file with the gene, organisms, and taxonomy added to it
  - It will also write `<mappingfile.tsv>`, a tabular file with the Trinity contig ID, gene, organism, and taxonomy cleanly laid out
