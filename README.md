# daas_py_common
## Project

Refrence of DaaS Project - https://github.com/nealrout/daas_docs

## Description
Project to hold common components that will be used by other projects.  

## Table of Contents
- [Requirements](#requirements)
- [Install-Uninstall](#install-uninstall)
- [Usage](#usage)
- [Features](#features)
- [Miscellaneous](#miscellaneous)
- [Contact](#contact)

## Requirements


## Install-Uninstall
__Install:__  
python -m pip install daas_py_common

__Uninstall:__  
python -m pip uninstall daas_py_common

__Rebuild from source:__  
python -m pip install --no-binary :all: .

## Usage
from daas_py_common.logging_config import logger

## Package
python -m build daas_py_common

## Features
- Logging module added and configured using built in Python logging library

## Miscellaneous
No additional modules are needed currently.  We are only using the built in logging module.

## Contact
Neal Routson  
nroutson@gmail.com
