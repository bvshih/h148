import tangos as db
import parentHalo

sim_name = 'h148.cosmo50PLKvdXsec.6144.VTS'
sim = db.get_simulation(sim_name)
halos = sim.timesteps[-1].halos

# contamination cut
uncontaminated = [halo for halo in halos if halo['contamination_fraction']<0.01]

print(uncontaminated[1])
print(uncontaminated[2])


print(uncontaminated[1].calculate('parentHalo()'))
print(uncontaminated[2].calculate('parentHalo()'))
