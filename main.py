from node import Node
from tree import DecisionTree
from utils import get_majority_label, get_split_attribute_and_value
from dataPreprocess import data_preprocess, saveData, loadData
import sys
import time
sys.setrecursionlimit(100000)


def create_decision_tree(data, attribute_list):
    """Create decision tree by input dataset and attribute list"""
    label_list = [sample[-1] for sample in data]
    # print(label_list)
    attribute_list = attribute_list

    # if all object belong to the same label type, return that label type
    if all(label == label_list[0] for label in label_list):
        print("All samples belong to the same class")
        return label_list[0]

    # All objects have the same value, or the number of S is too small
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

    tree = DecisionTree(attribute_list=attribute_list, maxLayer=14)

    print("Recursively generate all nodes")
    tree.recurrent_node(data, layer=0)

    return tree

attribute_list = [
    'age', 'workclass', "fnlwgt", "education", "education-num", "marital-status", "occupation",
    "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "income"
]

print("Training data preprocess ------------------------------------------")
preprocessedData = data_preprocess(inputFile='data/adult.data')
saveData(preprocessedData, 'data/adult.clean_data')  # save  preprocessed data

adultDataTrain = loadData(inputFile='data/adult.clean_data')  # loadData

start_time = time.time()
print("Built decision tree------------------------------------------")
decision_tree = create_decision_tree(adultDataTrain, attribute_list)
end_time = time.time()
run_time = end_time - start_time
print("Time for generating decision tree: ", run_time)

print("Save decision tree to txt file------------------------------------------")
tree_txt = str(decision_tree.get_tree_list())
with open('tree.txt', 'w') as f:
    f.write(tree_txt)

print("Loading decision tree from file------------------------------------------")
with open('tree.txt', 'r') as f:
    obj_str = f.read()
    node_list = eval(obj_str)
decision_tree = DecisionTree.load_tree(node_list, attribute_list)

print("Testing dataset preprocess------------------------------------------")
preprocessedData = data_preprocess(inputFile='data/adult.test')
saveData(preprocessedData, 'data/adult.clean_test')

adultDataTest = loadData(inputFile='data/adult.clean_test')


print("Running decision tree on test set------------------------------------------")
num_obj, num_correct, corr_rate, correct_classify_str, mis_classify_str = decision_tree.classify_dataset(adultDataTest)

print("The num of data set:", num_obj, " Number of correctly classified samples:", num_correct,
      " Classification accuracy:", corr_rate)

with open('correct_classify.txt', 'w') as f:
    f.write(correct_classify_str)

with open('mis_classify.txt', 'w') as f:
    f.write(mis_classify_str)
