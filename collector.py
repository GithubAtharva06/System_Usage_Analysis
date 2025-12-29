import psutil
import time
import csv
from datetime import datetime

file_name = "data.csv"

try:
    with open(file_name, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "cpu_usage", "ram_usage"])
except FileExistsError:
    pass

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, cpu, ram])

    print(timestamp, cpu, ram)
    time.sleep(5)
 
 #This code was generated using chatgpt for collecting data of my system.
 #Although everything else was done by the author.