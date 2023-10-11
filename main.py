import fileinput
import os

# Data preprocess
print("Data preprocess begin --------------------")
outData = ""
inputFilePreprocess = 'data/adult.test'

for line in fileinput.input(files=inputFilePreprocess): # input data document
    lineSplit = line.split(",")
    lineStr = ""
    # print(lineSplit)

    if len(lineSplit) <15:  # remove lineSplit == "\n"
        continue

    for element in lineSplit:
        addFlag = True  # Determine whether to add the current row to the output data
        if element == " ?":  # whether containing '?',if containing '?', remove this record
            addFlag = False
            break
        if element != lineSplit[-2]:  # remove native-country
            if element == lineSplit[-1]:  # the last element does not add ,
                lineStr = lineStr + str(element)
            else:
                lineStr = lineStr + str(element) + ","

    if addFlag:
        outData = outData + lineStr
        # print(outData)

# Data Writing output file
inputFileName = os.path.basename(inputFilePreprocess)
inputDirectory = os.path.dirname(inputFilePreprocess)
outputFileName = inputFileName + ".preprocessed"
outputPath = os.path.join(inputDirectory, outputFileName)

outputFile = open(outputPath, "w")
outputFile.write(str(outData))
outputFile.close()
fileinput.close()
print("Data preprocess finished, the output data is store in", outputPath, "\n")

# Read data
print("Data Reading begin --------------------")
adultData = list()
inputFile = outputPath
for line in fileinput.input(files=inputFile):
    line_split = line.split(",")
    line_split[-1] = line_split[-1][:-3]
    adultData.append(line_split)
fileinput.close()
print("Data has ", len(adultData), " rows and ", len(adultData[0])," columns")


