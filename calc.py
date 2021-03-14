import os
from datetime import date

os.system("smartctl -a disk0 > ~/newssdlc.txt")

def numOfDays(date1, date2):
    return (date2-date1).days


'''
If your code isn't working as expected, 
adjust these lines :- 18,19,21, 26,27,28, 43,44,45,46,47,48. 
you can manually enter the time period instead of adjusting line from 43 to 48
'''

first_file = open('firstssdlc.txt')
all_lines_of_first_file = first_file.readlines()
line_with_data_from_firstfile = all_lines_of_first_file[32]
line_with_date_from_firstfile = all_lines_of_first_file[12]
# print(lines[32].index("TB")) 
data_value_from_first_file = (line_with_data_from_firstfile[45:52]).strip(" TB[]")
first_data_value = float(data_value_from_first_file)

new_file = open('newssdlc.txt')
all_lines_of_new_file = new_file.readlines()
line_with_data_from_newfile = all_lines_of_new_file[32]
line_with_date_from_newfile = all_lines_of_new_file[12]
data_value_from_new_file = (line_with_data_from_newfile[45:52]).strip(" TB[]")
new_data_value = float(data_value_from_new_file)

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
year_f = int((line_with_date_from_firstfile[56:61]).strip(" +"))
month_f = month[(line_with_date_from_firstfile[40:43]).strip(" +")]
day_f = int((line_with_date_from_firstfile[44:47]).strip(" +"))
year_n = int((line_with_date_from_newfile[56:61]).strip(" +"))
month_n = month[(line_with_date_from_newfile[40:43]).strip(" +")]
day_n = int((line_with_date_from_newfile[44:47]).strip(" +"))

date1 = date(year_f, month_f, day_f)
date2 = date(year_n, month_n, day_n)
#print(type(numOfDays(date1, date2)))

time_period = (numOfDays(date1, date2))
avail_space = float(input("Enter the current available Free Space on your SSD in GBs : "))  # free space available (GB)
life_time = round(150/256*avail_space /((new_data_value - first_data_value)*365/time_period), 2)

# counting from purchasing date
print(f"You have at least {life_time} years of lifetime")

first_file.close()
new_file.close()
input("Press \"Enter\" to Quit.")
