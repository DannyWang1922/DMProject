import fileinput


def data_preprocess(inputFile):
    """Data preprocess"""
    outData = ""
    for line in fileinput.input(files=inputFile):  # input data document
        lineSplit = line.split(",")
        lineStr = ""
        # print(lineSplit)

        if len(lineSplit) < 15:  # remove lineSplit == "\n"
            continue

        for element in lineSplit:
            addFlag = True  # Determine whether to add the current row to the output data
            if element == " ?":  # whether containing '?',if containing '?', remove this record
                addFlag = False
                break
            if element != lineSplit[-2]:  # remove native-country
                if element == lineSplit[-1]:  # the last element does not add ,
                    if "." in element:  # remove . of test set
                        element = element.replace(".", "")
                    lineStr = lineStr + str(element)
                else:
                    lineStr = lineStr + str(element) + ","

        if addFlag:
            outData = outData + lineStr
            # print(outData)
    return outData


def saveData(data, outPath):
    """Save data to txt file"""
    outputFile = open(outPath, "w")
    outputFile.write(str(data))
    outputFile.close()
    fileinput.close()


def loadData(inputFile):
    """Load data from txt file"""
    adultData = list()
    for line in fileinput.input(files=inputFile):
        line_split = line.split(",")
        line_split[-1] = line_split[-1][:-1]
        adultData.append(line_split)
    fileinput.close()

    print("Data has ", len(adultData), " rows and ", len(adultData[0]), " columns")
    return adultData


if __name__ == "__main__":
    preprocessedData = data_preprocess(inputFile='data/adult.data')
    saveData(preprocessedData, 'data/adult.data.testversion')
    adultData = loadData(inputFile='data/adult.data.testversion')
    print("======================================================")
    print(adultData)
