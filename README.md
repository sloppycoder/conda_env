# use conda env

## create 2 env for 2 projects

create 2 directories for 2 different python projects with different dependencies. create a conda env for each project to manage dependecies. conda environments are under $CONDA_PREFIX directory, not inside your code directory.

```shell

mkdir proj1
cd proj1

# create env for proj1
conda create -n proj1 python=3.8
conda activate proj1

# install packages using conda, not pip
conda install numpy

# create test.py file and run

# export environment to an envrionment file
conda env export --from-history > proj1_conda_env.yml
conda deactivate

cd ..
mkdir proj2
cd proj2

conda create -n proj2 python=3.11
conda activate proj2
conda install python-dotenv

# create test.py file and run

# export environment to an envrionment file
conda env export --from-history > proj2_conda_env.yml
conda deactivate

# check environments created
conda env list

```

## re-create envs on another machine

```shell

# install conda or miniconda
# clone this repo

cd proj1

# re-create env proj1 from environment file
conda env create -f proj1_conda_env.yml

conda activate proj1
python test.py
conda deactivate

cd ../proj2

# re-create env proj2 from environment file
conda env create -f proj2_conda_env.yml

conda activate proj2
python test.py
conda deactivate

# check environments created
conda env list

```

See [conda documentations](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment) for more details
