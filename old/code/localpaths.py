import sys

sys.stderr.write("""
****************************************************************************
          PconsC : Combination of direct information methods and alignments 
                   improves contact prediction
****************************************************************************

If you use PconsC for contact prediction, please cite the following papers:

Skwark M.J., Abdel-Rehim A. and Elofsson A.  
"PconsC : Combination of direct information methods and alignments improves 
          contact prediction"

Ekeberg M, Lovkvist C, Lan Y., Weigt M. and Aurell E.
"Improved contact prediction in proteins: Using pseudolikelihoods to infer 
          Potts models"
doi: 10.1103/PhysRevE.87.012707

Jones D.T, Buchan D.W.A., Cozzetto D., Pontii M. 
"PSICOV: precise structural contact prediction using sparse inverse covariance 
         estimation on large multiple sequence alignments"
doi: 10.1093/bioinformatics/btr638

Johnson L., Eddy S. and Portugaly E.
"Hidden Markov model speed heuristics and iterative HMM search procedure"
doi:10.1186/1471-2105-11-431

Remmert M., Biegert A., Hauser A. and Soding J.     
"HHblits: lightning-fast iterative protein sequence searching by HMM-HMM
          alignment"
doi:10.1038/nmeth.1818 
-----------------------------------------------------------------------------

""")
# Directory where the distributable package is located
# e.g. root = '/afs/pdc.kth.se/home/m/mjs/volume4/correlated-bench/'
root = ''

if len(root) < 1:
	print 'You need to modify localpaths.py to use this script!'
	sys.exit(0)

# Path to formatdb formatted sequence database (e.g. Uniref90, nr90 etc.)
#uniref100 = '/home/mjs/db/uniref/uniref100.fasta'
uniref100 = ''

# Path to HHblits database
# hhblitsdb = '/home/mjs/db/hhpred/new/nr20_12Aug11'
hhblitsdb = ''

# Path to MATLAB executable
# matlab = '/afs/pdc.kth.se/pdc/vol/matlab/r2012a/bin/matlab'
matlab = ''

# Path to executable files
# jackhammer = root + 'bin/jackhmmer'
# hhblits = '/home/mjs/sw/hhsuite/bin/hhblits'
# psicov = root + 'bin/psicov'
jackhmmer = ''
hhblits = ''
psicov = ''

# These are included. Should not need changing.
scriptpath = root + 'scripts'
trim = root + 'scripts/trim.py'
trim2 = root + 'scripts/trimToFasta.py'

# Reformat script scavenged from HHsuite. Please cite the HHblits paper!
reformat = root + 'scripts/reformat.pl'

plmdca = root + 'scripts/plmDCA_symmetric_v2/plmDCA_symmetric.m'

