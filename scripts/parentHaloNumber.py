from tangos.properties import PropertyCalculation
import tangos

import numpy as np 

class parentHalo(PropertyCalculation):
    names = "parentHaloNumber"

    def requires_property(self):
        return ["parentHalo"]

    def calculate(self, particle_data, halo):
        if halo['parentHalo'] == 0:
            return -1
        else:
            return halo['parentHalo'].halo_number