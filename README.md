# NSF_CPS-SIRI-2022

This work is for research project at [*N*HanCE](https://engineering.purdue.edu/NHanCE) lab at Purdue University through the [NSF CPS Frontier: Cognitive Autonomy for Human CPS project](https://autonomy.unm.edu/index.html)

### Table of Content

1. [Files](#files)
2. [Instruction](#instruction)

---

## Files

1. `convert_daq_csv.m`: run on Matlab
2. `requirements.txt`: contain the version of Python libraries used in this project
3. `accum_csv.py`: merge all csv file into a big csv file that contains the whole dataset
---

## Instruction

### convert_daq_csv.m:
1. Run the `setpath_ndaqtools.m` in ndaqtools package (contact Professor Brandon Pitts at Purdue University for further information)
2. Type __"DaqViewer"__ in Matlab's Command Window (a window will pop up)
3. (optional) Click __"Create Cell List"__ to choose features you want to extract values, then save as `.mat` file
4. In __"Read DAQ Option"__, choose __"Read cell list"__ and choose `.mat` file that contains list of features
5. Click __"Read DAQ Vars"__
6. Run `convert_daq_csv.m` after editing file location
7. Result: each csv file contains it corresponding feature

### Setup:
1. Create an environment for this project. I suggest using [Anaconda](https://www.anaconda.com/). Run this command to create virtual env ([cheatsheet](https://anaconda.cloud/conda-cheatsheet)):
```
conda create --name env_name python=3.9.7
```
Then activate the env:
```
conda activate env_name
```

### requirements.txt:
1. Run this command to install the required libraries:
```
pip install -r requirements.txt
```
***Note***: This should be done before working on `*.py` files


### accum_csv.py:
1. Open terminal
2. Type the following command:
```
python accum_csv.py output_filename.csv
```
