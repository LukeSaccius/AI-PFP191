from datetime import datetime

def read_temperature_data(filename):
    """Read temperature data from a file and return a list of (datetime, temperature) tuples."""
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = []
        for i in range(0, len(lines), 2):
            timestamp = datetime.strptime(lines[i].strip(), '%d-%m-%Y %H:%M:%S')
            temperature = float(lines[i + 1].strip())
            data.append((timestamp, temperature))
        return data

def calculate_average_temperatures(data):
    """Calculate the average temperatures for the day, morning (5h-15h59), and evening (16h-21h59)."""
    daily_temps = []
    morning_temps = []
    evening_temps = []
    
    for timestamp, temperature in data:
        daily_temps.append(temperature)
        if 5 <= timestamp.hour <= 15:
            morning_temps.append(temperature)
        elif 16 <= timestamp.hour <= 21:
            evening_temps.append(temperature)
    
    average_daily = round(sum(daily_temps) / len(daily_temps), 3)
    average_morning = round(sum(morning_temps) / len(morning_temps), 3) if morning_temps else 0
    average_evening = round(sum(evening_temps) / len(evening_temps), 3) if evening_temps else 0
    
    return average_daily, average_morning, average_evening

def main():
    filename = 'temp.txt'  # Ensure this file is in the same directory as this script, or provide the full path
    data = read_temperature_data(filename)
    average_daily, average_morning, average_evening = calculate_average_temperatures(data)
    
    print(f"Average daily temperature: {average_daily}")
    print(f"Average morning temperature (5h00 to 15h59): {average_morning}")
    print(f"Average evening temperature (16h00 to 21h59): {average_evening}")

# The main method call
main()
