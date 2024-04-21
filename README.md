**Python version: 3.12**
[A guide to install python3.12 on Linux](https://medium.com/@donfiealex/getting-python-3-12-up-and-running-on-ubuntu-and-debian-servers-cbe557d7d368)

**How to setup a virtual environment**:
```console
// create a virtual environment under a folder named 'venv'
$ python3.12 -m venv venv 
// activate the venv (command for Linux, Windows' command for activation might differ)
$ source ./venv/bin/activate 
``` 

**Required packages installation**: `pip3.12 install -r requirements.txt`

**How to run**: `python3.12 src/Game.py`

**Helpful info**: 
- python3.12 venv (if not installed): `sudo apt install python3.12-venv`
- if you face an error: `AttributeError: module 'pkgutil' has no attribute 'ImpImporter'. Did you mean: 'zipimporter'?`, try `python3.12 -m pip install --upgrade setuptools`

**If you have Python < 3.12**
- switch to the branch `master-python-3.10`
- if you will copy some code from this file while doing tasks, remove all `@override` statements from that code

**How to generate a level**: see `python src/level_editor/level_generator.py`

**TASKS**
1. Creating the `Enemy` class and placing an enemy on the level 
- Copy a file `src/actors/characters/Fox.py` and rename it into `Enemy.py`, also rename the class `Fox` into `Enemy` in the new file
- 