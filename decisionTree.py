from node import Node
from tree import DecisionTree
from utils import get_majority_label, get_split_attribute_and_value


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

    print("begin split_data")
    split_attribute_index, split_attribute_value, s1, s2 = get_split_attribute_and_value(data)
    split_attribute = attribute_list[split_attribute_index]

    print("create decision tree")
    root_node = Node(index=0, attribute=split_attribute, attribute_idx=split_attribute_index, condition=split_attribute_value)
    tree = DecisionTree(root_node=root_node, attribute_list=attribute_list)
    # 递归生成所有节点
    tree.recurrent_node(data)

    return tree


# data = [
#     [1, 1, 1],
#     [1, 1, 1]
# ]
# attribute_list = ['A', 'B', 'C']

data = [
    ['yes', 'single', '125', 'no'],
    ['no', 'married', '100', 'no'],
    ['no', 'single', '70', 'no'],
    ['yes', 'married', '120', 'no'],
    ['no', 'divorced', '95', 'yes '],
    ['no', 'married', '60', 'no'],
    ['yes', 'divorced', '220', 'no'],
    ['no', 'single', '85', 'yes '],
    ['no', 'married', '75', 'no'],
    ['no', 'single', '90', 'yes ']

]
attribute_list = ['refund', 'marital', "income", "cheat"]

# data = [
#     ['1', 'A', 'no'],
#     ['1', 'A', 'no'],
#     ['1', 'C', 'no'],
#     ['2', 'C', 'Yes'],
# ]
# attribute_list = ['num', 'word', "cheat"]

# print(calculate_gini(data))
# print(get_split_attribute_and_value(data)[0], get_split_attribute_and_value(data)[1])

decision_tree = create_decision_tree(data, attribute_list)
decision_tree.show_tree()
