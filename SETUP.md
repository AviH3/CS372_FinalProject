# Setup
## Download files
All data files can be found at this [Huggingface Library](https://huggingface.co/datasets/HotshotGoku/Simulation_templated_pattern_prediction). You will want to extract all of these files by going to the location you want the expanded files in and running the below for each file. Following this, reconfigure the relevant config files in data for the experimental and simulation training sets.
```
tar -xf /filename
```
## Setup environment
Run the below to properly set up the conda environment.
```
conda env create -f pytorch_PA_patternprediction.yml
```
## Data Augmentation
Ensure that all of the relevant files have been updated to reflect your library. This can be done by checking what gets imported from the config file at the top of Augmentation script in the Data folder. You might have to update the import since the utils file has been removed for the sake of clarity in this repo. None of the other utils files are used for these scripts. There is a slurm file in this folder as well. The source should be set to wherever the conda.sh file is located in a miniconda folder, and the directory should be to whatever folder the corresponding .py file is. 
## Adding ControlNet
Download the Stable Diffusion 1.5 [checkpoint](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5/blob/main/v1-5-pruned.ckpt), and then run the below code.
```
python tool_add_control.py v1-5-pruned.ckpt ./control_sd15_ini.ckpt
```
This will create the control_sd15_ini_ckpt that you will want to use to train the model.
## Training
Check the simtoexp_train and simtoexp_dataset files in the src folder, and ensure that whatever they are importing from relevant config file is updated to your directory. You may also have to change how the config file gets imported since cldm is no longer in the same folder as the python script. Run the either the ControlNet_simtoexp or ControlNet_simtoexp_parallel in the slurm scripts folder in the docs folder. The same considerations for updates to the slurm file should be taken as above.
## Inference
Check the pipeline folder to see which files should be updated in the config folder. Run the batch_inference slurm script similar to what was done above. This should create inference folders with predictions for each simulation and experiment in the testset.
## Evaluation
Run the below line to activate the conda environment.
```
conda activate pytorch_PA_patternprediction
```
Following this, in the notebooks folder, run the inference notebook. Take note of anything that needs to change in the config file. Also take into consideration that if the config file is changed, the jupyter kernel will need to be reset to run the inference for another model.
