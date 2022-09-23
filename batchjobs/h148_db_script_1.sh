#!/bin/bash
#----------------------------------------------------
#Adds h148 sim to tangos
#----------------------------------------------------
#SBATCH -J h148_db_1           # Job name
#SBATCH -o ./script_outs/outs/h148_db_1.o%j       # Name of stdout output file
#SBATCH -e ./script_outs/errors/h148_db_1.e%j       # Name of stderr error file
#SBATCH -p normal          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes (must be 1 for serial)
#SBATCH -n 1               # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 10:00:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=bshih0@uw.edu
#SBATCH --mail-type=all    # Send email at begin and end of job

# Other commands must follow all #SBATCH directives...

module list
pwd
date

echo $TANGOS_SIMULATION_FOLDER
echo $TANGOS_DB_CONNECTION

# Launch serial code...

tangos add h148.cosmo50PLKvdXsec.6144.VTS
# ---------------------------------------------------