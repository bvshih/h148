#!/bin/bash
#----------------------------------------------------
#SBATCH -J h148_db_test                                # Job name
#SBATCH -o ./script_outs/outs/h148_db_test.o%j         # Name of stdout output file
#SBATCH -e ./script_outs/errors/h148_db_test.e%j       # Name of stderr error file
#SBATCH -p normal                                 # Queue (partition) name
#SBATCH -N 1                                        # Total # of nodes 
#SBATCH -n 32                                        # Total # of mpi tasks 
#SBATCH -t 02:00:00                                 # Run time (hh:mm:ss)
#SBATCH --mail-user=bshih0@uw.edu
#SBATCH --mail-type=all                             # Send email at begin and end of job

# Other commands must follow all #SBATCH directives...

module list
pwd
date
echo 'normal partition'
echo 'N = 1, n = 32'

# Launch MPI code...

ibrun tangos write dm_density_profile --with-prerequisites --include-only="contamination_fraction<0.01" --for h148.cosmo50PLKvdXsec.6144.VTS --load-mode=server --backend mpi4py --backwards 

# ---------------------------------------------------