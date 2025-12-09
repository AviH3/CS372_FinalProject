#!/bin/bash 
#SBATCH -J batch_infer
#SBATCH -o ../slurm_oe/%x_%j-%a.out
#SBATCH -e ../slurm_oe/%x_%j-%a.err
#SBATCH -p youlab-gpu 
#SBATCH --exclusive
#SBATCH --mem=32G
#SBATCH --mail-type=ALL
source /hpc/group/youlab/rah94/miniconda3/etc/profile.d/conda.sh
conda activate pytorch_PA_patternprediction
cd /hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential
python batch_infer.py "$@"