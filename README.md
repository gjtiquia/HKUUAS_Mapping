# HKU UAS Mapping Package
The HKU Unmanned Aerial Systems Team (HKU UAS) Mapping Python Package.

For example usage, refer to HKUUAS_Mapping/src/HKUUAS_Mapping/main.py

Suggested image dataset for testing: https://github.com/pierotofy/drone_dataset_sheffield_park_2/tree/master

# Usage
**Run as a package**
1. Intialize a pipenv environment

```bash
pipenv shell
```

2. Install packages

```bash
bash install_packages.sh
```

3. Run OpenDroneMap Docker Container
```bash
bash run_odm_docker.sh
```

This will run the docker container (name: hkuuas-mapping) in detech mode.

4. 


**Example**
```
from ... import Package.FunctionOrWhatever

FunctionOrWhatever(args)
```

**Requirements**
```
pipreqs output
```


# Contents
```
Package
┣ Folder1
┃ ┣ File1.json
┃ ┣ File2.bin
┃ ┗ File3.txt
┣ Subpackage1
┃ ┣ README.md
┃ ┗ __init__.py
┣ README.md
┗ __init__.py
```
## **\_\_init__.py**
Description of file + any useful information

---
## **Folder**
Description of folder and contents

---
## **Subpackages**

### **Subpackage1** ###
Description of what subpackage1 does
