from datetime import datetime
from pathlib import Path
import matplotlib as mpl

currentDay = datetime.now().day
currentMonth = datetime.now().month


###############
# File creation of latents, will refer to the generated files in the later part of the code
###############

LATENT_OUTPUT_FILE=f'latent_dim_75000_4channels_4x32x32_gray_intermediate{currentMonth}{currentDay}.pickle'
LATENT_OUTPUT= f'/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Latent_Outputs/{LATENT_OUTPUT_FILE}'

LATENT_OUTPUT_TDB_FILE=f'latent_dim_75000_4channels_4x32x32_gray_complex{currentMonth}{currentDay}.pickle'
LATENT_OUTPUT_TDB= f'/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Latent_Outputs/{LATENT_OUTPUT_TDB_FILE}'

LATENT_OUTPUT_EXP_FILE=f'latent_dim_40900_4channels_4x32x32_gray_exp{currentMonth}{currentDay}.pickle'
LATENT_OUTPUT_EXP= f'/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Latent_Outputs/{LATENT_OUTPUT_EXP_FILE}'

LATENT_OUTPUT_SIMCORRTOEXP_FILE=f'latent_dim_40900_4channels_4x32x32_gray_simcorrtoexp{currentMonth}{currentDay}.pickle'
LATENT_OUTPUT_SIMCORRTOEXP= f'/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Latent_Outputs/{LATENT_OUTPUT_SIMCORRTOEXP_FILE}'

MODEL_SAVE_LOCATION='/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/saved_models'
LOGS_SAVE_LOCATION= '/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Saved_models/logs'


#########
# Font for plots

FPATH = Path(mpl.get_data_path(), "/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/ARIAL.TTF")
#########

################
#  FIG 1
################
# Define folder paths for input seeds, experimental, and simulated images
SEED_FOLDER = "/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Exp_SimcorrtoExp_seed" # Exp_SimcorrtoExp_seed.tar
EXPERIMENTAL_FOLDER = "/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Exp" # Exp.tar
SIMULATED_FOLDER = "/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/SimcorrtoExp" # Sim_corrtoexp.tar

# Selected files for display of simulation and Experimental data, Fig 1a and 1b
FILES_FIG1A= ['Fixed_19_6.TIF','Fixed_15_3.TIF','Fixed_25_4.TIF','Fixed_6_1.TIF','Fixed_26_3.TIF']
FILES_FIG1B= ['5_2.TIF','Fixed_14_2.TIF', 'Fixed_29_3.TIF', 'Fixed_15_2.TIF','Fixed_22_1.TIF']
# number of seeds     1         2                   4               6                   8

#################
#  FIG 2
#################
# Define folder paths for TEST SET simulated images

# note these 2 folders also serve as input and output for model training, for testing we use different files in these folders
SIMULATION_TEST_OUTPUT_FOLDER_2='/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Sim_050924_intermediate_Tp3' # Sim_050924_intermediate_Tp3.tar
SIMULATION_TEST_INPUT_FOLDER_2="/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Sim_050924_seed" # Sim_050924_seed.tar

SIMULATION_TEST_OUTPUT_FOLDER='/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Sim_050924_ModelTesting_intermediate_Tp3' # Sim_050924_ModelTesting_intermediate_Tp3.tar
SIMULATION_TEST_INPUT_FOLDER="/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Sim_050924_ModelTesting_seed" # Sim_050924_ModelTesting_seed.tar

# make simulation patterns output to latent dimension for training
# note: Generate the latents first and save accordingly 

LATENT_OUTPUT_FILE_SAVED= 'latent_dim_75000_4channels_4x32x32_gray_intermediate1120.pickle' 
LATENT_OUTPUT_SAVED=f'/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Latent_Outputs/{LATENT_OUTPUT_FILE_SAVED}'
    
# Model save path
MODEL_DILRESNET_FIG2_FILE='Pixel_32x32x3to32x32x4_dilRESNET_30k_graypatterns_seedtointermediate_v101_4-1759366230_best.pt' # note no .pt extension
MODEL_DILRESNET_FIG2=f'{MODEL_SAVE_LOCATION}/{MODEL_DILRESNET_FIG2_FILE}'

# Json list of SEED COUNTS in each branching pattern
JSON_FILE_SEEDS_SUPPFIG8='/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Sim_050924_seed_counts_testset_60000_70000.json' # Sim_050924_seed_counts_testset_60000_70000.json



