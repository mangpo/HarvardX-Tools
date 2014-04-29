#!/bin/tcsh

# Set up separate directories for each class
# Move files to those directories
# Rename to something shorter and more uniform
# Create a .csv file from each of the sql files
buildClassList.py
separateClassFiles.py

