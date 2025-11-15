class FileReaderIterator:
    def __init__(self, filename, lines_per_read):
        self.filename = filename
        self.lines_per_read = lines_per_read
        self.file = open(filename, "r")
    
    def __iter__(self):
        return self
    
    def __next__(self):
        lines = []
        # Read N lines
        for _ in range(self.lines_per_read):
            line = self.file.readline()
            if not line:  # End of file
                break
            lines.append(line.strip())
        
        if not lines:
            self.file.close()
            raise StopIteration
        
        return lines
reader = FileReaderIterator("example.txt", 3)

for chunk in reader:
    print(chunk)
