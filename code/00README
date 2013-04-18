***************************************************
 PconsC : Combination of direct information methods 
         and alignments improves contact prediction
***************************************************

PconsC requires:
	* Python interpreter (tested from Python 2.7 onwards)
	* jackhmmer (part of HMMER package http://hmmer.janelia.org/software)
	* HHblits 2.0.15 or newer (ftp://toolkit.genzentrum.lmu.de/pub/HH-suite/)
	* PSICOV (http://bioinfadmin.cs.ucl.ac.uk/downloads/PSICOV/)
	* sequence databases for jackhmmer (BLAST-formatted protein database, 
	  e.g. nr90, uniref90) and HHblits (bundled with software, nr20)
	* MATLAB for running plmDCA (necessarily with Java VM enabled)

After installing the necessary software, set paths in localconfig.py

Usage:
------

PconsC method is optimized for e-value cutoffs of: 1e-40, 1e-10, 1e-4 and 1e0
and requires 16 files with individual predictions, to work. That is:

	 JackHMMER 1e-4 Psicov
	 JackHMMER 1e-4 plmDCA
	 JackHMMER 1e-0 Psicov
	 JackHMMER 1e-0 plmDCA
	 JackHMMER 1e-10 Psicov
	 JackHMMER 1e-10 plmDCA
	 JackHMMER 1e-40 Psicov
	 JackHMMER 1e-40 plmDCA
	 HHblits 1e-4 Psicov
	 HHblits 1e-4 plmDCA
	 HHblits 1e-0 Psicov
	 HHblits 1e-0 plmDCA
	 HHblits 1e-10 Psicov
	 HHblits 1e-10 plmDCA
	 HHblits 1e-40 Psicov
	 HHblits 1e-40 plmDCA

Output files need to come in *order*!

If you have these files, use ./predict.py to predict contacts (note the input
order again!) If you want to omit one (or more) of the files, please feel free to do
so by providing a size 0 file as an input. Our experience shows that the method
may perform well also in this case, although the estimated probabilities will
be incorrect, the mutual ranking will still be roughly correct.

NOTE: While this capability is included, we explicitly do not support this usage.

PconsC is capable of generating these file on its own, provided the proper paths
are set. Use ./predictAll.py to generate all the alignments and run all the
predictions. Be aware that it may take longer time. We recommend running individual
predictions in parallel, if possible, but due to vast diversity of available
parallel processing platforms, we are unable to provide any general case support.
Please feel free to contact the authors, if you run into any problems with software
operation either at marcin (at) skwark (dot) pl or arne (at) bioinfo (dot) se.

Output format:
aa1 	aa2 	contact_propensity

Example:
1	5	0.003
1	6	0.007
1	7	0.200
[...]
27	43	0.952

The higher the propensity, the more likely are two residues to be in contact


PSICOV problem
--------------

Recent versions of PSICOV (justly) refuse operation if the input alignment has
insufficient amount of (effective) sequences. PconsC uses PSICOV predictions,
even if they are not trustworthy. Therefore, we recommend disabling the check
for the sufficient alignment complexity.

To do so, modify psicov.c file, before compilation and change:

	#define MINEFSEQS (seqlen)

to:

	#define MINEFSEQS 1

If you DO NOT want to do so, change the value of parameter in localconfig.py from:

	psicovfail = False

to:
	psicovfail = True

This will allow PconsC to overcome this problem, at an expense of potentially 
less accurate predictions.

Additional forests
------------------

For confident users, in extras/ directory we have provided some additional forests
trained on the subsets of alignments/predictions. We provide no support for them, 
but feel free to modify the ./predict.py code to use them instead, if you need to.
We provide a sample ./predictAll-fast.py and ./predict-fast.py scripts, to run the
first of the combinations below. 

We recommend running the version with 16 inputs though, as we believe it provides
greatest accuracy.

*** Input files expected: ***

hh4-psicovplmdca.dat (fastest, accurate combination)
	 HHblits 1e-4 Psicov
	 HHblits 1e-4 plmDCA

hhbjhm-plmdca.dat  
	 JackHMMER 1e-4 plmDCA
	 JackHMMER 1e-0 plmDCA
	 JackHMMER 1e-10 plmDCA
	 JackHMMER 1e-40 plmDCA
	 HHblits 1e-4 plmDCA
	 HHblits 1e-0 plmDCA
	 HHblits 1e-10 plmDCA
	 HHblits 1e-40 plmDCA

hhbjhm-psicov.dat  
	 JackHMMER 1e-4 Psicov
	 JackHMMER 1e-0 Psicov
	 JackHMMER 1e-10 Psicov
	 JackHMMER 1e-40 Psicov
	 HHblits 1e-4 Psicov
	 HHblits 1e-0 Psicov
	 HHblits 1e-10 Psicov
	 HHblits 1e-40 Psicov

hhb-plmdca.dat  
	 HHblits 1e-4 plmDCA
	 HHblits 1e-0 plmDCA
	 HHblits 1e-10 plmDCA
	 HHblits 1e-40 plmDCA

hhb-psicov.dat  
	 HHblits 1e-4 Psicov
	 HHblits 1e-0 Psicov
	 HHblits 1e-10 Psicov
	 HHblits 1e-40 Psicov

hhb-psicovplmdca.dat  
	 HHblits 1e-4 Psicov
	 HHblits 1e-4 plmDCA
	 HHblits 1e-0 Psicov
	 HHblits 1e-0 plmDCA
	 HHblits 1e-10 Psicov
	 HHblits 1e-10 plmDCA
	 HHblits 1e-40 Psicov
	 HHblits 1e-40 plmDCA

jhm-plmdca.dat  
	 JackHMMER 1e-4 plmDCA
	 JackHMMER 1e-0 plmDCA
	 JackHMMER 1e-10 plmDCA
	 JackHMMER 1e-40 plmDCA

jhm-psicov.dat  
	 JackHMMER 1e-4 Psicov
	 JackHMMER 1e-0 Psicov
	 JackHMMER 1e-10 Psicov
	 JackHMMER 1e-40 Psicov

jhm-psicovplmdca.dat
	 JackHMMER 1e-4 Psicov
	 JackHMMER 1e-4 plmDCA
	 JackHMMER 1e-0 Psicov
	 JackHMMER 1e-0 plmDCA
	 JackHMMER 1e-10 Psicov
	 JackHMMER 1e-10 plmDCA
	 JackHMMER 1e-40 Psicov
	 JackHMMER 1e-40 plmDCA
