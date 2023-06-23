import os

# find all the txt files in the dataset folder
inputs = []
for file in os.listdir("D:\lazard\mongoDb\SplitAndMerge"):
    if file.endswith(".txt"):
        inputs.append(os.path.join("D:\lazard\mongoDb\SplitAndMerge", file))

# concatanate all txt files in a file called merged_file.txt
with open('merged_file.txt', 'w') as outfile:
    for fname in inputs:
        with open(fname, encoding="utf-8", errors='ignore') as infile:
            outfile.write(infile.read())

