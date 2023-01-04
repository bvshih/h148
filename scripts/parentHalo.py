from tangos.properties import PropertyCalculation
import tangos

import numpy as np 

class parentHalo(PropertyCalculation):
    names = "parentHalo"

    def requires_property(self):
        return ["shrink_center", 'contamination_fraction']


    def calculate(self, particle_data, halo):
        offsets = np.linalg.norm(halo['shrink_center'] - self.centres, axis=1)

        offsets[offsets<1e-5] = np.inf # exclude self!
        inside_mask = offsets<self.radii

        if np.any(inside_mask):                  
            dbid_masked = self.dbid[inside_mask]

            return tangos.get_halo(dbid_masked[self.radii[inside_mask].argmax()])
        else:
            return tangos.get_halo(halo)

    def preloop(self, particle_data, timestep):
        self.centres, self.radii, self.dbid = timestep.calculate_all('shrink_center',"max_radius","dbid()")
