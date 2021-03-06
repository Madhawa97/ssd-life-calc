## SSDLifeCalc
Simple calculator for check the usable time period of the SSD on your M1 Macs based on your usage.
The results will be further accurate with a Longer time period ( minimum is a day )

This calculate based on the available free space on your SSD and **assuming these SSDs have a 150TBW value per 250GB.**

haven't tested for intel macs.

### Prerequisites

install [Smartmontools](https://www.smartmontools.org/) via [Homebrew](https://brew.sh/) using,
``` shell
brew install smartmontools
```

locate to your **home directory** and create "first.txt" including the output from the [smartmontools](https://www.smartmontools.org/) using,
``` shell
smartctl -a disk0 > ~/first.txt
```

### How to Use
After few days of regular usage, you can check your SSD's usable time period.

Following steps should be performed every time you want to run the test.

```shell
smartctl -a disk0 > ~/new.txt
```
Then run the `calc.py` python script.  
which will ask you to enter the avaiable Free Space on your SSD and Number of days elapsed since the creation of first.txt

This will output the result on your terminal window.