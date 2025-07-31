import os
from datetime import date
import json
import time
import sys

# ANSI Color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(text="Loading", duration=3):
    """Simple loading animation with dots"""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for char in chars:
            if time.time() >= end_time:
                break
            sys.stdout.write(f'\r{Colors.CYAN}{char} {text}...{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.1)
    
    sys.stdout.write('\r' + ' ' * (len(text) + 10) + '\r')
    sys.stdout.flush()

def progress_bar(duration=2):
    """Animated progress bar"""
    width = 50
    print(f"\n{Colors.BRIGHT_BLUE}Analyzing SSD Health:{Colors.RESET}")
    
    for i in range(width + 1):
        percentage = (i / width) * 100
        filled = '█' * i
        empty = '░' * (width - i)
        
        # Color gradient effect
        if percentage < 33:
            color = Colors.BRIGHT_RED
        elif percentage < 66:
            color = Colors.BRIGHT_YELLOW
        else:
            color = Colors.BRIGHT_GREEN
            
        sys.stdout.write(f'\r{color}[{filled}{empty}] {percentage:5.1f}%{Colors.RESET}')
        sys.stdout.flush()
        time.sleep(duration / width)
    
    print()

def print_3d_banner():
    """3D styled banner with colors and shadows"""
    clear_screen()
    
    # 3D SSD Life Calculator banner with shadow effect
    banner_lines = [
        "   ███████╗███████╗██████╗     ██╗     ██╗███████╗███████╗",
        "   ██╔════╝██╔════╝██╔══██╗    ██║     ██║██╔════╝██╔════╝",
        "   ███████╗███████╗██║  ██║    ██║     ██║█████╗  █████╗  ",
        "   ╚════██║╚════██║██║  ██║    ██║     ██║██╔══╝  ██╔══╝  ",
        "   ███████║███████║██████╔╝    ███████╗██║██║     ███████╗",
        "   ╚══════╝╚══════╝╚═════╝     ╚══════╝╚═╝╚═╝     ╚══════╝",
        "",
        "    ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ ",
        "   ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗",
        "   ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝",
        "   ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗",
        "   ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║",
        "    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝"
    ]
    
    # Shadow lines (offset and dimmed)
    shadow_lines = []
    for line in banner_lines:
        if line.strip():  # Only add shadow for non-empty lines
            shadow_lines.append("  " + line)  # Offset by 2 spaces
        else:
            shadow_lines.append("")
    
    # Print shadow first (dimmed)
    print(f"{Colors.DIM}{Colors.BRIGHT_BLACK}")
    for line in shadow_lines:
        print(line)
    print(Colors.RESET)
    
    # Move cursor up to overlay the main banner
    print(f"\033[{len(shadow_lines)}A", end="")
    
    # Print main banner with gradient colors
    gradient_colors = [
        Colors.BRIGHT_CYAN,
        Colors.BRIGHT_BLUE,
        Colors.BLUE,
        Colors.BRIGHT_MAGENTA,
        Colors.MAGENTA,
        Colors.BRIGHT_RED,
        Colors.RED,
        Colors.BRIGHT_YELLOW,
        Colors.YELLOW,
        Colors.BRIGHT_GREEN,
        Colors.GREEN,
        Colors.BRIGHT_CYAN,
        Colors.CYAN
    ]
    
    for i, line in enumerate(banner_lines):
        color = gradient_colors[i % len(gradient_colors)]
        print(f"{Colors.BOLD}{color}{line}{Colors.RESET}")
    
    # Decorative border
    border = "═" * 88
    print(f"\n{Colors.BRIGHT_CYAN}{Colors.BOLD}╔{border}╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}║{' ' * 88}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}║{Colors.BRIGHT_WHITE}{'Advanced SSD Health Monitoring & Lifespan Prediction System'.center(88)}{Colors.BRIGHT_CYAN}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}║{' ' * 88}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}╚{border}╝{Colors.RESET}\n")

# Generate current data files with loading animation
def generate_data_files():
    print(f"{Colors.BRIGHT_YELLOW}Initializing SSD diagnostics...{Colors.RESET}")
    loading_animation("Gathering SMART data", 2)
    
    os.system("smartctl -a disk0 -j > ~/newssdlc.json")
    loading_animation("Collecting disk information", 1)
    
    os.system('diskutil info -plist / | plutil -convert json -o ~/currentdiskinfo.json -')
    
    progress_bar(1.5)
    print(f"{Colors.BRIGHT_GREEN}✓ Data collection complete!{Colors.RESET}\n")

def num_of_days(date1, date2):
    return (date2 - date1).days

month = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

def print_out():
    # Color-coded information with status indicators
    def get_status_color(value, thresholds):
        if isinstance(value, str):
            return Colors.BRIGHT_WHITE
        if value < thresholds[0]:
            return Colors.BRIGHT_GREEN
        elif value < thresholds[1]:
            return Colors.BRIGHT_YELLOW
        else:
            return Colors.BRIGHT_RED

    # Health status indicators
    wear_color = get_status_color(percentage_used, [50, 80])
    space_color = get_status_color(usage_percentage, [70, 90])
    
    info = [
        ("SSD Model", obj_new_file.get('model_name', 'Unknown')),
        ("Temperature", f"{obj_new_file['nvme_smart_health_information_log'].get('temperature', 'Unknown')}°C"),
        ("Power-On Hours", f"{Colors.BRIGHT_BLUE}{power_on_hours:,}{Colors.RESET} hrs"),
        ("Power Cycles", f"{Colors.BRIGHT_BLUE}{obj_new_file['nvme_smart_health_information_log'].get('power_cycles', 0):,}{Colors.RESET}"),
        ("Unsafe Shutdowns", f"{Colors.BRIGHT_RED if obj_new_file['nvme_smart_health_information_log'].get('unsafe_shutdowns', 0) > 0 else Colors.BRIGHT_GREEN}{obj_new_file['nvme_smart_health_information_log'].get('unsafe_shutdowns', 0)}{Colors.RESET}"),
        ("Wear Level", f"{wear_color}{percentage_used}%{Colors.RESET} used"),
        ("Free Space", f"{Colors.BRIGHT_GREEN}{avail_space:.2f}{Colors.RESET} GB"),
        ("Used Space", f"{space_color}{used_space:.2f} GB ({usage_percentage:.1f}%){Colors.RESET}"),
        ("Monitoring Period", f"{Colors.BRIGHT_CYAN}{time_period}{Colors.RESET} days"),
        ("Written This Period", f"{Colors.BRIGHT_MAGENTA}{data_written_diff:.2f}{Colors.RESET} TB"),
        ("Daily Write Rate", f"{Colors.BRIGHT_YELLOW}{daily_write_rate:.3f}{Colors.RESET} TB/day"),
        ("Yearly Write Rate", f"{Colors.BRIGHT_YELLOW}{yearly_write_rate:.2f}{Colors.RESET} TB/year"),
        ("Life: TBW Method", f"{Colors.BRIGHT_GREEN if life_time_tbw > 5 else Colors.BRIGHT_YELLOW if life_time_tbw > 2 else Colors.BRIGHT_RED}{life_time_tbw:.2f} yrs{Colors.RESET} → {Colors.BRIGHT_CYAN}{replacement_year_tbw}{Colors.RESET}" if life_time_tbw != float('inf') else f"{Colors.BRIGHT_GREEN}∞{Colors.RESET}"),
        # ("Life: SMART Method", f"{Colors.BRIGHT_GREEN if life_time_smart > 5 else Colors.BRIGHT_YELLOW if life_time_smart > 2 else Colors.BRIGHT_RED}{life_time_smart:.2f} yrs{Colors.RESET} → {Colors.BRIGHT_CYAN}{replacement_year_smart}{Colors.RESET}" if life_time_smart != float('inf') else f"{Colors.BRIGHT_GREEN}∞{Colors.RESET}"),
        ("Life: Free Space Method", f"{Colors.BRIGHT_GREEN if life_time_free_space > 5 else Colors.BRIGHT_YELLOW if life_time_free_space > 2 else Colors.BRIGHT_RED}{life_time_free_space:.2f} yrs{Colors.RESET} → {Colors.BRIGHT_CYAN}{replacement_year_free_space}{Colors.RESET}" if life_time_free_space != float('inf') else f"{Colors.BRIGHT_GREEN}∞{Colors.RESET}"),
    ]

    # Print results section header
    print(f"\n{Colors.BRIGHT_WHITE}{Colors.BG_BLUE} 📊 SSD HEALTH ANALYSIS RESULTS {Colors.RESET}\n")
    
    # Print info with enhanced formatting
    info_lines = [f"{Colors.BRIGHT_WHITE}{label:<22}{Colors.RESET}: {value}" for label, value in info]
    
    for line in info_lines:
        print(f"  {line}")

    # Enhanced footer with recommendations
    print(f"\n{Colors.BRIGHT_CYAN}{'─' * 88}{Colors.RESET}")
    
    # Health assessment
    if percentage_used < 50:
        health_status = f"{Colors.BRIGHT_GREEN}🟢 EXCELLENT{Colors.RESET}"
    elif percentage_used < 80:
        health_status = f"{Colors.BRIGHT_YELLOW}🟡 GOOD{Colors.RESET}"
    else:
        health_status = f"{Colors.BRIGHT_RED}🔴 CAUTION{Colors.RESET}"
    
    print(f"{Colors.BRIGHT_WHITE}Overall SSD Health: {health_status}")
    print(f"{Colors.DIM}💡 Tip: SMART method uses wear level progression over time.{Colors.RESET}")
    print(f"{Colors.DIM}📝 Note: Free Space method shows conservative estimate based on available space.{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{'═' * 88}{Colors.RESET}\n")

try:
    print_3d_banner()
    generate_data_files()

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

        # Method 1: TBW-based calculation (same as old code)
        if yearly_write_rate > 0:
            life_time_tbw = ssd_tbw_rating / yearly_write_rate
            replacement_year_tbw = year_n + int(life_time_tbw)
        else:
            life_time_tbw = float('inf')
            replacement_year_tbw = "N/A"

        # Method 2: SMART-based calculation (fixed from old code logic)
        if percentage_used > 0 and time_period > 0:
            # Calculate wear rate per day based on the monitoring period
            wear_rate_per_day = percentage_used / time_period
            remaining_percentage = 100 - percentage_used
            remaining_days = remaining_percentage / wear_rate_per_day if wear_rate_per_day > 0 else float('inf')
            life_time_smart = remaining_days / 365  # Convert to years
            replacement_year_smart = year_n + int(life_time_smart) if life_time_smart != float('inf') else "N/A"
        else:
            life_time_smart = float('inf')
            replacement_year_smart = "N/A"

        # Method 3: Free space method (corrected calculation from old code)
        if yearly_write_rate > 0 and avail_space > 0:
            # Convert available space from GB to TB
            available_space_tb = avail_space / 1000
            # Calculate lifespan based on proportional TBW for available space
            proportional_tbw = (ssd_tbw_rating / ssd_capacity_gb) * avail_space
            life_time_free_space = proportional_tbw / yearly_write_rate
            replacement_year_free_space = year_n + int(life_time_free_space)
        else:
            life_time_free_space = float('inf')
            replacement_year_free_space = "N/A"

except FileNotFoundError as e:
    print(f"{Colors.BRIGHT_RED}❌ File not found: {e}{Colors.RESET}")
    print("Make sure both firstssdlc.json and the generated files exist.")
except KeyError as e:
    print(f"{Colors.BRIGHT_RED}❌ Key error: {e}{Colors.RESET}")
    print("JSON structure might have changed. Please check the file contents.")
except TypeError as e:
    print(f"{Colors.BRIGHT_RED}❌ Type Error: {e}{Colors.RESET}")
    print("Please check data types in JSON files.")
except ValueError as e:
    print(f"{Colors.BRIGHT_RED}❌ Value Error: {e}{Colors.RESET}")
    print("Please check data values in JSON files.")
except ZeroDivisionError:
    print(f"{Colors.BRIGHT_RED}❌ Division by zero error - no time period or write activity detected.{Colors.RESET}")
except Exception as e:
    print(f"{Colors.BRIGHT_RED}❌ Unexpected error: {e}{Colors.RESET}")
else:
    print_out()
finally:
    print(f"\n{Colors.BRIGHT_CYAN}Press {Colors.BRIGHT_WHITE}\"Enter\"{Colors.BRIGHT_CYAN} to exit...{Colors.RESET}")
    input()