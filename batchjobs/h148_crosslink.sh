#!/bin/bash
#----------------------------------------------------
#Crosslinks SIDM and CDM+Baryons runs
#----------------------------------------------------
#SBATCH -J crosslink           # Job name
#SBATCH -o ./script_outs/h148_db/crosslink/%j.o       # Name of stdout output file
#SBATCH -e ./script_outs/h148_db/crosslink/%j.e       # Name of stderr error file
#SBATCH -p normal          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes (must be 1 for serial)
#SBATCH -n 1               # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 24:00:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=bv.shih@gmail.com
#SBATCH --mail-type=all    # Send email at begin and end of job

# Other commands must follow all #SBATCH directives...

module list
pwd
date

echo $TANGOS_SIMULATION_FOLDER
echo $TANGOS_DB_CONNECTION

# Launch serial code...

tangos crosslink h148.cosmo50PLK.6144g3HbwK1BH h148.cosmo50PLKvdXsec.6144.VTS --backwards
# ---------------------------------------------------