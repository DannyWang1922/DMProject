import fileinput

attribute_list = [
    'age', "fnlwgt",  "education-num", "capital-gain", "capital-loss", "hours-per-week", "income"
]

with open('tree.txt', 'r') as f:
    obj_str = f.read()
    node_list = eval(obj_str)

def saveData(data, outPath):
    """Save data to txt file"""
    outputFile = open(outPath, "w")
    outputFile.write(str(data))
    outputFile.close()
    fileinput.close()

def printTree(node):
    if node is not None:
        if node['left'] is not None: # Check if 'left' key exists
            printTree(node_list[node['left']])

        ## print node
        if node['left'] is None and node['right'] is None: # leaf node
            print(' ' * 5 * node['layer'] + '#', f"index: {node['index']}", f"layer: {node['layer']}",f"label: {node['label']}")
        elif node['attribute'] in attribute_list: # node
            print(' ' * 5 * node['layer'] + '=>', f"index: {node['index']}", f"layer: {node['layer']}",f"attribute: {node['attribute']}: {node['split_condition']}",  f"left: <={node['split_condition']} {node['left']}", f"right: >{node['split_condition']} {node['right']}")
        else:
            print(' ' * 5 * node['layer'] + '=>', f"index: {node['index']}", f"layer: {node['layer']}",f"attribute: {node['attribute']}: {node['split_condition']}",  f"left: ={node['split_condition']} {node['left']}", f"right: !={node['split_condition']} {node['right']}")

        if node['right'] is not None:  # Check if 'right' key exists
            printTree(node_list[node['right']])
printTree(node_list[0])
