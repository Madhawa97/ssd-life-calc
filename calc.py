import os
from datetime import date
import json

# Generate current data files
os.system("smartctl -a disk0 -j > ~/newssdlc.json")
os.system('diskutil info -plist / | plutil -convert json -o ~/currentdiskinfo.json -')

def num_of_days(date1, date2):
    return (date2 - date1).days

month = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

def print_banner():
    print("=" * 80)
    print("█" * 80)
    print("█" + " " * 78 + "█")
    print("█" + " " * 25 + "SSD LIFE CALCULATOR" + " " * 34 + "█")
    print("█" + " " * 78 + "█")
    print("█" * 80)
    print("=" * 80)
    print()

def print_out():
    ascii_logo = r"""
   ██████  ██        ██████  
  ██       ██       ██    ██
  ███████  ██      ███ 
        ██ ██       ██    ██ 
   ██████  ███████   ██████  
    """

    info = [
        ("SSD Model", obj_new_file.get('model_name', 'Unknown')),
        ("Temperature", f"{obj_new_file['nvme_smart_health_information_log'].get('temperature', 'Unknown')}°C"),
        ("Power-On Hours", f"{power_on_hours:,} hrs"),
        ("Power Cycles", f"{obj_new_file['nvme_smart_health_information_log'].get('power_cycles', 0):,}"),
        ("Unsafe Shutdowns", obj_new_file['nvme_smart_health_information_log'].get('unsafe_shutdowns', 0)),
        ("Wear Level", f"{percentage_used}% used"),
        ("Free Space", f"{avail_space:.2f} GB"),
        ("Used Space", f"{used_space:.2f} GB ({usage_percentage:.1f}%)"),
        ("Monitoring Period", f"{time_period} days"),
        ("Written This Period", f"{data_written_diff:.2f} TB"),
        ("Daily Write", f"{daily_write_rate:.3f} TB/day"),
        ("Yearly Write", f"{yearly_write_rate:.2f} TB/year"),
        ("Life: TBW", f"{life_time_tbw:.2f} yrs → {replacement_year_tbw}" if life_time_tbw != float('inf') else "∞"),
        # ("Life: SMART", f"{life_time_smart:.2f} yrs → {replacement_year_smart}" if life_time_smart != float('inf') else "∞"), // Commented as the logic needs to be updated by research
        ("Life: Free Space", f"{life_time_free_space:.2f} yrs → {replacement_year_free_space}" if life_time_free_space != float('inf') else "∞"),
    ]

    # Print logo and info side-by-side
    logo_lines = ascii_logo.strip("\n").split("\n")
    info_lines = [f"{label:<22}: {value}" for label, value in info]
    max_lines = max(len(logo_lines), len(info_lines))

    for i in range(max_lines):
        left = logo_lines[i] if i < len(logo_lines) else " " * 28
        right = info_lines[i] if i < len(info_lines) else ""
        print(f"{left:<30}  {right}")

    # Footer
    print("\n" + "-" * 80)
    print("Tip: SMART estimates are generally more accurate for modern SSDs.")
    print("Note: Real-world lifespan often exceeds manufacturer TBW ratings.")
    print("=" * 80 + "\n")


