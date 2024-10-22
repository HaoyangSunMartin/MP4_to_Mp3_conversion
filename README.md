# Example Python Project

## Purpose

This repository is designed as a simple tool to extract .mp3 from .mp4 files.

Please feel free to Fork or Download this repository for your own usage.
A graphical for drag and drop interface might be developed in the future.
Feel free to fork this project and contribute.

## Dependencies
first set up a conda environment with python>=3.9 and moviepy package:

`conda install -c conda-forge moviepy`

## Instructions

run the command line for further instructions:

`python main.py --help`

## Potential Issues and Fixes

if you get the error similar to:

`cannot import name 'volumex' from 'moviepy.video.fx`

please refer to this page[MoviePyFix] for help by changing the __init__.py file of the moviepy:

[1]: https://github.com/Zulko/moviepy/issues/591           "MoviePyFix"

