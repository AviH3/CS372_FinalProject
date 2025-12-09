#!/bin/bash 
#SBATCH -o /hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/slurm_oe/slurm_CMMD_20251011.out
#SBATCH -e /hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/slurm_oe/slurm_CMMD_20251011.err
#SBATCH -p youlab-gpu
#SBATCH --exclusive
#SBATCH --mem=24G
#SBATCH --mail-type=ALL
source /hpc/group/youlab/rah94/miniconda3/etc/profile.d/conda.sh
conda activate pytorch_PA_patternprediction
cd /hpc/dctrl/ks723/cmmd
# Folder pairs
declare -A comparisons
comparisons["exp_vs_sim"]=" /hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Exp_testset /hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/SimcorrtoExp_testset"
comparisons["exp_vs_pred"]="/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Exp_testset /hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v2025128_217_SIMTOEXP_g4"
comparisons["sim_vs_pred"]="/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/SimcorrtoExp_testset /hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v2025128_217_SIMTOEXP_g4"
# comparisons["exp_test_vs_exp_train"]=" /hpc/group/youlab/ks723/storage/Processed_testsets/exp /hpc/group/youlab/ks723/storage/Exp_images/Final_folder_uniform_fixedseed_preprocess_png/"



# Loop and run
for label in "${!comparisons[@]}"; do
    read dir1 dir2 <<< "${comparisons[$label]}"
    echo "Running $label: $dir1 vs $dir2"
    cmmd_output=$(python main.py "$dir1" "$dir2" --batch_size=1)
    echo "CMMD ($label) = $cmmd_output"
done

