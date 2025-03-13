class FileHandler(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

# Define the concrete class TextFileHandler
class TextFileHandler(FileHandler):
    def read(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"File '{self.file_path}' not found."

    def write(self, data):
        with open(self.file_path, 'w') as file:
            file.write(data)

# Define the concrete class BinaryFileHandler
class BinaryFileHandler(FileHandler):
    def read(self):
        try:
            with open(self.file_path, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            return f"File '{self.file_path}' not found."

    def write(self, data):
        with open(self.file_path, 'wb') as file:
            file.write(data)

# Create instances of the concrete classes
text_handler = TextFileHandler('example.txt')
binary_handler = BinaryFileHandler('example.bin')

# Use the read() and write() methods
text_data = "Hello, World!"
text_handler.write(text_data)
print(text_handler.read())

binary_data = b"Hello, World!"
binary_handler.write(binary_data)
print(binary_handler.read())
