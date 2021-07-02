# SSD-Life-Calc

## Introduction

Simple calculator for check the usable time period of the SSD on your M1 Mac.
The results will be further accurate with a Longer time period ( minimum is 1 day, a month is preferred )

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

<img width="942" alt="Screenshot 2021-07-02 at 23 46 59" src="https://user-images.githubusercontent.com/70215958/124314334-db3dd180-db8f-11eb-8be8-959f43c85621.png">


  
  
## Removal
This script will create 3 files in your home directory. (firstssdlc.json, newssdlc.json and currentfreespace.txt) you can delete them if you're no longer using the script. 
