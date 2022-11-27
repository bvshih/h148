#!/bin/bash
# ---------------------------------------------------
#SBATCH -J track_halos           # Job name
#SBATCH -o ./script_outs/track_halos/%j.o        # Name of stdout output file
#SBATCH -e ./script_outs/track_halos/%j.e       # Name of stderr error file
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

# Launch serial code...

python ../scripts/run_track_all_halos.py    

# ---------------------------------------------------