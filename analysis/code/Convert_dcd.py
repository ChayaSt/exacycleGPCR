# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 16:10:08 2014

@author: sternc1
"""

import mdtraj as md
import os

targets=['apo_b2ar','agonist_b2ar','inverse_agonist_b2ar']
pdbs=['apo_snapshot','active_crystal_reference','inactive_crystal_reference']
for target, pdb in zip(targets,pdbs):
    path = '/Users/sternc1/src/choderalab/exacycleGPCR/%s_trajectories' % target
    listing=os.listdir(path)
    for infile in listing:
#        print infile
        t1=md.load_lh5('/Users/sternc1/src/choderalab/exacycleGPCR/%s_trajectories/%s' % (target ,infile))
        t2=md.load('/Users/sternc1/src/choderalab/exacycleGPCR/GPCR_NatureChemistry/reference-structures/%s.pdb' % pdb)
        table1, bonds1 = t1.topology.to_dataframe()
        table2, bonds2 = t2.topology.to_dataframe()
        t1.topology = t2.topology
        t1.save('/Users/sternc1/src/choderalab/exacycleGPCR/dcd_trajectories/%s/%s.dcd' %(target,infile))

    