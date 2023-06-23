import os
inputs = []
lines_per_file = 20
chunkfile = None
with open('D:\\lazard\\mongoDb\\DATABASE.txt') as mf:
    for line_no, line in enumerate(mf):
        if line_no % lines_per_file == 0:
            if chunkfile:
                chunkfile.close()
            chunk_filename = 'Split_file_{}.txt'.format(line_no + lines_per_file)
            chunkfile = open(chunk_filename, "w")
        chunkfile.write(line)
    if chunkfile:
        chunkfile.close()
for i in os.listdir("D:\\lazard\\mongoDb\\SplitAndMerge"):   # read folder
    if i.endswith(".txt"):
        inputs.append(os.path.join("D:\\lazard\\mongoDb\\SplitAndMerge", i))
with open('split_merged_file.txt', 'w') as of:    # concatanate , merge all txt files
    for j in inputs:
        with open(j, encoding="utf-8", errors='ignore') as file:
            of.write(file.read())

