#!/bin/bash
# ---------------------------------------------------
#SBATCH -J test_track_halos           # Job name
#SBATCH -o ./script_outs/outs/test_track_halos.o%j       # Name of stdout output file
#SBATCH -e ./script_outs/errors/test_track_halos.e%j       # Name of stderr error file
#SBATCH -p development          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes (must be 1 for serial)
#SBATCH -n 1               # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 00:30:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=bv.shih@gmail.com
#SBATCH --mail-type=all    # Send email at begin and end of job

# Other commands must follow all #SBATCH directives...

module list
pwd
date

# Launch serial code...

python ../scripts/run_track_all_halos.py    

# ---------------------------------------------------