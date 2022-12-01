import tangos as db

import numpy as np

def calculate_distance(center1, center2):
    return np.sqrt((center1[0]-center2[0])**2+(center1[1]-center2[1])**2+(center1[2]-center2[2])**2)

def find_all_distances(sim_name,outfn, n):

    with open(outfn, 'w') as outfile:
        outfile.write('z halo_num distance\n')

    sim = db.get_simulation(sim_name)

    timesteps = sim.timesteps

    all_main_halos = timesteps[-1].halos[0].calculate_for_progenitors('halo_number()')[0]-1
    all_main_halos = np.flip(all_main_halos)

    distances_per_timestep = []
    for i in range(n):
        print(str(i))
        halos = timesteps[i].halos
        print(f'num halos: {halos.count()}')
        main_halo = halos[all_main_halos[i]]

        main_halo_center = [main_halo['Xc'], main_halo['Yc'], main_halo['Zc']]
        z = main_halo.calculate('z()')
        
        distances_per_halo = []
        for halo in halos:
            halo_num = halo.calculate('halo_number()')
            halo_center = [halo['Xc'], halo['Yc'], halo['Zc']]
        
            distance = calculate_distance(main_halo_center, halo_center)
            distances_per_halo.append(distance)

            with open(outfn, 'a') as outfile:
                outfile.write(f'{z:.2f} {halo_num} {distance:.16f}\n')
        distances_per_timestep.append(distances_per_halo)

sim_name = 'h148.cosmo50PLKvdXsec.6144.VTS'
outfn = './distance_calc_test.dat'
n = 2

find_all_distances(sim_name, outfn, n)