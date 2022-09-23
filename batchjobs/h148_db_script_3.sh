#!/bin/bash
#----------------------------------------------------
#Generate merger trees for h148
#----------------------------------------------------
#SBATCH -J h148_db_3           # Job name
#SBATCH -o ./script_outs/outs/h148_db_3.o%j       # Name of stdout output file
#SBATCH -e ./script_outs/errors/h148_db_3.e%j       # Name of stderr error file
#SBATCH -p normal          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes (must be 1 for serial)
#SBATCH -n 1               # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 08:00:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=bshih0@uw.edu
#SBATCH --mail-type=all    # Send email at begin and end of job

# Other commands must follow all #SBATCH directives...

module list
pwd
date


# Launch serial code...

tangos link --for h148.cosmo50PLKvdXsec.6144.VTS
# ---------------------------------------------------
