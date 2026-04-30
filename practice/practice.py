from pathlib import Path

#https://docs.python.org/3/library/pathlib.html

#============================================================ create a file ==================================================

# myFile = Path("my_file.txt")
# myFile.touch()
# myFile.write_text("Hello from the first file text using pathlib")
# print(myFile.stat())
# print(Path.cwd()) # returns the ABSOLUTE path [D:\university\Programming_and_algo\Python\eleventh_lab]

#============================================================ create files ==================================================
# for item in range(1,6):
#     file = Path(f'myPyFile{item}.py')
#     file.write_text(f"print('Hello from file number {item} ')")

#============================================================ delete files ==================================================

# for item in range(1,6):
#     file = Path(f'myPyFile{item}.py')
#     file.unlink()

#============================================================ create a file in a given directory ==================================================
# test = Path("test")
# newFile = test /'newTest.txt'
# newFile.touch()
# newFile.write_text(newFile.read_text() +"\nthis is the eleventh lab")
# newFile.write_text(newFile.read_text() + "\nBut this is just a practice\n") #write without deleting the previous content

# print(newFile.read_text())
#============================================================ create a folder ==================================================

# path = Path("D:/university/Programming_and_algo/Python/eleventh_lab/test")
# path = Path("test2")
# path.mkdir()
# print(path)

# print(dir(Path()))

# test = Path("test")
# print(f"info: {test.info}")
# print(f"stat: {test.stat()}")
# print(f"parent: {test.parent}")

# test = Path("my_file.txt")
# print(f"info: {test.info}")
# print(f"stat: {test.stat()}")
# print(f"parent: {test.parent}")


