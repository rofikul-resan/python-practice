import os

# show all file  and folder using os module

directory_path="/"
file_and_dirs= os.listdir(directory_path)

# list the all dirs using loop
for item in file_and_dirs:
    print(item)
