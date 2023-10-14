from node import Node
from tree import DecisionTree
from utils import get_majority_label, get_split_attribute_and_value
from dataPreprocess import data_preprocess, saveData, loadData
import sys

sys.setrecursionlimit(100000)

def create_decision_tree(data, attribute_list):
    """创建决策树"""
    label_list = [sample[-1] for sample in data]
    # print(label_list)
    attribute_list = attribute_list

    # 所有样本属于同一类别，返回该类别
    if all(label == label_list[0] for label in label_list):
        print("All samples belong to the same class")
        return label_list[0]

    print("All samples do not belong to the same class")

    # 所有样本value相同，或者S的数量过少
    flag = False
    for arr in range(len(attribute_list)):
        for i in range(len(data)):
            if data[arr][i] != data[0][0]:
                flag = True
                break
            if (data[arr][i] == data[-1][-1] == data[0][0]) or len(data[arr]) == 1:
                return get_majority_label(label_list)
        if flag:
            break

    tree = DecisionTree(attribute_list=attribute_list)

    print("Recursively generate all nodes")
    tree.recurrent_node(data)

    return tree


attribute_list = [
    'age', 'workclass', "fnlwgt", "education", "education-num", "marital-status", "occupation",
    "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "income"
]

print("Training data preprocess ------------------------------------------")
preprocessedData = data_preprocess(inputFile='data/adult.data')
saveData(preprocessedData, 'data/adult.clean_data')  # save  preprocessed data

adultDataTrain = loadData(inputFile='data/adult.clean_data')  # loadData

print("Built decision tree------------------------------------------")
decision_tree = create_decision_tree(adultDataTrain, attribute_list)

print("Save decision tree to txt file------------------------------------------")
tree_txt = str(decision_tree.save_tree())
with open('tree.txt', 'w') as f:
    f.write(tree_txt)

print("Testing data preprocess------------------------------------------")
preprocessedData = data_preprocess(inputFile='data/adult.test')
saveData(preprocessedData, 'data/adult.clean_test')

adultDataTest = loadData(inputFile='data/adult.clean_test')


print("Loading tree from file------------------------------------------")
with open('tree.txt', 'r') as f:
    obj_str = f.read()
    tree_list = eval(obj_str)
decision_tree = DecisionTree.load_tree(tree_list, attribute_list)


print("run decision tree on test set------------------------------------------")
num_obj, num_correct, corr_rate = decision_tree.classify_dataset(adultDataTest)

print("The num of data set:", num_obj, " Number of correctly classified samples:", num_correct,
      " Classification accuracy:", corr_rate)
