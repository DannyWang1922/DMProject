from node import Node

from utils import get_split_attribute_and_value


class DecisionTree:
    def __init__(self, root_node, attribute_list):
        self.root_node = root_node
        self.num_node = 0
        self.attribute_list = attribute_list
        self.node_list = []

    def recurrent_node(self, data):

        last_column = [row[-1] for row in data]
        # print("last_column ", last_column)

        # 如果所有样本都属于同一label，则将当前节点标记为叶节点，并设置类别标签
        if len(set(last_column)) == 1:
            node = Node(self.num_node, label=last_column[0])
            self.node_list.append(node)
            self.num_node = self.num_node + 1
            return node
        # print("data:", data)

        split_attribute_index, split_attribute_value, s1, s2 = get_split_attribute_and_value(data)
        split_attribute = self.attribute_list[split_attribute_index]

        if self.num_node == 0:
            node = self.root_node
        else:
            node = Node(index=self.num_node, attribute=split_attribute, attribute_idx=split_attribute_index, condition=split_attribute_value)

        # print("index: ", self.num_node, "split_attribute: ", node.attribute, "split_attribute_value: ",
        #       node.split_condition)
        # print("s1", s1)
        # print("s2", s2)
        # print("")

        # if self.num_node != 0:
        #     node.get_info()

        self.node_list.append(node)
        self.num_node = self.num_node + 1
        # input_node.left_node(self.recurrent_node(node, s1))
        # input_node.right_node(self.recurrent_node(node, s2))

        node.left_node = self.recurrent_node(s1)
        node.right_node = self.recurrent_node(s2)

        return node

    def show_tree(self):
        for node in self.node_list:
            node.get_info()


