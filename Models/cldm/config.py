import matplotlib as mpl
from pathlib import Path
from datetime import datetime   

currentMinute = datetime.now().minute
currentHour   = datetime.now().hour
currentDay    = datetime.now().day
currentMonth  = datetime.now().month
currentYear   = datetime.now().year


#########
# Font for plots
FPATH = Path(mpl.get_data_path(), "/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/ARIAL.TTF")
#########

# For creating prompt.json files 
BASE_FOLDER= '/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar'
SPECIFIC_FOLDER_SIM='/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/SimcorrtoExp_AUG100_DUP2' # Extract SimcorrtoExp.tar, run the augmentation script and use those images here
SPECIFIC_FOLDER_EXP='/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Exp_AUG100_DUP2' # Extract Exp.tar, run the augmentation script and use those images here
SPECIFIC_FOLDER_SEED='/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/specific_seed_aug' # Extract Exp_SimcorrtoExp_seed.tar, run Seed_DataAugmentation.py script and use those images here

# For Sim to Exp dataset, model training
EXP_FOLDER_TRAIN_NONAUG='/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Exp'  # Exp.tar

# For Seed to Exp dataset, model training

SEED_FOLDER_TRAIN_NONAUG="/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Exp_SimcorrtoExp_seed"  # Exp_SimcorrtoExp_seed.tar

# For running model inference # test images folder, v3 is the folder with 96 images- same number of images in experiment and simulation folders, used in the final analysis
SIM_FOLDER_TEST   = "/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/SimcorrtoExp_testset/"  # SimcorrtoExp_testset.tar
SEED_FOLDER_TEST  = "/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Exp_SimcorrtoExp_testset_seed/"  # Exp_SimcorrtoExp_testset_seed.tar
EXP_FOLDER_TEST   = "/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Exp_testset/"  # Exp_testset.tar


# Creation of different folders that will be later used for inference outputs
OUTPUT_DIR_SEEDTOEXP = f"/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v{currentYear}{currentMonth}{currentDay}_{currentHour}{currentMinute}_SEEDTOEXP"
OUTPUT_DIR_SIMTOEXP = f"/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v{currentYear}{currentMonth}{currentDay}_{currentHour}{currentMinute}_SIMTOEXP"

OUTPUT_DIR_RANDOMSEEDSWEEP = f"/hpc/dctrl/ks723/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v{currentYear}{currentMonth}{currentDay}_{currentHour}{currentMinute}_random_seed_sweep/"
OUTPUT_DIR_ABLATION_BASE= f"/hpc/dctrl/ks723/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v{currentYear}{currentMonth}{currentDay}"
OUTPUT_DIR_CONTRASTIVE_LEARNING=f"/hpc/dctrl/ks723/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/contrastive_learning_v{currentYear}{currentMonth}{currentDay}_{currentHour}{currentMinute}/"

# For ablation study 

MAIN_FOLDER= '/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v2025125_226_SIMTOEXP_lr2'   # default ControlNet, OUTPUT_DIR_SIMTOEXP
ABLATION_1=  '/hpc/dctrl/ks723/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v20251023_1458_no_guess/'  # Guess_mode= TRUE , Run ablation script and modify the part accordingly
ABLATION_2=  '/hpc/dctrl/ks723/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v20251023_1753_no_negative' # n_prompt=""
ABLATION_3=  '/hpc/dctrl/ks723/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v20251023_1756_plus_positive' # a_prompt="best quality, extremely detailed" # default ControlNet
ABLATION_4=  '/hpc/dctrl/ks723/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v20251023_1758_low_strength_point85' # strength=0.85
ABLATION_5=  '/hpc/dctrl/ks723/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v20251023_1758_high_strength_1point25' # strength=1.25
ABLATION_6=  '/hpc/dctrl/ks723/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v20251023_1759_higher_DDIM_steps_100'  # ddim_steps=100
ABLATION_7=  '/hpc/dctrl/ks723/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v20251023_181_lower_guidance_9point0'  # guidance_scale=9.0 # default ControlNet


# For plotting Fig 5 (SUPP FIG 15)
PRED_FOLDER_SEEDTOEXP = '/hpc/dctrl/ks723/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/inference/v20251011_841_seedtoexp_swapped_v3'  # OUTPUT_DIR_SEEDTOEXP

# Checkpoint path for inference 

CKPT_PATH='/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/sim_to_exp_diffusion/controlnet_essential/lightning_logs/version_40380828/checkpoints/epoch=4-step=51124.ckpt'   # checkpoint_simtoexp.tar
CKPT_PATH_SEEDTOEXP="/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/checkpoint_seedtoexp/epoch=4-step=51124.ckpt" # checkpoint_seedtoexp.tar








