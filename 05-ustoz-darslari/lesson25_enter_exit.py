# # 1
# class FileManager:
#     def __init__(self, file_name, mode):
#         self.file_name = file_name
#         self.mode = mode
#         self.file = None

#     def __enter__(self):
#         print(f"Opening file {self.file_name} in {self.mode} mode.")
#         self.file = open(self.file_name, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         print(f"Closing file {self.file_name}.")
#         if self.file:
#             self.file.close()
#         if exc_type:
#             print(f"An error occurred: {exc_value}")
#         return False

# 2 
# with FileManager("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# 1
# file_manager = FileManager("example1.txt", "w")

# file = file_manager.__enter__()
# try:
#     file.write("hi")
# finally:
#     file_manager.__exit__(None, None, None)


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


# # 3
# class Open:
#     def __init__(self, file_name, file_mode):
#         self.file_name = file_name
#         self.file_mode = file_mode
#         self.file = None
        
#     def __enter__(self):
#         print('open')
#         self.file = open(self.file_name, self.file_mode)
#         return self.file
    
#     def __exit__(self, a, b, c):
#         self.file.close()
#         print("done")
#         return False
    
# with Open("good.txt", "w") as file:
#     file.write("somsa")
        