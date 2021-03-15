# SSD-Life-Calc

## Introduction

Simple calculator for check the usable time period of the SSD on your M1 Macs based on your usage.
The results will be further accurate with a Longer time period ( minimum is a day, a month is preferred. )

This calculates based on the available free space on your SSD and **assuming these SSDs have a 150TBW value per 250GB.**  
Thats the worst case scenario. Based on the current speculations these drives could have a (500 to 1500)TBW value per 256GB.

haven't tested for intel macs.

## Prerequisites

install [Smartmontools](https://www.smartmontools.org/) via [Homebrew](https://brew.sh/) using,

``` shell
brew install smartmontools
```

**run Following command.** it will create a file named "firstssdlc.txt" in your **home directory**. You need to perform this at the first time.

``` shell
smartctl -a disk0 > ~/firstssdlc.txt
```
 


## How to Use

After few days or months of regular usage, you can check your SSD's usable time period. if will be more accurate with a longer period of time.


**Locate the terminal to your Home directory** and run the `calc.py` python script. 
```shell
python3 ~/PATH/TO/THE/FILE/calc.py
```
(replace the PATH/TO/THE/FILE with your own location or just place the calc.py in the Home directory)

### Set Alias in .zshrc
example:
``` shell
alias slc="python3 ~/Projects/ssd-life-calc/calc.py"
```
<img width="838" alt="Screenshot 2021-03-15 at 05 23 14" src="https://user-images.githubusercontent.com/70215958/111089045-13bd8f00-8550-11eb-9fec-36441f045749.png">

## Removal
All of this process will create 2 files in your home directory. (firstssdlc.txt and newssdlc.txt) you can delete them if you're no longer using the script. 
