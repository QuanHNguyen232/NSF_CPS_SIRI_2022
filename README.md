# NSF_CPS-SIRI-2022

This work is for research project at [*N*HanCE](https://engineering.purdue.edu/NHanCE) lab at Purdue University through the [NSF CPS Frontier: Cognitive Autonomy for Human CPS project](https://autonomy.unm.edu/index.html)

### Table of Content

1. [Files](#files)
2. [Instruction](#instruction)

---

## Files

1. `convert_daq_csv.m`: run on Matlab

---

## Instruction

1. Run the `setpath_ndaqtools.m` in ndaqtools package (contact Professor Brandon Pitts at Purdue University for further information)
2. Type __"DaqViewer"__ in Matlab's Command Window (a window will pop up)
4. (optional) Click __"Create Cell List"__ to choose features you want to extract values, then save as `.mat` file
5. In __"Read DAQ Option"__, choose __"Read cell list"__ and choose `.mat` file that contains list of features
6. Click __"Read DAQ Vars"__
7. Run `convert_daq_csv.m` after editing file location
