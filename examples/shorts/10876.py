# Custom iterator to loop over file lines with batch processing
class FileBatchIterator:
    def __init__(self, file_path: str, batch_size: int = 5):
        self.file_path = file_path
        self.batch_size = batch_size
        self._file = None  # File handle placeholder
        self._buffer = []  # Internal buffer to store lines

    def __iter__(self):
        self._file = open(self.file_path, 'r')
        return self

    def __next__(self):
        # If buffer is empty, refill it with the next batch of lines
        if not self._buffer:
            self._buffer = [self._file.readline().strip() for _ in range(self.batch_size)]
            self._buffer = [line for line in self._buffer if line]  # Filter empty lines

        # StopIteration if buffer is empty after reading the file
        if not self._buffer:
            self._file.close()
            raise StopIteration

        # Return the next line from the buffer
        return self._buffer.pop(0)

# Example usage
file_iterator = FileBatchIterator('/tmp/test/input.txt', batch_size=3)
for line in file_iterator:
    print(line)