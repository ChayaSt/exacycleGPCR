import glob
import mixtape.featurizer, mixtape.tica, mixtape.cluster, mixtape.markovstatemodel
import numpy as np
import mdtraj as md
from mixtape import ghmm, subset_featurizer, selector 
#from parameters import load_trajectories, build_full_featurizer
import sklearn.pipeline, sklearn.externals.joblib
import mixtape.utils


n_iter = 1000

n_choose = 100
stride = 1
lag_time = 1

PDB =  md.load_pdb('../../GPCR_NatureChemistry/reference-structures/apo_snapshot.pdb')

filenames = glob.glob("../../dcd_trajectories/apo_b2ar_processed/trj*")

#trajectories = [md.load(filename) for filename in filenames[::50]]
train = [md.load(filename, top=PDB) for filename in filenames[::2]]
for i in range(10):
	
	#featurizer = build_full_featurizer(trj0, n_choose)  # Doesn't work right now, too many features need to re-optimize later.
	featurizer = sklearn.externals.joblib.load("./featurizer%d-%d.job" % (i,n_choose))

	tica_optimizer = mixtape.selector.TICAOptimizer(featurizer, train, lag_time=lag_time)
	tica_optimizer.optimize(n_iter, train)


	sklearn.externals.joblib.dump(tica_optimizer.featurizer, "./featurizer%d-%d.job" % (i+1, n_choose), compress=True)


