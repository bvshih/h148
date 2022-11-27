import pandas as pd
import pynbody
import datetime
import numpy as np

outfn = '../datfiles/halos_keys.dat'

s = pynbody.load('/scratch/06040/adcruz/SIMS/sandraSI/h148.cosmo50PLKvdXsec.6144.VTS/h148.cosmo50PLKvdXsec.6144.VTS.004096')

now = datetime.datetime.now()
print(f'[{now:%Y-%m-%d %H:%M:%S}] loaded in simulation', flush=True)

s.physical_units()

now = datetime.datetime.now()
print(f'[{now:%Y-%m-%d %H:%M:%S}] changed to physical units', flush=True)

h = s.halos()

now = datetime.datetime.now()
print(f'[{now:%Y-%m-%d %H:%M:%S}] loaded in halos', flush=True)

h1 = h[1]

now = datetime.datetime.now()
print(f'[{now:%Y-%m-%d %H:%M:%S}] centered on h1', flush=True)

keys = h1.all_keys()

properties = h1.properties

with open(outfn, 'w') as outfile:
	joined_keys = ', '.join(keys)
	outfile.write(joined_keys)

	joined_properties = ', '.join(properties)
	outfile.write(joined_properties)






