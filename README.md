# NSF_CPS-SIRI-2022

This work is for research project at [*N*HanCE](https://engineering.purdue.edu/NHanCE) lab at Purdue University through the [NSF CPS Frontier: Cognitive Autonomy for Human CPS project](https://autonomy.unm.edu/index.html)

**TODO:** 
- [x] merge-miniSim: will be removed
- [x] update `match_eye_trk.py`
- [ ] remove all columns that have 1 value (e.g.: all 0)
- [ ] merge daq w/ miniSim: miniSim get index of first and last window frame

### Table of Content

1. [Files](#files)
2. [Instruction](#instruction)

---

## Files

1. `convert_daq_csv.m`: convert daq features into csv files - each feature results in 1 one csv file (Matlab) -- do not use this.
2. `convert_daq_txt.m`: convert daq features into txt files - each feature results in 1 one txt file (Matlab).
3. `requirements.txt`: contain the version of Python libraries used in this project.
4. `accum_csv.py`: merge all csv file into a big csv file that contains the whole dataset.
5. `miniSim-to-txt.py`: convert .miniSim file to .txt file.
6. `merge-miniSim.py`: merge dataset from daq with .miniSim data based on `frame`.
7. `convert-miniSim-txt.py` and `convert-eyetracking-txt.py`: create the same `merge` column to easily merge miniSim and eyetracking data together.
---

## Instruction

#### Follow this order:
1. Run `convert_daq_csv.m`
2. Setup environment
3. Install libraries using `requirements.txt`
4. Run `accum_feat.py`
5. Run `miniSim-to-txt.py`
6. Run `merge-miniSim.py`


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


### accum_feat.py:
1. Open terminal
2. Type the following command:
```
python accum_csv.py output_filename.csv
```
Or extension of feature data files: txt/csv (result from `convert_daq_txt.m`)
```
python accum_csv.py filename.txt -x extension
```

### miniSim-to-txt.py;

### merge-miniSim.py
1. Type this command:
```
python read-miniSim.py out_name file_1 file_2 merge_on
```
*With*:
* file_1 = 'accum-data.txt'
* file_2 = 'P13-miniSim.txt'
* merge_on = 'Frames0'
