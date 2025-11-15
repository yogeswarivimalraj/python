def filter_log_entries(filename):
    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line or "WARNING" in line:
                yield line.strip()   
for log in filter_log_entries("log.txt"):
    print(log)
