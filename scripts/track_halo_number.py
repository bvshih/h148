import tangos as db 
import numpy as np 
import sys 
import os
import datetime

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

		now = datetime.datetime.now()
		print(f'[{now:%Y-%m-%d %H:%M:%S}] dat file exists at {outfn}', flush=True)

		outfile = open(outfn, 'r')
		lines = [line for line in outfile]
		outfile.close()
		
		#finds what the last entry in the file is 	
		if len(lines) == 1 :
			#file only has column names written
			#start at z = 0
			#start with first halo

			now = datetime.datetime.now()
			print(f'[{now:%Y-%m-%d %H:%M:%S}] dat file only has headers, starting with z = 0 and halo_1', flush=True)

			last_timestep_in_file = 0
			last_halo_in_file = 0
			last_z0_halo_in_file = 0
		else:
			last_line = lines[-1].split()

			last_timestep_in_file = last_line[1]
			last_halo_in_file = int(last_line[-1])
			last_z0_halo_in_file = int(last_line[-2])

			now = datetime.datetime.now()
			print(f'[{now:%Y-%m-%d %H:%M:%S}] dat file has entries, starting with halo_{last_halo_in_file} in timestep {last_timestep_in_file}', flush=True)

	#creates an outfile if one doesnt already exist
	else:
		now = datetime.datetime.now()
		print(f'[{now:%Y-%m-%d %H:%M:%S}] dat file does not exist, creating dat file and header at {outfn}', flush=True)

		last_timestep_in_file = 0
		last_halo_in_file = 0
		last_z0_halo_in_file = 0

		with open(outfn, 'a') as outfile:
			outfile.write('model output z time z0_halo_num halo_num\n')


	#load simulation and halos
	sim = db.get_simulation(sim_name)
	halos = sim.timesteps[-1].halos
	halos_count = halos.count()


	# if last_timestep_in_file == 0:	
	# 	#no entries in datfile 
	# 	halo = halos[0]
	# else:
	# 	#has entries in datfile
	# 	halo = halos[last_z0_halo_in_file]
	
	if last_timestep_in_file == 0:
		#datfile has no entries
		starting_halo = halos[0]
		starting_index = 0
	else:
		starting_halo = db.get_halo(f'{sim_name}/%{last_timestep_in_file}/halo_{last_halo_in_file-1}')

		all_z = halos[0].calculate_for_progenitors('t()')[0]
		starting_z = starting_halo.calculate('t()')
		starting_index = np.where(np.isclose(all_z, starting_z))[0][0]

	#run thru the halos array
	for halo in halos[last_z0_halo_in_file-1:]:
		now = datetime.datetime.now()
		print(f'[{now:%Y-%m-%d %H:%M:%S}] halo_{halo.halo_number} of halo_{halos_count} in z = 0', flush=True)
		
		#trace thru all z for halo
		for i in range(starting_index, len(all_z)):
			try:
				halo_num = halo.calculate('earlier('+str(i+1)+')').halo_number
				step_num = halo.calculate('earlier('+str(i+1)+')').timestep
				z = halo.calculate('earlier('+str(i+1)+')').calculate('z()')
				t = halo.calculate('earlier('+str(i+1)+')').calculate('t()')

				with open(outfn, 'a') as outfile: 
					outfile.write('%s %i %.2f %.2f %i %i\n' % (model, int(step_num.extension[-6:]), z, t, halo.halo_number, halo_num))
			except:
				break