try:
    print_banner()

    # Get currently available free space from JSON
    with open(os.path.expanduser('~/currentdiskinfo.json'), 'r') as cfs:
        disk_info = json.load(cfs)

    container_free_space_bytes = disk_info.get("APFSContainerFree", 0)
    avail_space = container_free_space_bytes / (1000 ** 3)

    with open(os.path.expanduser('~/firstssdlc.json'), 'r') as first_file:
        obj_first_file = json.load(first_file)

    with open(os.path.expanduser('~/newssdlc.json'), 'r') as new_file:
        obj_new_file = json.load(new_file)

    data_written_from_first_reading = (obj_first_file["nvme_smart_health_information_log"]["data_units_written"]
                                     * 512000) / (1000 ** 4)
    data_written_from_new_reading = (obj_new_file["nvme_smart_health_information_log"]["data_units_written"]
                                   * 512000) / (1000 ** 4)

    data_read_from_first_reading = (obj_first_file["nvme_smart_health_information_log"]["data_units_read"]
                                  * 512000) / (1000 ** 4)
    data_read_from_new_reading = (obj_new_file["nvme_smart_health_information_log"]["data_units_read"]
                                * 512000) / (1000 ** 4)

    data_written_diff = data_written_from_new_reading - data_written_from_first_reading
    data_read_diff = data_read_from_new_reading - data_read_from_first_reading

    total_space = disk_info.get("APFSContainerSize", 0) / (1000 ** 3)
    used_space = total_space - avail_space
    usage_percentage = (used_space / total_space) * 100 if total_space > 0 else 0

    time_on_firstfile = obj_first_file["local_time"]["asctime"]
    time_on_newfile = obj_new_file["local_time"]["asctime"]

    day_f = int(time_on_firstfile[8:10])
    month_f = month[time_on_firstfile[4:7]]
    year_f = int(time_on_firstfile[20:24])

    day_n = int(time_on_newfile[8:10])
    month_n = month[time_on_newfile[4:7]]
    year_n = int(time_on_newfile[20:24])

    date1 = date(year_f, month_f, day_f)
    date2 = date(year_n, month_n, day_n)
    time_period = num_of_days(date1, date2)

    percentage_used = obj_new_file['nvme_smart_health_information_log'].get('percentage_used', 0)
    available_spare = obj_new_file['nvme_smart_health_information_log'].get('available_spare', 100)
    power_on_hours = obj_new_file['nvme_smart_health_information_log'].get('power_on_hours', 0)

    ssd_capacity_gb = 256
    ssd_tbw_rating = 150  # TBW

    # Defaults
    daily_write_rate = 0
    yearly_write_rate = 0
    life_time_tbw = 0
    life_time_smart = 0
    life_time_free_space = 0
    replacement_year_tbw = "N/A"
    replacement_year_smart = "N/A"
    replacement_year_free_space = "N/A"

    if time_period > 0:
        daily_write_rate = data_written_diff / time_period
        yearly_write_rate = daily_write_rate * 365
        yearly_read_rate = (data_read_diff / time_period) * 365

        # Method 1: TBW
        if yearly_write_rate > 0:
            life_time_tbw = ssd_tbw_rating / yearly_write_rate
            replacement_year_tbw = year_n + int(life_time_tbw)
        else:
            life_time_tbw = float('inf')
            replacement_year_tbw = "N/A"

        # Method 2: SMART
        if percentage_used > 0 and power_on_hours > 0:
            # wear_rate_per_hour = percentage_used / power_on_hours
            # remaining_percentage = 100 - percentage_used
            # remaining_hours = remaining_percentage / wear_rate_per_hour if wear_rate_per_hour > 0 else float('inf')

            wear_rate_per_day = percentage_used / time_period  # time_period is days between readings
            remaining_days = (100 - percentage_used) / wear_rate_per_day
            life_time_smart = remaining_days / 365  # in years

            # life_time_smart = remaining_hours / (24 * 365)
            replacement_year_smart = year_n + int(life_time_smart) if life_time_smart != float('inf') else "N/A"
        else:
            life_time_smart = float('inf')
            replacement_year_smart = "N/A"

        # Method 3: Free space method (explicit)
        if yearly_write_rate > 0:
            life_time_free_space = (ssd_tbw_rating / ssd_capacity_gb) * avail_space / yearly_write_rate
            replacement_year_free_space = year_n + int(life_time_free_space)
        else:
            life_time_free_space = float('inf')
            replacement_year_free_space = "N/A"

except FileNotFoundError as e:
    print(f"File not found: {e}")
    print("Make sure both firstssdlc.json and the generated files exist.")
except KeyError as e:
    print(f"Key error: {e}")
    print("JSON structure might have changed. Please check the file contents.")
except TypeError as e:
    print(f"Type Error: {e}")
    print("Please check data types in JSON files.")
except ValueError as e:
    print(f"Value Error: {e}")
    print("Please check data values in JSON files.")
except ZeroDivisionError:
    print("Division by zero error - no time period or write activity detected.")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print_out()
finally:
    input("Press \"Enter\" to Quit.")
