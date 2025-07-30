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
    print("_" * 80 + "\n")
    print("📊 SSD HEALTH INFORMATION:")
    print(f"\tSSD Model : \t\t\t\t {obj_new_file.get('model_name', 'Unknown')}")
    print(f"\tCurrent Temperature : \t\t\t {obj_new_file['nvme_smart_health_information_log'].get('temperature', 'Unknown')}°C")
    print(f"\tPower On Hours : \t\t\t {obj_new_file['nvme_smart_health_information_log'].get('power_on_hours', 0):,} hours")
    print(f"\tPower Cycles : \t\t\t\t {obj_new_file['nvme_smart_health_information_log'].get('power_cycles', 0):,}")
    print(f"\tUnsafe Shutdowns : \t\t\t {obj_new_file['nvme_smart_health_information_log'].get('unsafe_shutdowns', 0)}")
    print(f"\tPercentage Used : \t\t\t {obj_new_file['nvme_smart_health_information_log'].get('percentage_used', 0)}%")
    print(f"\tAvailable Spare : \t\t\t {obj_new_file['nvme_smart_health_information_log'].get('available_spare', 0)}%")
    print("\n" + "📈 USAGE ANALYSIS:")
    print(f"\tData Units Written at current read : \t {data_written_from_new_reading:.2f} TB")
    print(f"\tMonitored time period : \t\t {time_period} Days")
    print(f"\tData written in period : \t\t {data_written_diff:.2f} TB")
    print(f"\tData read in period : \t\t\t {data_read_diff:.2f} TB")
    print(f"\tAverage daily write : \t\t\t {daily_write_rate:.3f} TB/day")
    print(f"\tEstimated yearly write : \t\t {yearly_write_rate:.2f} TB/year")
    print("\n💾 STORAGE STATUS:")
    print(f"\tTotal Container Space : \t\t {total_space:.2f} GB")
    print(f"\tUsed Space : \t\t\t\t {used_space:.2f} GB")
    print(f"\tAvailable free space : \t\t\t {avail_space:.2f} GB")
    print(f"\tSpace usage percentage : \t\t {usage_percentage:.1f}%")
    print("\n⏳ LIFE EXPECTANCY ESTIMATES:")

    print("\n📊 Method 1: Based on Write Endurance (TBW Rating):")
    if life_time_tbw == float('inf'):
        print(f"\tLife expectancy : \t\t\t ∞ (No write activity detected)")
    else:
        print(f"\tLife expectancy : \t\t\t {life_time_tbw:.2f} Years")
        print(f"\tEstimated replacement date : \t\t {replacement_year_tbw}")
    print(f"\tBased on: Available space ({avail_space:.0f}GB) vs total endurance")

    print("\n🔬 Method 2: Based on Percentage Used (SMART Data):")
    if life_time_smart == float('inf'):
        print(f"\tLife expectancy : \t\t\t ∞ (No usage detected)")
    else:
        print(f"\tLife expectancy : \t\t\t {life_time_smart:.2f} Years")
        print(f"\tEstimated replacement date : \t\t {replacement_year_smart}")
    print(f"\tBased on: Current {percentage_used}% wear level over {power_on_hours:,} hours")

    print("\n📊 Method 3: Based on Available Free Space:")
    if life_time_free_space == float('inf'):
        print(f"\tLife expectancy : \t\t\t ∞ (No write activity detected)")
    else:
        print(f"\tLife expectancy : \t\t\t {life_time_free_space:.2f} Years")
        print(f"\tEstimated replacement date : \t\t {replacement_year_free_space}")
    print(f"\tBased on: Current available space ({avail_space:.0f}GB) vs estimated TBW usage rate")

    print(f"\n📈 Comparison:")
    life_estimates = {
        "TBW Method": life_time_tbw,
        "SMART Method": life_time_smart,
        "Free Space Method": life_time_free_space
    }

    usable = {k: v for k, v in life_estimates.items() if v != float('inf')}
    if len(usable) >= 2:
        best = max(usable, key=usable.get)
        worst = min(usable, key=usable.get)
        print(f"\tLongest estimate: {best} ({usable[best]:.2f} years)")
        print(f"\tShortest estimate: {worst} ({usable[worst]:.2f} years)")
    else:
        print(f"\tNot enough usable data for comparison")

    print("\n* Modern SSDs often last 2-5x longer than manufacturer ratings")
    print("* Method 1 uses conservative approach based on available space")
    print("* Method 2 uses actual wear measurement from SSD's internal monitoring")
    print("* Method 3 offers a hybrid of space and write rate")
    print("* Consider the more conservative (shorter) estimate for planning purposes")
    print("_" * 80 + "\n")

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
            life_time_tbw = (ssd_tbw_rating / ssd_capacity_gb) * avail_space / yearly_write_rate
            replacement_year_tbw = year_n + int(life_time_tbw)
        else:
            life_time_tbw = float('inf')
            replacement_year_tbw = "N/A"

        # Method 2: SMART
        if percentage_used > 0 and power_on_hours > 0:
            wear_rate_per_hour = percentage_used / power_on_hours
            remaining_percentage = 100 - percentage_used
            remaining_hours = remaining_percentage / wear_rate_per_hour if wear_rate_per_hour > 0 else float('inf')
            life_time_smart = remaining_hours / (24 * 365)
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
