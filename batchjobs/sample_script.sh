#!/bin/bash
# ---------------------------------------------------
#SBATCH -J myjob           # Job name
#SBATCH -o ./script_outs/outs/myjob.o%j       # Name of stdout output file
#SBATCH -e ./script_outs/errors/myjob.e%j       # Name of stderr error file
#SBATCH -p normal          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes (must be 1 for serial)
#SBATCH -n 1               # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 01:30:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=bshih0@uw.edu
#SBATCH --mail-type=all    # Send email at begin and end of job
# ---------------------------------------------------
# Other commands must follow all #SBATCH directives...

module list
pwd
date

# Launch serial code...

./myprogram         # Do not use ibrun or any other MPI launcher

# ---------------------------------------------------