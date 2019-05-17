with open("index.rst") as fp:
    while line := fp.readline():
        print(len(line))
