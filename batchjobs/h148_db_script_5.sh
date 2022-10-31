#!/bin/bash
#----------------------------------------------------
#More properties for h148 run in parallel 
#----------------------------------------------------
#SBATCH -J h148_db_5                                # Job name
#SBATCH -o ./script_outs/h148_db/h148_db_5.o%j         # Name of stdout output file
#SBATCH -e ./script_outs/h148_db/h148_db_5.e%j       # Name of stderr error file
#SBATCH -p skx-normal                                 # Queue (partition) name
#SBATCH -N 1                                        # Total # of nodes 
#SBATCH -n 32                                        # Total # of mpi tasks 
#SBATCH -t 48:00:00                                 # Run time (hh:mm:ss)
#SBATCH --mail-user=bv.shih@gmail.com
#SBATCH --mail-type=all                             # Send email at begin and end of job

# Other commands must follow all #SBATCH directives...

module list
pwd
date
echo 'N = 1, n = 32'

# Launch MPI code...

ibrun tangos write dm_density_profile --with-prerequisites --include-only="contamination_fraction<0.01" --for h148.cosmo50PLKvdXsec.6144.VTS --load-mode=server --backend mpi4py --backwards 

# ---------------------------------------------------