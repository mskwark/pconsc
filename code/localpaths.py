import sys

# Directory where the distributable package is located
# e.g. root = '/afs/pdc.kth.se/home/m/mjs/volume4/correlated-bench/'
root = '/afs/pdc.kth.se/home/m/mjs/volume4/correlated-bench/distributable/'

if len(root) < 1:
	print 'You need to modify localpaths.py to use this script!'
	sys.exit(0)

# Path to formatdb formatted sequence database (e.g. Uniref90, nr90 etc.)
#uniref100 = '/home/mjs/db/uniref/uniref100.fasta'
uniref100 = '/home/mjs/db/uniref/MessyUniref100'
hhblitsdb = '/home/mjs/db/hhpred/new/nr20_12Aug11'

# Path to MATLAB executable
matlab = '/afs/pdc.kth.se/pdc/vol/matlab/r2012a/bin/matlab'

# Path to JackHMMER executable
jackhammer = root + 'bin/jackhmmer'
hhblits = '/home/mjs/sw/hhsuite/bin/hhblits'
psicov = root + 'bin/psicov'
print jackhammer


# These are included. Should not need changing
scriptpath = root + 'scripts'
trim = root + 'scripts/trim.py'
trim2 = root + 'scripts/trimToFasta.py'
reformat = root + 'scripts/reformat.pl'
dca = root + 'scripts/dca.m'

