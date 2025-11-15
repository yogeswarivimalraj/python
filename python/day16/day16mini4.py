class BatchDataIterator:
    def __init__(self, data_source, batch_size):
        """
        data_source : any iterable (file, list, database results, etc.)
        batch_size  : number of records per batch
        """
        self.data_source = data_source
        self.batch_size = batch_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        """Read the next batch of N records"""
        batch = []

        
        for _ in range(self.batch_size):
            if self.index >= len(self.data_source): 
                break
            batch.append(self.data_source[self.index])
            self.index += 1

        if not batch: 
            raise StopIteration
        
        return batch

data = [
    {"id": 1, "name": "A"},
    {"id": 2, "name": "B"},
    {"id": 3, "name": "C"},
    {"id": 4, "name": "D"},
    {"id": 5, "name": "E"},
]

processor = BatchDataIterator(data, batch_size=2)

for batch in processor:
    print("Processing:", batch)
