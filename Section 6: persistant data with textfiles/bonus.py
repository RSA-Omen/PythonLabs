content = ["content one", "content two", "content three"]
filenames = ["file1.txt", "file2.txt", "file3.txt"]
for content, filename in zip(content, filenames):
    with open(f"files/{filename}", "w") as file:
        file.write(content) 