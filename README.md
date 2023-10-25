# winsi

Python script to set window size.

Sometimes I need to change some window size to be 16:9/HD in order to record the window using OBS. The first time I did it by hand, but quickly I tried to automate the process using Python and Windows.

It set the previous active windows. For example, you click on your browser, then in the terminal to run the script, and your browser get resized. For me it's useful and handy.

## Setup

> You need to install Python in Windows. It must be installed outside WSL2.

In a terminal, run:

```
git clone git@github.com:bypirob/winsi.git
cd winsi
python3 -m pip install pywin32

click the window you want to resize, and come back to the terminal

python3 winsi.py
```

You can change the width/height using the variables that are ate the top of the script.
