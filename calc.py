import os
os.system("smartctl -a disk0 > ~/newssdlc.txt")


'''
If your code isn't working as expected, 
use the commented out code to find the index of you TB value. 
update line 15 and 20 accordingly. 
.strip method will remove the extra bit from the selected part.
'''

first_file = open('firstssdlc.txt')
all_lines_of_first_file = first_file.readlines()
line_with_data_from_fristfile = all_lines_of_first_file[32]
# print(lines[32].index("TB")) 
data_value_from_first_file = (line_with_data_from_fristfile[45:52]).strip(" TB[]")
first_data_value = float(data_value_from_first_file)

new_file = open('newssdlc.txt')
all_lines_of_new_file = new_file.readlines()
line_with_data_from_newfile = all_lines_of_new_file[32]
data_value_from_new_file = (line_with_data_from_newfile[45:52]).strip(" TB[]")
new_data_value = float(data_value_from_new_file)

time_period = float(input("No. of Days from the creation of firstssdlc.txt file? : "))  # in days
#drive_size = 256  # (GB)
avail_space = float(input("Enter the current available Free Space on your SSD in GBs : "))  # free space available (GB)
life_time = round(150/256*avail_space /((new_data_value - first_data_value)*365/time_period), 2)

# counting from purchasing date
print(f"You have at least {life_time} years of lifetime")

first_file.close()
new_file.close()
input("Press \"Enter\" to Quit.")
