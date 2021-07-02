import os
from datetime import date
import json

os.system("smartctl -a disk0 -j > ~/newssdlc.json")
os.system('diskutil info / | grep "Free Space" > ~/currentfreespace.txt')

def num_of_days(date1, date2):
    return (date2-date1).days

month = {	'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12		}

def print_out():
    print("_"*80+"\n")
    print(f"\tDate of first read : \t\t\t {day_f}-{month_f}-{year_f}")
    print(f"\tData Units Written at first read : \t {data_written_from_first_reading} TB\n")
    print(f"\tDate of current read : \t\t\t {day_n}-{month_n}-{year_n}")
    print(f"\tData Units Written at current read : \t {data_written_from_new_reading} TB\n")
    print(f"\tTime period : \t\t\t\t {time_period} Days\n")
    print(f"\tAvailable free space : \t\t\t {avail_space} GB\n")
    print(f"\tMinimum life expectancy : \t\t {life_time} Years\n")
    print("* please not that, Modern SSDs can last more than 2 times the above time period.")
    print("_"*80+"\n")

try:
    # get currently available free space
    cfs = open('currentfreespace.txt')
    cfs_lines = cfs.readlines()
    cfs_line = cfs_lines[0]
    cfsl_index = cfs_line.index('exactly')
    cfs_int = round((int(cfs_line[cfsl_index:].split()[1]))*512000/1000**4, 1)


    first_file = open('firstssdlc.json')
    json_data_of_firstfile = first_file.read()
    obj_first_file = json.loads(json_data_of_firstfile)

    new_file = open('newssdlc.json')
    json_data_of_newfile = new_file.read()
    obj_new_file = json.loads(json_data_of_newfile)

    data_written_from_first_reading = round(((obj_first_file["nvme_smart_health_information_log"]).get("data_units_written"))*512000/1000**4, 3)
    data_written_from_new_reading = round(((obj_new_file["nvme_smart_health_information_log"]).get("data_units_written"))*512000/1000**4, 3)

    time_on_firstfile = (obj_first_file["local_time"]).get("asctime")
    time_on_newfile = (obj_new_file["local_time"]).get("asctime")

    day_f = int(time_on_firstfile[8:10])
    month_f = month[(time_on_firstfile[4:7])]
    year_f = int(time_on_firstfile[20:24])
    day_n = int(time_on_newfile[8:10])
    month_n = month[(time_on_newfile[4:7])]
    year_n = int(time_on_newfile[20:24])

    date1 = date(year_f, month_f, day_f)
    date2 = date(year_n, month_n, day_n)

    time_period = (num_of_days(date1, date2))
    # avail_space = float(input("\nEnter the currently available Free Space on your SSD in GBs : "))
    avail_space = cfs_int
    life_time = round(150/256*avail_space /((data_written_from_new_reading - data_written_from_first_reading)*365/time_period), 2)

except TypeError:
    print("Type Error! please try again.")
    raise
except ValueError:
    print("Value Error! please try again.")
    raise

else:
    print_out()

finally:
    first_file.close()
    new_file.close()
    cfs.close()
    input("Press \"Enter\" to Quit.")


