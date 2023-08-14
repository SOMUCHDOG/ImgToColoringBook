<h1>A script to automate converting images to a pdf coloring book that is compatible with Amazon KDP.</h1>

![somuchdog_arcana_3d_3d_render_highly_detailed_32k_uhd_as_an_adu_fe89092c-ad02-4609-bffc-d597f070983c](https://github.com/SOMUCHDOG/ImgToColoringBook/assets/35353414/6eb15a42-0057-4c2d-85e5-9fe5562c9260)


To use you will need to install Python3

*I am using MacOS and homebrew, you may need to use different commands for Windows or Linux*

Tested with version 3.11.4

# Install Python:

## MacOS
```
brew install python3
```
## Linux
```
apt-get install python3
```
## Windows
https://www.python.org/downloads/windows/


# Install Pillow and reportLab
```
pip install Pillow reportLab
```

Upload images you want to convert into the folder. I used an aspect ratio of 3:4, I have not tested with other ratios.

Run the program!

```
python3 main.py
```

if you are having issues with running the program it is likely you have not configured your $PATH variable to your interpreter.
You can use the command
```
Where Python3
```
to locate it and use this command to run it while in the project directory. Optionally you can configure your python3 interpreter $PATH variable.
```
path/to/your/Python3 main.py
```
Should export as a pdf in the directory. :) Best of luck!

If you have questions, feel free to raise an issue and I will do my best to help you out.


