import track_halo_number

sim_name = 'h148.cosmo50PLKvdXsec.6144.VTS'
model = 'h148vdXsec'
ini_stepnum = 4096
ini_halo_num = 2

track_halo_number.new_halo_num_tracker(model, sim_name, ini_stepnum, ini_halo_num)
