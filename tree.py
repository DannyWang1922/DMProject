from node import Node
from utils import get_split_attribute_and_value, get_majority_label, remove_zeros


class DecisionTree:
    def __init__(self, root_node=None, attribute_list=None):
        self.root_node = root_node
        self.num_node = 0
        self.attribute_list = attribute_list
        self.node_list = []

    def recurrent_node(self, data):
        """ Generate decision tree nodes recursively """

        if len(remove_zeros(data[0])) == 1:  # Remove attributes that have been classified by remove_zeros function
            # print("=========================================", data)
            node = Node(self.num_node, label=get_majority_label([row[-1] for row in data]))
            self.node_list.append(node)
            self.num_node = self.num_node + 1
            return node

        # If all object belong to the same label, mark the current node as a leaf node and set a category label
        last_column = [row[-1] for row in data]
        if len(set(last_column)) == 1:
            node = Node(self.num_node, label=last_column[0])
            self.node_list.append(node)
            self.num_node = self.num_node + 1
            return node

        split_attribute_index, split_attribute_value, s1, s2 = get_split_attribute_and_value(data)
        split_attribute = self.attribute_list[split_attribute_index]

        # Any set of s1 or s2 is null
        if (len(remove_zeros(s1)) == 0) or (len(remove_zeros(s2)) == 0):
            if len(remove_zeros(s1)) == 0:
                node = Node(self.num_node, label=get_majority_label([row[-1] for row in s2]))
            if len(remove_zeros(s2)) == 0:
                node = Node(self.num_node, label=get_majority_label([row[-1] for row in s1]))
            self.node_list.append(node)
            self.num_node = self.num_node + 1
            return node

        node = Node(index=self.num_node, attribute=split_attribute, attribute_idx=split_attribute_index,
                    split_condition=split_attribute_value)

        # root node of decision tree
        if self.num_node == 0:
            self.root_node = node

        self.node_list.append(node)
        self.num_node = self.num_node + 1
        # print("index: ", self.num_node, "split_attribute: ", node.attribute, "split_attribute_value: ",
        #       node.split_condition)

        if self.num_node % 100 == 0:
            print(self.num_node, " nodes is generated")

        # Let the deleted attribute value be 0 to keep the original attribute dimension, and correspond to the attribute value
        s1 = [row[:split_attribute_index] + ["0"] + row[split_attribute_index + 1:] for row in s1]
        s2 = [row[:split_attribute_index] + ["0"] + row[split_attribute_index + 1:] for row in s2]

        node.left_node = self.recurrent_node(s1)
        node.right_node = self.recurrent_node(s2)

        return node

    def show_tree(self):
        for node in self.node_list:
            print(node.get_info())

    def classify(self, input):
        """classify the input single object"""
        obj = input[:-1]  # remove obj label
        current_node = self.root_node
        while current_node.label is None:
            if current_node.split_condition.isnumeric():  # Nominal Attribute
                if obj[current_node.attribute_idx] < current_node.split_condition:
                    current_node = current_node.left_node
                else:
                    current_node = current_node.right_node
            else:  # Ordinal Attribute
                if obj[current_node.attribute_idx] == current_node.split_condition:
                    current_node = current_node.left_node
                else:
                    current_node = current_node.right_node
        # print("current_node.label", current_node.label, "input[-1]", input[-1])
        if current_node.label == input[-1]:
            return True
        else:
            return False

    def classify_dataset(self, input_dataset):
        """classify the input dataset (object list)"""
        num_correct = 0
        for obj in input_dataset:
            res = self.classify(obj)
            if res:
                num_correct = num_correct + 1
        corr_rate = num_correct / len(input_dataset)
        return len(input_dataset), num_correct, corr_rate

    def get_tree_list(self):
        """get the list of all decision tree nodes"""
        tree_list = []
        for node in self.node_list:
            tree_list.append(node.get_info())
        return tree_list

    @staticmethod
    def load_tree(node_list, attribute_list):
        """load tree from the input node list"""
        tree = DecisionTree(attribute_list=attribute_list)
        tree.attribute_list = attribute_list
        tree.node_list = [None] * len(node_list)

        # Traverse all nodes in reverse order
        # Let the left and right nodes of the node be generated before this node
        node_list.reverse()
        for node in node_list:
            node_new = Node(index=node.get("index"), attribute=node.get("attribute"),
                            attribute_idx=node.get("attribute_idx"),
                            split_condition=node.get("split_condition"), label=node.get("label"),
                            left_node=None if node.get("left") is None else tree.node_list[node.get("left")],
                            right_node=None if node.get("right") is None else tree.node_list[node.get("right")])
            tree.node_list[node_new.index] = node_new
            tree.num_node = tree.num_node + 1
            if node == node_list[-1]:
                tree.root_node = node_new
        return tree
