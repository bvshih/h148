#!/bin/bash
#----------------------------------------------------
#writes parentHalo to tangos
#----------------------------------------------------
#SBATCH -J parentHalo                               # Job name
#SBATCH -o /scratch/08263/tg875625/h148/batchjobs/script_outs/h148_db/parentHalo/%j.o     # Name of stdout output file
#SBATCH -e /scratch/08263/tg875625/h148/batchjobs/script_outs/h148_db/parentHalo/%j.e     # Name of stderr error file
#SBATCH -p development                                   # Queue (partition) name
#SBATCH -N 1                                        # Total # of nodes (must be 1 for serial)
#SBATCH -n 1                                        # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 01:00:00                                 # Run time (hh:mm:ss)
#SBATCH --mail-user=bv.shih@gmail.com
#SBATCH --mail-type=all                             # Send email at begin and end of job

# Other commands must follow all #SBATCH directives...

module list
pwd
date

echo $PYTHONPATH
echo $TANGOS_PROPERTY_MODULES
# Launch serial code...

tangos write parentHalo --with-prerequisites --include-only="contamination_fraction<0.01" --for h148.cosmo50PLKvdXsec.6144.VTS --backwards
# ---------------------------------------------------