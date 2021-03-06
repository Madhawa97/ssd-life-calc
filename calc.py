f = open('first.txt')
lines = f.readlines()
# print(lines[32].index("TB"))
line = lines[32]
#tb_location = line.index("TB")
# print(tb_location)
first_read_from_file = (line[45:52]).strip(" TB[]")

g = open('new.txt')
lines_2 = g.readlines()
line_2 = lines_2[32]
new_read_from_file = (line_2[45:52]).strip(" TB[]")

first_read = float(first_read_from_file)
# first_read = 1.47  # (TB)
new_read = float(new_read_from_file)
# new_read = 1.61  # (TB)
time_period = float(
    input("No. of Days from the creation of first.txt file? : "))  # in days
drive_size = 256  # (GB)
avail_space = float(
    input("Enter the current available Free Space on your SSD in GBs : "))  # free space available (GB)
life_time = round(150/256*avail_space /
                  ((new_read - first_read)*365/time_period), 2)

print(f"You have {life_time} years of lifetime")  # from purchasing date

f.close()
g.close()
input()
