class Node:
    def __init__(self, index=None, attribute=None, attribute_idx=None,
                 condition=None, left_node=None, right_node=None, label=None):
        self.index = index
        self.attribute = attribute
        self.attribute_idx = attribute_idx
        self.split_condition = condition
        self.left_node = left_node
        self.right_node = right_node
        self.label = label

    def get_info(self):
        if (self.left_node is None) or (self.right_node is None):
            print("index:", self.index, "attribute:", self.attribute, "attribute_idx:", self.attribute_idx, "condition:", self.split_condition,
                  "label:", self.label)
        elif self.right_node is None:
            print("index:", self.index, "attribute:", self.attribute, "attribute_idx:", self.attribute_idx, "condition:", self.split_condition,
                  "label:", self.label, "left:", self.left_node.index)
        elif self.left_node is None:
            print("index:", self.index, "attribute:", self.attribute, "attribute_idx:", self.attribute_idx, "condition:", self.split_condition,
                  "label:", self.label, "right:", self.right_node.index)
        else:
            print("index:", self.index, "attribute:", self.attribute, "attribute_idx:", self.attribute_idx, "condition:", self.split_condition,
                  "label:", self.label, "left:", self.left_node.index,
                  "right:", self.right_node.index)






if __name__ == "__main__":
    node = Node(1, "good", '1')
    node.get_info()