#################
#  FIG 3
#################

# Define folder for thiner, denser branches: this serves as model output now, simulation_test_folder_2 serves input

SIMULATION_TEST_OUTPUT_FOLDER_TDB= '/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/Sim_050924_ModelTesting_complex_Tp3' # Sim_050924_ModelTesting_complex_Tp3.tar
SIMULATION_TEST_OUTPUT_FOLDER_TDB_2= '/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/sim_050924_complex_Tp3' # Sim_050924_complex_Tp3.tar

MODEL_DILRESNET_FIG3_FILE= 'Pixel_32x32x3to32x32x4_dilRESNET_graypatterns_intermediatetocomplex_Model_30000_v101_Cluster_GPU_tfData-1759363890_best.pt' # note no .pt extension
#'Pixel_32x32x3to32x32x4_dilRESNET_newpatterns_intermediatetocomplex_Model_v930_Cluster_GPU_tfData-1759271090' 
#"Pixel_32x32x3to32x32x4_dilRESNET_newpatterns_intermediatetocomplex_Model_v1119_Cluster_GPU_tfData-1732077621"
MODEL_DILRESNET_FIG3=f'/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/relavent_tar/saved_models/Pixel_32x32x3to32x32x4_dilRESNET_graypatterns_intermediatetocomplex_Model_30000_v101_Cluster_GPU_tfData-1759363890_best.pt'

LATENT_OUTPUT_TDB_FILE_SAVED= 'latent_dim_75000_4channels_4x32x32_gray_complex1121.pickle' 
LATENT_OUTPUT_TDB_SAVED=f'/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Latent_Outputs/{LATENT_OUTPUT_TDB_FILE_SAVED}'


##############
# Supplementary FIG S13
##############

# Define folder paths for exps and simulation corresponding to these exps

EXPERIMENTAL_TRAIN_OUTPUT_FOLDER= "/hpc/group/youlab/ks723/storage/Exp_images/Final_folder_uniform_fixedseed_100AUG" # Run Augmentation_ExpandSim.py on Exp.tar and SimcorrtoExp.tar, use Exp folder here
SIMULATION_CORRTOEXP_TRAIN_OUTPUT_FOLDER="/hpc/group/youlab/ks723/storage/MATLAB_SIMS/Sim_031524/Selected_v4_ALL_100AUG" # Run Augmentation_ExpandSim.py on Exp.tar and SimcorrtoExp.tar, use SimcorrtoExp folder here

# Sorting done by a specific manner to avoid data leakage from augmentation in training/validation splits
SORTED_FILENAMES_PATH = '/hpc/group/youlab/ks723/miniconda3/Lingchong/sorted_files_full.txt'   # sorted_files_full.txt

LATENT_OUTPUT_SIMULATION_CORRTOEXP_FILE_SAVED='latent_dim_40900_4channels_4x32x32_gray_simcorrtoexp926.pickle'
LATENT_OUTPUT_SIMULATION_CORRTOEXP_SAVED=f'/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Latent_Outputs/{LATENT_OUTPUT_SIMULATION_CORRTOEXP_FILE_SAVED}'

LATENT_OUTPUT_EXPERIMENT_FILE_SAVED='latent_dim_40900_4channels_4x32x32_gray_exp926.pickle'
LATENT_OUTPUT_EXPERIMENT_SAVED=f'/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Latent_Outputs/{LATENT_OUTPUT_EXPERIMENT_FILE_SAVED}'

MODEL_DILRESNET_SUPPFIG13_FILE='Pixel_32x32x4to32x32x4_dilRESNET_BnW_30k_SimtoExp_Model_30000_v1023_1-1761239974_best_tolerant.pt'
MODEL_DILRESNET_SUPPFIG13= f'{MODEL_SAVE_LOCATION}/{MODEL_DILRESNET_SUPPFIG13_FILE}'

#################
#  FIG 4
#################

# data augmentation 
SIMULATION_AUGMENTATION_BASE='/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Aug_output/Sim/def' # Run DataDemand_augmentation.py, this folder is corresponding to default patterns
SIMULATION_AUGMENTATION_BASE_TDB='/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Aug_output/Sim/TDB' # Run DataDemand_augmentation.py, this folder is corresponding to TDB patterns
LATENT_OUTPUT_BASE= '/hpc/group/youlab/rah94/one_species/Physics_constrained_DL_pattern_prediction/seed_to_sim1_sim2_deterministic/Latent_Outputs'






