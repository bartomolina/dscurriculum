# Environment Setup
## Setup
- Install Anaconda
- Install Git
  - git config --global user.name "FIRST_NAME LAST_NAME"
  - git config --global user.email "MY_NAME@example.com"
- Clone environment repository:`git clone https://github.com/learn-co-curriculum/dsc-1-01-05-setting-up-environment`
- Create environment
  - Mac: `conda env create -f environment.yml`
  - Windows: `conda env create -f windows.yml`
- Activate environment
  - `source activate learn-env` (Mac / Git bash)
  - `activate learn-env` (Windows shell)
- Verify: `conda info --envs`
## Activate kernel
- `source activate learn-env` (`activate learn-env` in Windows shell)
- Verify: `conda list -f obscure` should show you that you have v1.0.1 of the "obscure" package
- Add kernel: `python -m ipykernel install --user --name=learn-env`
- Start Jupyter notebook: `jupyter notebook`
## Update environment
- `source activate base # To make sure you're not in the learn-env environment`
- `conda remove -n learn-env --all # To get rid of the enviroment`
- `conda env list # Make sure it doesn't list learn-env - if it does, try the last step again`
- Then recreate the environment
  - Mac: `conda env create -f environment.yml`
  - Windows: `conda env create -f windows.yml`
## Update / Install conda / packages
- `conda update --all` / `conda update -n base conda`
- `pip3 install pandas`
- `pip3 install matplotlib`
- `pip install xlrd`
- `pip install scipy`
- `pip install sqlalchemy`
- `pip install seaborn`
- `pip install tqdm`
- `pip install statsmodels`
- `pip install sklearn`
- `conda install shapely`
- `pip install cartoframes`
- `pip install -U python-dotenv`
## Jupyter Notebook Extensions
https://ndres.me/post/best-jupyter-notebook-extensions/
- `pip install jupyter_contrib_nbextensions`
- `jupyter contrib nbextension install --user`
  - Collapsible Headings
  - Codefolding / Codefolding in editor
  - Scratchpad
  - Variable inspector
  - ExecuteTime
  - Freeze