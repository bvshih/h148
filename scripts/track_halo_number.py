import tangos as db 
import numpy as np 
import sys 
import os

def new_halo_num_tracker(model, sim_name, ini_stepnum, ini_halo_num):
	halo = db.get_halo(sim_name + '/%' + str(ini_stepnum) + '/halo_' + str(ini_halo_num))
	sim = db.get_simulation(sim_name) 


	#change outfn to include info on which halo number it is at z=0
	outfn   = f'../datfiles/{model}_halo_{ini_halo_num}_track.dat'	
	outfile = open(outfn, 'w+')
	outfile.write('model output z time halo\n')
	
	for i in range(len(halo.calculate_for_progenitors('z()')[0])-1):
		halo_num = halo.calculate('earlier('+str(i+1)+')').halo_number
		step_num = halo.calculate('earlier('+str(i+1)+')').timestep
		z = halo.calculate('earlier('+str(i+1)+')').calculate('z()')
		t = halo.calculate('earlier('+str(i+1)+')').calculate('t()')
		outfile.write('%s %i %.2f %.2f %i\n' % (model, int(step_num.extension[-6:]), z, t, halo_num))
	outfile.close()


def all_halos_tracker(model, sim_name):
	'''
	model: model name
	sim_name: sim name used in tangos
	z0_ts: timestep number for z = 0
	'''

	outfn   = '../datfiles/' +  model + '_all_halo_track.dat'	

	#check if outfile already exists
	if os.path.exists(outfn):
		print(f'dat file exists at {outfn}')
		outfile = open(outfn, 'r')
		lines = [line for line in outfile]
		outfile.close()
		
		#finds what the last entry in the file is 	
		if len(lines) == 1 :
			#file only has column names written
			#start at z = 0
			#start with first halo (halo_1)
			
			print(f'dat file only has headers, starting with z = 0 and halo_1')
			last_timestep_in_file = 0
			last_halo_in_file = 1
			z0_halo_num = 1
		else:
			last_line = lines[-1].split()

			last_timestep_in_file = last_line[1]
			last_halo_in_file = int(last_line[-1])
			z0_halo_num = int(last_line[-2])

			print(f'dat file has entries, starting with halo_{last_halo_in_file} in timestep {last_timestep_in_file}')

	#creates an outfile if one doesnt already exist
	else:
		print(f'dat file does not exist, creating dat file and header at {outfn}')
		last_timestep_in_file = 0
		last_halo_in_file = 1
		z0_halo_num = 1

		with open(outfn, 'a') as outfile:
			outfile.write('model output z time z0_halo_num halo_num\n')


	#load simulation and halos
	sim = db.get_simulation(sim_name)
	halos_count = sim.timesteps[-1].halos.count()


	if last_timestep_in_file == 0:	
		halo = sim.timesteps[-1].halos[0]
	else:
		halo = db.get_halo(f'{sim_name}/%{last_timestep_in_file}/halo_{last_halo_in_file}')


	#run thru each halo in z = 0
	for j in range(z0_halo_num, halos_count + 1):
		print(f'halo_{j} of halo_{halos_count} in z = 0')
		
		#trace thru all z for halo_j
		for i in range(len(halo.calculate_for_progenitors('z()')[0])-1):
			try:
				#print(f"calculate_for_progenitors('z()')[0]-1: {len(halo.calculate_for_progenitors('z()')[0])-1}")
				halo_num = halo.calculate('earlier('+str(i+1)+')').halo_number
				step_num = halo.calculate('earlier('+str(i+1)+')').timestep
				z = halo.calculate('earlier('+str(i+1)+')').calculate('z()')
				t = halo.calculate('earlier('+str(i+1)+')').calculate('t()')

				#print('%s %i %.2f %.2f %i %i\n' % (model, int(step_num.extension[-6:]), z, t, j, halo_num))
				with open(outfn, 'a') as outfile: 
					outfile.write('%s %i %.2f %.2f %i %i\n' % (model, int(step_num.extension[-6:]), z, t, j, halo_num))
			except: 
				break
		halo = sim.timesteps[-1].halos[j]  # j-1 since halos is 0 indexed but this is loading for next loop so j-1+1 = j
		