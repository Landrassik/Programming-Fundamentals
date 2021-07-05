File_name, File_extension = "".join([i for i in input().split("\\") if "." in i]).split(".")
print(f"File name: {File_name}")
print(f"File extension: {File_extension}")