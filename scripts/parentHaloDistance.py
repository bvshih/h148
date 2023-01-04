from tangos.properties import PropertyCalculation
import tangos

import numpy as np 

class parentHaloDistance(PropertyCalculation):
    names = "parentHaloDistance"

    def requires_property(self):
        return ["parentHalo", "shrink_center"]


    def calculate(self, particle_data, halo):
        

    def preloop(self, particle_data, timestep):
        self.centres, self.radii, self.dbid = timestep.calculate_all('shrink_center',"max_radius","dbid()")
