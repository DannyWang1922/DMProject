def calculate_gini(data):
    """计算数据集的GINI指数"""
    num_obj = len(data)
    label_count = {}
    for obj in data:
        label = obj[-1]
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
    # print('calculate_gini Function: label_count:', label_count)

    gini = 1.0
    for count_obj in label_count.values():
        p = count_obj / num_obj
        gini = gini - p ** 2
    return gini


def get_majority_label(labels):
    """多数表决，选择出现次数最多的类别"""
    label_count = {}
    for label in labels:
        if label not in label_count:
            label_count[label] = 0
        label_count[label] = label_count[label] + 1
    # print('majority_label Function: label_count: ', label_count)

    label_sorted = sorted(label_count.items(), key=lambda x: x[1], reverse=True)
    majority_label = label_sorted[0][0]
    # print('majority_label Function: majority_label: ', majority_label)
    return majority_label


def split_data(data, attribute_index, attribute_value):
    """根据特征值划分数据集"""
    s1 = []
    s2 = []
    if attribute_value.isnumeric():  # Nominal Attribute
        for obj in data:
            # print(obj[attribute_index], attribute_value, (obj[attribute_index] <= attribute_value))
            if float(obj[attribute_index]) <= float(attribute_value):
                s1.append(obj)
            else:
                s2.append(obj)

    else:  # Ordinal Attribute
        for obj in data:
            if obj[attribute_index] == attribute_value:
                s1.append(obj)
            else:
                s2.append(obj)

    # print("attribute_value: ", attribute_value)
    # print("s1:", s1)
    # print("s2:", s2)
    return s1, s2


def get_split_attribute_and_value(data):
    """选择最佳划分特征"""
    num_attributes = len(data[0])
    min_attribute_gini = 1
    best_split_attribute_index = 0
    best_split_attribute_value = None
    best_split_s1 = None
    best_split_s2 = None

    # loop all attributes
    for attribute in range(num_attributes - 1):
        attribute_values = [obj[attribute] for obj in data]
        attribute_values = set(attribute_values)  # 去掉一个属性中相同的值
        # print("attribute: ", attribute)

        # loop all values of one attribute
        min_value_gini = 1
        temp_split_value = None
        temp_split_s1 = None
        temp_split_s2 = None
        for value in attribute_values:

            s1, s2 = split_data(data, attribute, value)
            prob = len(s1) / len(data)
            value_gini = prob * calculate_gini(s1) + (1 - prob) * calculate_gini(s2)

            # find the smallest gini value of one attribute
            if value_gini < min_value_gini:
                min_value_gini = value_gini  # smallest gini value
                temp_split_value = value  # split value of current attribute
                temp_split_s1 = s1
                temp_split_s2 = s2


        attribute_gini = min_value_gini
        attribute_split_value = temp_split_value
        attribute_split_s1 = temp_split_s1
        attribute_split_s2 = temp_split_s2
        # print("attribute_gini: ", attribute_gini, "min_attribute_gini: ", min_attribute_gini)
        # print("attribute_split_value: ", attribute_split_value, "temp_split_value: ", temp_split_value)

        # Compare the minimum gini value of the current attribute with previous attribute
        if attribute_gini < min_attribute_gini:
            min_attribute_gini = attribute_gini
            best_split_attribute_index = attribute
            best_split_attribute_value = attribute_split_value
            best_split_s1 = attribute_split_s1
            best_split_s2 = attribute_split_s2
            # print("best_split_attribute_index:", best_split_attribute_index, "best_split_attribute_value: ",
            #       best_split_attribute_value)
            # print(best_split_s1)
            # print(best_split_s2)

    return best_split_attribute_index, best_split_attribute_value, best_split_s1, best_split_s2