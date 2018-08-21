import atexit
dir(atexit)
print(dir(atexit))

with open("Output.txt", "w") as text_file:
    print(f"In this module we can find: " + str(dir(atexit)), file=text_file)