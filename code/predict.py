#!/usr/bin/env python

"""Script to predict contacts, given the 12 input files"""

from sklearn.ensemble import RandomForestClassifier
import pickle, sys
import os


if len(sys.argv) != 13:
	print 'Usage: ' + sys.argv[0] + ' <output files>'
	print 'Output files need to come in *order*!'
	print 'That is:'
	print ' JackHMMER 1e-4 Psicov'
	print ' JackHMMER 1e-4 DCA'
	print ' JackHMMER 1e-0 Psicov'
	print ' JackHMMER 1e-0 DCA'
	print ' JackHMMER 1e-10 Psicov'
	print ' JackHMMER 1e-10 DCA'
	print ' HHblits 1e-4 Psicov'
	print ' HHblits 1e-4 DCA'
	print ' HHblits 1e-0 Psicov'
	print ' HHblits 1e-0 DCA'
	print ' HHblits 1e-10 Psicov'
	print ' HHblits 1e-10 DCA'
	sys.exit(1)

chosen = range(12)
files = sys.argv[1:]
forrest = pickle.load(open(os.path.dirname(os.path.abspath(sys.argv[0])) + '/forest.dat'))

maxres = -1
selected = set()
contacts = {}
X = []
Y = []
for index in range(12):
	contacts[index] = {}
	d = files[index]
	r = []
	if not os.path.exists(d):
		sys.stderr.write(d + ' does not exist!\n')
		sys.exit(1)
	infile = open(d).readlines()
	if len(infile) < 1:
		sys.stderr.write(d + ' is empty!\n')
		sys.exit(1)
	for m in infile:
		x = m.split()
		if index % 2 == 0:
			if len(x) != 5:
				print d + ' has wrong format!'
				sys.exit(1)
			c = 4
		else:
			if len(x) != 4:
				print d + ' has wrong format!'
				sys.exit(1)
			c = 3
		aa1 = int(x[0])
		aa2 = int(x[1])
		if aa1 > maxres:
			maxres = aa1
		if aa2 > maxres:
			maxres = aa2	
		if abs(aa1 - aa2) < 5:
			continue
		score = float(x[c])
		selected.add( (aa1, aa2) )
		contacts[index][(aa1, aa2)] = score

for s in sorted(list(selected)):
	q = []
	for index in chosen:
		try:
			q.append(contacts[index][s])
		except:
			pass

	if len(q) == len(chosen):
		X.append(q)
		Y.append(s)

predictionf = forrest.predict_proba(X)

for l in range(len(Y)):
	(aa1, aa2) = (Y[l][0], Y[l][1])
	print '{:d} {:d} {:6.4f}'.format(aa1, aa2, predictionf[l][1])


