import os
import re
from datetime import datetime, timedelta
from PIL import Image
import pytesseract

# Regex to extract upgrade name and time e.g. "archer queen 1d 2h 15m"
upgrade_regex = re.compile(
    r'([a-zA-Z\s]+?)\s+((\d+d\s*)?(\d+h\s*)?(\d+m)?)',
    re.IGNORECASE
)


# Parse time string like '1d 2h 15m' into timedelta
def parse_time_str(time_str):
    days = hours = minutes = 0
    d_match = re.search(r'(\d+)d', time_str)
    h_match = re.search(r'(\d+)h', time_str)
    m_match = re.search(r'(\d+)m', time_str)
    if d_match:
        days = int(d_match.group(1))
    if h_match:
        hours = int(h_match.group(1))
    if m_match:
        minutes = int(m_match.group(1))
    return timedelta(days=days, hours=hours, minutes=minutes)


# Extract upgrades from one image file using OCR
def extract_upgrades_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    upgrades = []
    for match in upgrade_regex.finditer(text):
        upgrade_name = match.group(1).strip().lower()
        time_str = match.group(2).strip()
        if time_str:
            upgrade_time = parse_time_str(time_str)
            if upgrade_time.total_seconds() > 0:
                upgrades.append((upgrade_name, upgrade_time))
    return upgrades


# Extract upgrades from all images in a directory
def extract_upgrades_from_directory(directory):
    all_upgrades = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            path = os.path.join(directory, filename)
            print(f"Processing {filename}...")
            upgrades = extract_upgrades_from_image(path)
            all_upgrades.extend(upgrades)
    return all_upgrades


# Calculate finish time with clock tower boost applied repeatedly (every 22h cooldown after 22m boost)
def apply_clock_tower_boost(start_time, upgrade_duration, cooldown_left):
    BOOST_DURATION = timedelta(minutes=22)
    COOLDOWN = timedelta(hours=22)
    BOOST_SPEEDUP = 9  # 9x speed during boost

    remaining = upgrade_duration
    current_time = start_time
    cooldown = cooldown_left

    while remaining > timedelta(0):
        if cooldown <= timedelta(0):
            # Boost active: 22 minutes actual, but 22 * 9 = 198 minutes of upgrade time passed
            boost_upgrade_time = BOOST_DURATION * BOOST_SPEEDUP
            if remaining > boost_upgrade_time:
                # Boost covers part of upgrade
                remaining -= boost_upgrade_time
                current_time += BOOST_DURATION
                cooldown = COOLDOWN
            else:
                # Boost finishes upgrade early
                boost_real_time = remaining / BOOST_SPEEDUP
                current_time += boost_real_time
                remaining = timedelta(0)
        else:
            # No boost, normal speed until cooldown ends or upgrade finishes
            normal_duration = min(cooldown, remaining)
            current_time += normal_duration
            remaining -= normal_duration
            cooldown -= normal_duration
    return current_time


def main():
    print("Clash of Clans Upgrade Finish Time Calculator with OCR Image Input and Clock Tower Boost\n")
    image_dir = input("Enter path to folder with upgrade images: ").strip()
    if not os.path.isdir(image_dir):
        print("Invalid directory path.")
        return

    # Extract all upgrades from images
    extracted_upgrades = extract_upgrades_from_directory(image_dir)
    if not extracted_upgrades:
        print("No upgrades found in images.")
        return

    # Input Clock Tower cooldown left (hours minutes)
    while True:
        cooldown_str = input("Enter Clock Tower cooldown left (hours minutes, e.g. '0 0' if ready): ").strip()
        parts = cooldown_str.split()
        if len(parts) == 2 and all(p.isdigit() for p in parts):
            cooldown_left = timedelta(hours=int(parts[0]), minutes=int(parts[1]))
            break
        else:
            print("Please enter valid cooldown time in hours and minutes.")

    now = datetime.now()

    # Apply boost calculation to each upgrade
    upgrades_finish = []
    cooldown = cooldown_left
    for name, duration in extracted_upgrades:
        finish_time = apply_clock_tower_boost(now, duration, cooldown)
        upgrades_finish.append((name.title(), finish_time))
        # Update cooldown for next upgrade start: cooldown left after finishing this upgrade
        # Calculate cooldown left at finish time relative to now
        elapsed = finish_time - now
        # cooldown ticks down as time passes, max 0
        cooldown = max(timedelta(0), cooldown - elapsed)

    # Calculate next available boost time
    if cooldown_left <= timedelta(0):
        next_boost_time = now + timedelta(minutes=22) + timedelta(hours=22)
    else:
        next_boost_time = now + cooldown_left

    # Add clock tower info as special entry
    upgrades_finish.append(("[CLOCK TOWER]", next_boost_time))

    # Sort upgrades by finish time
    upgrades_finish.sort(key=lambda x: x[1])

    # Print nicely formatted schedule
    print("\n=== Upgrade Schedule ===")
    for name, finish in upgrades_finish:
        print(f"{name:20} ({finish.strftime('%b %d')}) {finish.strftime('%I:%M %p')}")


if __name__ == "__main__":
    main()
