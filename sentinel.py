import hashlib
import time
from datetime import datetime

# files that the program will monitor
files = ["config.sys", "users.db", "firewall_rules.txt"]

# creates the files only if they do not already exist
def create_files():
    sample_data = {
        "config.sys": "system=active",
        "users.db": "demo_user",
        "firewall_rules.txt": "DENY ALL",
    }

    for filename in files:
        try:
            file = open(filename, "x")
            file.write(sample_data[filename])
            file.close()
        except FileExistsError:
            pass

# function to get the hash of a file
def get_file_hash(filename):
    try:
        hash_value = hashlib.sha256()
        file = open(filename, "rb")
        for line in file:
            hash_value.update(line)
        file.close()
        return hash_value.hexdigest()
    except FileNotFoundError:
        return None

create_files()
print("Files are ready.")

# saves the first hash of each file
baseline = {}
for filename in files:
    baseline[filename] = get_file_hash(filename)

print("Baseline saved.")
print("Sentinel is watching for file changes...")
print("Press Ctrl+C to stop the program.")

try:
    while True:
        time.sleep(5)
        for filename in files:
            current_hash = get_file_hash(filename)
            if current_hash != baseline[filename]:
                current_time = datetime.now()
                if current_hash is None:
                    message = filename + " was deleted"
                elif baseline[filename] is None:
                    message = filename + " was restored"
                else:
                    message = filename + " was modified"
                print("!!! RED ALERT !!!")
                print(message)
                print("Time of change:", current_time)
                log_file = open("incident_report.log", "a")
                log_file.write(str(current_time) + " - " + message + "\n")
                log_file.close()
                # updates the hash so the same warning does not repeat
                baseline[filename] = current_hash
except KeyboardInterrupt:
    print("\nSentinel stopped.")
