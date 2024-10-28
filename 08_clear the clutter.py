import os

os.chdir("D:/Files")
directory = os.getcwd()
try:
    i = 0
    for filename in os.listdir():
        if filename.endswith('.png'):
            i += 1
            new_name = (f"image {i}.png")

            new_file = os.path.join(directory, new_name)
            old_file = os.path.join(directory, filename)

            os.rename(old_file, new_file)
except:
    print("Files already has been renamed.")

try:
    x = 0
    for filename in os.listdir():
        if filename.endswith('.pdf'):
            x += 1
            new_name = (f"PDF {x}.pdf")

            new_file = os.path.join(directory, new_name)
            old_file = os.path.join(directory, filename)

            os.rename(old_file, new_file)
except:
    print("Files already has been renamed.")

