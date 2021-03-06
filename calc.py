first_read = 1.47  # (TB)
new_read = 1.61  # (TB)
time_period = 7  # in days
drive_size = 256  # (GB)
avail_space = 170  # free space available (GB)
life_time = round(150/256*avail_space /
                  ((new_read - first_read)*365/time_period), 2)

print(f"You have {life_time} years of lifetime")  # from purchasing date
