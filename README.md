# plots

Yes another plotting repository.


# Installation
This program was made with python 2.7.

1. Install needed depdencies (if you don't have them)
```
pip install -r requirments.txt
```

# Usage
* Run ``python plot -h`` for help inormaiton
```
usage: plot.py [-h] [-f FILENAMETAG] [-d DEPTHS] [-s SIZE] [-p DENSITY]
               [-l LENGTH]
               task

Easy NAMS Plotting.

positional arguments:
  task                  task name

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAMETAG, --fileNameTag FILENAMETAG
                        Appends it to the end of a filename so it can be
                        unique when you plot it
  -d DEPTHS, --depths DEPTHS
                        integer - amount of depths/layers
  -s SIZE, --size SIZE  int - size of the domain (s,s)
  -p DENSITY, --density DENSITY
                        int - density of the plot (higher values mean more
                        lines)
  -l LENGTH, --length LENGTH
                        int - length or min length
```



* Options for ``task`` include, ``stream``, ``quiver``, and soon ``contour``.

Here is an example of creating a 30x30 plot with 5 layers using the stream
command:

```
python plot.py stream -s 30 -d 5

```
