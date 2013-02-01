#!/usr/bin/env python

from localpaths import *
import sys, subprocess, os
import string as s

def check_output(command):
	return subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
	
if len(sys.argv) < 2:
	print sys.argv[0], '<sequence file>'
	sys.exit(0)

seqfile = sys.argv[1]

rundir = seqfile.rfind('/')
if rundir < 0:
	rundir = '.'
else:
	rundir = seqfile[:rundir]

if not os.path.exists(seqfile):
	print seqfile, 'does not exist'
	sys.exit(0)

f = open(seqfile).read()

if os.path.exists(seqfile + '.fasta'):
	subprocess.call(['mv', seqfile + '.fasta', seqfile +'.bak'])

f2 = open(seqfile +'.fasta', 'w')
if f[0] != '>':
	f2.write('>target\n' + f +'\n')
else:
	x = f.split('\n')
	if len(x[0]) > 6:
		target = x[0][1:5] + x[0][6]
	f2.write('>target\n' + "".join(x[1:]) + '\n')
f2.close()

names = ['E4', 'E0', 'E10']
cutoffs = ['1e-4', '1', '1e-10']

predictionnames = []
for i in range(3):
	sys.stderr.write('jackhmmer ' + names[i] + '\n')
	if not os.path.exists(seqfile + '.jh' + names[i] + '.fas'):
		t = check_output([jackhammer, '--cpu', '4', '-N', '5', '-E', '0.1', '-A', seqfile +'.jh' + names[i] + '.ali', seqfile + '.fasta', uniref100])
		check_output([reformat, 'sto', 'fas', seqfile + '.jh' + names[i] + '.ali', seqfile + '.jh' + names[i] + '.fas'])
		check_output(['rm', seqfile + '.jh' + names[i] + '.ali'])

	if not os.path.exists(seqfile + '.jh' + names[i] + '.psicov'):
        	t = check_output([trim, seqfile + '.jh' + names[i] + '.fas'])
		f = open(seqfile + '.jh' + names[i] + '.jones', 'w')
		f.write(t)
		f.close()
		sys.stderr.write("Running psicov\n")
		if not os.path.exists(seqfile + '.jh' + names[i] + '.psicov'):
			t = check_output([psicov, seqfile + '.jh' + names[i] + '.jones'])
			f = open(seqfile + '.jh' + names[i] + '.psicov', 'w')
			f.write(t)
			f.close()

	predictionnames.append(seqfile + '.jh' + names[i] + '.psicov')
	t = check_output([trim2, seqfile + '.jh' + names[i] + '.fas'])
	f = open(seqfile + '.jh' + names[i] + '.trimmed', 'w')
	f.write(t)
	f.close()

	if not os.path.exists(seqfile + '.jh' + names[i] + '.dca'):
		sys.stderr.write("Running DCA\n")
		t = check_output([matlab, '-nodesktop', '-nojvm', '-r', "path(path, '" + scriptpath + "'); dca " + seqfile + '.jh' + names[i] + '.trimmed ' + seqfile + '.jh' + names[i] + '.dca; exit'])
	predictionnames.append(seqfile + '.jh' + names[i] + '.dca')

	sys.stderr.write('HHblits ' + names[i] + '\n')
	if not os.path.exists(seqfile + '.hh' + names[i] + '.fas'):
		t = check_output([hhblits, '-oa3m', seqfile + '.hh' + names[i] + '.a3m', '-i', seqfile + '.fasta', '-d', hhblitsdb])
		check_output([reformat, 'a3m', 'fas', seqfile + '.hh' + names[i] + '.a3m', seqfile + '.hh' + names[i] + '.fas'])
	
	if not os.path.exists(seqfile + '.hh' + names[i] + '.psicov'):
        	t = check_output([trim, seqfile + '.hh' + names[i] + '.fas'])
		if len(t) < 10:
			sys.exit(0)
		f = open(seqfile + '.hh' + names[i] + '.jones', 'w')
		f.write(t)
		f.close()
		sys.stderr.write("Running psicov\n")
		if not os.path.exists(seqfile + '.hh' + names[i] + '.psicov'):
			t = check_output([psicov, seqfile + '.hh' + names[i] + '.jones'])
			f = open(seqfile + '.hh' + names[i] + '.psicov', 'w')
			f.write(t)
			f.close()

	predictionnames.append(seqfile + '.hh' + names[i] + '.psicov')
	t = check_output([trim2, seqfile + '.hh' + names[i] + '.fas'])
	f = open(seqfile + '.hh' + names[i] + '.trimmed', 'w')
	f.write(t)
	f.close()

	if not os.path.exists(seqfile + '.hh' + names[i] + '.dca'):
		sys.stderr.write("Running DCA\n")
		t = check_output([matlab, '-nodesktop', '-nojvm', '-r', "path(path, '" + scriptpath + "'); dca " + seqfile + '.hh' + names[i] + '.trimmed ' + seqfile + '.hh' + names[i] + '.dca; exit'])
	predictionnames.append(seqfile + '.hh' + names[i] + '.dca')


results = check_output([os.path.dirname(os.path.abspath(sys.argv[0])) + '/predict.py'].extend(predictionnames))

print results
