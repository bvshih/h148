import pandas as pd
import pynbody
import datetime
import numpy as np

def calc_distance(x1,y1,z1,x2,y2,z2):
    return np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)


df = pd.read_csv('/scratch/06040/adcruz/SIMS/sandraSI/h148.cosmo50PLKvdXsec.6144.VTS/h148.cosmo50PLKvdXsec.6144.VTS.004096.z0.000.AHF_halos', sep='\s+')

now = datetime.datetime.now()
print(f'[{now:%Y-%m-%d %H:%M:%S}] read in AHF_halos')

s = pynbody.load('/scratch/06040/adcruz/SIMS/sandraSI/h148.cosmo50PLKvdXsec.6144.VTS/h148.cosmo50PLKvdXsec.6144.VTS.004096')

now = datetime.datetime.now()
print(f'[{now:%Y-%m-%d %H:%M:%S}] loaded in simulation')

s.physical_units()

now = datetime.datetime.now()
print(f'[{now:%Y-%m-%d %H:%M:%S}] changed to physical units')

h_factor = s.properties['h']

h = s.halos()

now = datetime.datetime.now()
print(f'[{now:%Y-%m-%d %H:%M:%S}] loaded in halos')

# -------------------------------------------------------------------------------------
# pot: potential minimum
# com: center of mass
# ssc: shrink sphere center
# ind: center on specific particles; supply the list of particles using the ind keyword.    
# hyb: for sane halos, returns the same as ssc, but works faster by
#     starting iteration near potential minimum
# -------------------------------------------------------------------------------------

AHF_list = []
com_list = []
ssc_list = []

for i in range(4):
    print(f'[{now:%Y-%m-%d %H:%M:%S}] calculating for h{i+1}')
    
    AHF = [df['Xc(6)'][i],df['Yc(7)'][i], df['Zc(8)'][i]]
    AHF_list.append(AHF)
    
    com = pynbody.analysis.halo.center_of_mass(h[i+1])
    com_list.append(com)
    now = datetime.datetime.now()
    print(f'[{now:%Y-%m-%d %H:%M:%S}] com calculated')


    ssc = pynbody.analysis.halo.shrink_sphere_center(h[i+1])
    ssc_list.append(ssc)
    now = datetime.datetime.now()
    print(f'[{now:%Y-%m-%d %H:%M:%S}] ssc calculated')

# -------------------------------------------------------------------------------------

print('\n')

# for i in range(1,4):
#     print(f'h{i+1}: ')
#     print(AHF_list[i])
#     print(com_list[i])
#     print(ssc_list[i])
#     print('\n')
# -------------------------------------------------------------------------------------

print('distances:')

for i in range(1,4):

    dist = [calc_distance(*AHF_list[0], *AHF_list[i]), calc_distance(*com_list[0], *com_list[i]), calc_distance(*ssc_list[0], *ssc_list[i])]
    print(f'h1 and h{i+1}')
    print('\t\tAHF: ', dist[0])
    print('\t\tCOM: ', dist[1])
    print('\t\tSSC: ', dist[2])
    print('\tadjusted with h:')
    print('\t\tAHF: ', dist[0])
    print('\t\tCOM: ', dist[1]*h_factor)
    print('\t\tSSC: ', dist[2]*h_factor)


print(f'h: {h_factor:.16f}')