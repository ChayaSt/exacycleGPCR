# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 16:10:08 2014

@author: sternc1
"""

import mdtraj as md
import os

targets=['agonist_b2ar','inverse_agonist_b2ar']
pdbs=['active_crystal_reference','inactive_crystal_reference']
for target, pdb in zip(targets,pdbs):
    path = '/home/chayas/src/choderalab/GPCRexacycle/%s_trajectories' % target
    listing=os.listdir(path)
    for infile in listing:
        print infile
        t1=md.load_lh5('/home/chayas/src/choderalab/GPCRexacycle/%s_trajectories/%s' % (target ,infile))
        t2=md.load('/home/chayas/src/choderalab/GPCRexacycle/GPCR_NatureChemistry/reference-structures/%s.pdb' % pdb)
        table1, bonds1 = t1.topology.to_dataframe()
        table2, bonds2 = t2.topology.to_dataframe()
        t1.topology = t2.topology
        t1.save('/home/chayas/src/choderalab/GPCRexacycle/dcd_trajectories/%s/%s.dcd' %(target,infile))

    
