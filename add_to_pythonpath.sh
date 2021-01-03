#! /bin/bash

# Adds the current working directory to the ~/.bash_profile and
# ~/.bashrc files. Needed in order for the plot modules to be
# accessible to python scripts.

PROFILE=${HOME}/.bash_profile
RC=${HOME}/.bashrc
PWD=$(pwd)

echo 'PYTHONPATH='"$PWD"':$PYTHONPATH' >> $PROFILE
echo 'PYTHONPATH='"$PWD"':$PYTHONPATH' >> $RC
