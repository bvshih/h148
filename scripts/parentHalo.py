from tangos.properties import PropertyCalculation
from tangos import get_halo
import numpy as np 

import pandas as pd

class parentHalo(PropertyCalculation):
    names = "parentHalo"

    def requires_property(self):
        return ["shrink_center", 'contamination_fraction']


    def calculate(self, particle_data, halo):

        #offsets = np.linalg.norm(np.array([halo['Xc'], halo['Yc'], halo['Zc']]) - self.centres, axis=1)
        offsets = np.linalg.norm(halo['shrink_center'] - self.centres, axis=1)
        
        # print('self.centres length:', len(self.centres))
        # print('self.centres:', self.centres, '\n')
        # print('existing_properties["shrink_center"]:', existing_properties['shrink_center'],'\n')
        # print('offsets:', offsets)

        offsets[offsets<1e-5] = np.inf # exclude self!
        inside_mask = offsets<self.radii

        # print('offsets length:', len(offsets), '\n')
        # print('self.radii length:', len(self.radii), '\n')

        # print('inside_mask:', inside_mask, '\n')

        # print('offsets:', offsets)

        # print('self.radii:', self.radii)

        if np.any(inside_mask):      
            # print('masked rmax:', self.radii[inside_mask])
            
            # print('dbid: ', self.dbid[self.radii[inside_mask].argmax()])
            dbid_masked = self.dbid[inside_mask]
            # print('masked dbid: ', dbid_masked[self.radii[inside_mask].argmax()])

            return get_halo(dbid_masked[self.radii[inside_mask].argmax()]).halo_number()
        else:
            return -1

    def preloop(self, particle_data, timestep):
        #self.xc, self.yc, self.zc , self.radii, self.dbid = timestep.calculate_all('Xc','Yc', 'Zc',"Rhalo","dbid()")

        #self.centres = [self.xc, self.yc, self.zc]
        
        self.centres, self.radii, self.dbid = timestep.calculate_all('shrink_center',"max_radius","dbid()")
