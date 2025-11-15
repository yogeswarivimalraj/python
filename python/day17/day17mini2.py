def log_reader(filename, keyword=None):
   
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if keyword:
                if keyword in line:
                    yield line
            else:
                yield line

for entry in log_reader("system.txt"):
    print(entry)

    
# for entry in log_reader("system.txt", keyword="WARNING"):
#     print(entry)

