from node import Node
from tree import DecisionTree
from utils import get_majority_label, get_split_attribute_and_value
from dataPreprocess import data_preprocess, saveData, loadData
import sys
import time
import argparse

sys.setrecursionlimit(100000)

def create_decision_tree(data, attribute_list, max_layer):
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

    tree = DecisionTree(attribute_list=attribute_list, maxLayer=max_layer)

    print("Recursively generate all nodes")
    tree.recurrent_node(data, layer=0)

    return tree

# python main.py --model_mode train --training_set data/adult.data  --testing_set data/adult.test --max_layer 14
# python main.py --model_mode test --processed_testing_set data/adult.clean_test --tree tree.txt
parser = argparse.ArgumentParser()

parser.add_argument('--model_mode', type=str, default="train", help='Model mode, training mode or testing mode')
parser.add_argument('--training_set', type=str, default="data/adult.data", help='Input training set file')
parser.add_argument('--testing_set', type=str, default="data/adult.test", help='Input testing set file')
parser.add_argument('--processed_testing_set', type=str, default="data/adult.clean_test",
                    help='Input preprocessed testing set file')
parser.add_argument('--tree', type=str, default="tree.txt", help='tree model file')
parser.add_argument('--max_layer', type=int, default=15, help='Max Number of decision tree layers')

args = parser.parse_args()

attribute_list = [
    'age', 'workclass', "fnlwgt", "education", "education-num", "marital-status", "occupation",
    "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "income"
]

if args.model_mode == "train":
    print("Train mode ------------------------------------------")
    print("Training data preprocess ------------------------------------------")
    preprocessedData = data_preprocess(inputFile=args.training_set)
    saveData(preprocessedData, 'data/adult.clean_data')  # save preprocessed training data
    adultDataTrain = loadData(inputFile='data/adult.clean_data')  # load training Data

    start_time = time.time()
    print("Built decision tree------------------------------------------")
    decision_tree = create_decision_tree(adultDataTrain, attribute_list, args.max_layer)
    end_time = time.time()
    run_time = end_time - start_time
    print("Time for generating decision tree: ", run_time)

    print("Save decision tree to txt file------------------------------------------")
    tree_txt = str(decision_tree.get_tree_list())
    with open('tree.txt', 'w') as f:
        f.write(tree_txt)

    print("Testing dataset preprocess------------------------------------------")
    preprocessedData = data_preprocess(inputFile=args.testing_set)
    saveData(preprocessedData, 'data/adult.clean_test')  # save preprocessed testing data
    adultDataTest = loadData(inputFile="data/adult.clean_test")  # load test Data

else:  # test mode
    print("Test mode ------------------------------------------")
    print("Loading decision tree from file------------------------------------------")
    with open(args.tree, 'r') as f:
        obj_str = f.read()
        node_list = eval(obj_str)
    decision_tree = DecisionTree.load_tree(node_list, attribute_list)
    adultDataTest = loadData(inputFile=args.processed_testing_set)

print("Running decision tree on test set------------------------------------------")
num_obj, num_correct, corr_rate, correct_classify_str, mis_classify_str = decision_tree.classify_dataset(adultDataTest)

print("The num of data set:", num_obj, " Number of correctly classified samples:", num_correct,
      " Classification accuracy:", corr_rate)

with open('correct_classify.txt', 'w') as f:
    f.write(correct_classify_str)

with open('mis_classify.txt', 'w') as f:
    f.write(mis_classify_str)

