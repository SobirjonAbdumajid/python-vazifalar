# 1
class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file {self.file_name} in {self.mode} mode.")
        self.file = open(self.file_name, self.mode)
        return self.file  # with bloki ichida ishlatish uchun

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing file {self.file_name}.")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return False  # Xatoni qayta ko'taradi

with FileManager("example.txt", "r") as file:
    content = file.read()
    print(content)  # F



# # 2
# from contextlib import contextmanager

# @contextmanager
# def open_file(file_name, mode):
#     file = open(file_name, mode)
#     try:
#         yield file
#     finally:
#         file.close()

# # Foydalanish
# with open_file("example.txt", "w") as file:
#     file.write("Hello, with contextlib!")
