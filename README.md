# NSF-CPS-SIRI-2022

This work is for research project at [*N*HanCE](https://engineering.purdue.edu/NHanCE) lab at Purdue University through the [NSF CPS Frontier: Cognitive Autonomy for Human CPS](https://autonomy.unm.edu/index.html) project.

**TODO:** 
- [ ] Get data from Fixation data

### Table of Content

1. [Files](#files)
2. [Instruction](#instruction)

---

## Files
<!-- https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/tree:
type: tree /f
 -->
File structure:
```
.
│   .gitignore
│   7-11-feat_list.mat
│   feat_suggest.txt
│   README.md
│   requirements.txt
│   
├───Data-Processing
│   │   check-missing.py
│   │   ERROR-data.txt
│   │   
│   ├───daq-data-process
│   │       accum_feat_v2.1.py
│   │       convert_daq_txt-csv.m
│   │       getObsvWindow.py
│   │       Obstacle_Finder.py
│   │
│   └───eye-track-data-process
│           convert-eyetracking-txt.py
│           convert-miniSim-txt.py
│           get_Fixation_wind.py
│           match_eye_trk.py
│           miniSim-to-txt.py
│
└───Models
    │   Kmeans.py
    │   MyDataLoader.py
    │   RF.py
    │   Utils.py
```

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
<details>
<summary markdown="span">Click to expand</summary>

1. Create an environment for this project. I suggest using [Anaconda](https://www.anaconda.com/). Run this command to create virtual env ([cheatsheet](https://anaconda.cloud/conda-cheatsheet)):
```
conda create --name env_name python=3.9.7
```
Then activate the env:
```
conda activate env_name
```

</details>

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


<p align="right"><a href="#nsf-cps-siri-2022">[Back to top]</a></p>
