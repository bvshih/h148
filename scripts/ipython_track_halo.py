import numpy as np

import pandas as pd

import tangos as db

sim_name = 'h148.cosmo50PLKvdXsec.6144.VTS'
sim = db.get_simulation(sim_name)
halos = sim.timesteps[-1].halos

last_timestep_in_file = 1824
last_halo_in_file = 3
last_z0_halo_in_file = 2

starting_halo = db.get_halo(f'{sim_name}/%{last_timestep_in_file}/halo_{last_halo_in_file - 1}')
print(starting_halo)

#all_t = np.flip(halos[0].calculate_for_progenitors('z()')[0])

all_t = halos[last_z0_halo_in_file].calculate_for_progenitors('z()')[0]
starting_t = starting_halo.calculate('z()')
starting_index = np.where(np.isclose(all_t, starting_t))[0][0]

halo = halos[last_z0_halo_in_file-1]

for i in range(starting_index, len(all_t)):
    print(i)
    halo_num = halo.calculate('earlier('+str(i+1)+')').halo_number
    step_num = halo.calculate('earlier('+str(i+1)+')').timestep

    print('%i %i %i\n' % (int(step_num.extension[-6:]), halo.halo_number, halo_num))



