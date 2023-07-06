"""
Run all experiments.
"""

import pathlib

import experiment1
import experiment2
import experiment3
import experiment4
import experiment5



if __name__=="__main__":
    dirpath = str(pathlib.Path(__file__).parent.resolve())
    print("Writing directory: \t", dirpath)

    print("\n\n\nExperiment 1\n")
    experiment1.experiment1(dirpath=dirpath)
    print("\n\n\nExperiment 2\n")
    experiment2.experiment2(dirpath=dirpath)
    print("\n\n\nExperiment 3\n")
    experiment3.experiment3(dirpath=dirpath)
    print("\n\n\nExperiment 4\n")
    experiment4.experiment4(dirpath=dirpath)
    print("\n\n\nExperiment 5\n")
    experiment5.experiment5(dirpath=dirpath)

