# nciv

This program is still in very early stages of development and
will most likely not work for most users.

Dependancies:
 - python 3.5.5
 - w3m browser
 - python curses library

In Image.py, line 24, change the argument of subprocess.run() to 
point to the w3mimgdisplay executable file.

The program must be run within the directory to be viewed.
Example:
\# cd /path/to/image/directory
\# python /path/to/nciv/img.py

nciv has been tested on rxvt-unicode
