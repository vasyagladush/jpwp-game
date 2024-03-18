**Python version: 3.12**
[A guide to install python3.12 on Linux](https://medium.com/@donfiealex/getting-python-3-12-up-and-running-on-ubuntu-and-debian-servers-cbe557d7d368)

**How to setup a virtual environment**:
```console
// create a virual environment under a folder named 'venv'
$ python3.12 -m venv venv 
// activate the venv (command for Linux, Windows' command for activation might differ)
$ source ./venv/bin/activate 
``` 

**Dependencies installation**: `pip3.12 install -r requirements.txt`

**Dependencies**: 
- python3.12 venv: `sudo apt install python3.12-venv`
- pygame-ce: `pip3.12 install pygame-ce`
If you face an error: `AttributeError: module 'pkgutil' has no attribute 'ImpImporter'. Did you mean: 'zipimporter'?`, try `python3.12 -m pip install --upgrade setuptools`
 