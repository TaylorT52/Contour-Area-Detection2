# Contour Detection

## Setup
To install, please ensure you have python 3.9.1 or later!

### Install dependencies
Note! Some are only used for debugging the algorithm and can be removed if they don't install correctly on your computer! See the `requirements.txt` for notes.

```
pip3 install -r requirements.txt
```

### Create the egg
This will make a python egg in the folder called `output`:

```
python3 create_egg.py
```

### Add to your program
You can now add the module to your program:

```python
import sys
from os import listdir
from os.path import isfile, join

sys.path.append('../output/contour_detection-1.0-py3.9.egg')

import contour_detection

# set the minimmum amount of image that is not detected to be slide
min_percent = 50

detection_obj = contour_detection.ContourDetection(path, min_percent)

acceptable = detection_obj.contoured_area(False)

# acceptable is set to `True` if it's over the threshold, and `False` if not
```

### Example program
There is an example program called `./scripts/test.py` folder that will read the file `test1.jpg`
in the `sample_images` directory and show the image
