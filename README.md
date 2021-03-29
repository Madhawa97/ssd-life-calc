# SSD-Life-Calc

## Introduction

Simple calculator for check the usable time period of the SSD on your M1 Macs on the go.
The results will be further accurate with a Longer time period ( minimum is a day, a month is preferred. )

This script calculates based on the available free space on your SSD and **assuming these SSDs have a 150TBW per 250GB.**


## Prerequisites

install [Smartmontools](https://www.smartmontools.org/) via [Homebrew](https://brew.sh/) using,

``` shell
brew install smartmontools
```

**run Following command.** it will create a file named "firstssdlc.json" in your **home directory**. You only need to run this command at the first time.

``` shell
smartctl -a disk0 -j > ~/firstssdlc.json
```
  

## How to Use


**Locate the terminal to your Home directory** and run the `calc.py` python script. 
```shell
python3 ~/PATH/TO/THE/FILE/calc.py
```

or,  
just place the calc.py in the Home directory.
  

### Set an alias in .zshrc
example:
``` shell
alias slc="python3 ~/Projects/ssd-life-calc/calc.py"
```

  
## Sample Run

<img width="942" alt="Screenshot 2021-03-30 at 02 53 12" src="https://user-images.githubusercontent.com/70215958/112902068-3a102c80-9103-11eb-982a-5d94956e850f.png">


  
  
## Removal
This script will create 2 files in your home directory. (firstssdlc.json and newssdlc.json) you can delete them if you no longer use the script. 
