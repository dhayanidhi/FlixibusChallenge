from collections import namedtuple

class Node(object):

    def __init__(self, row_object):
        self.row_object = row_object
        self.node_left = None
        self.node_right = None

    def set_node_left(self, node):
        self.node_left = node

    def set_node_right(self, node):
        self.node_right = node


def execute_model(stream_list):
    """
    Dummy function to replace machine learning model
    :param stream_list:
    :return:
    """
    ids = [obj.id for obj in stream_list]
    ids.sort(reverse=True)
    return ids

def _compare_node(node1, node2):
    """
    Compare node1 and node2
    :param node1:
    :param node2:
    :return:
    """
    cmp_list = [node1.row_object, node2.row_object]
    res = execute_model(cmp_list)
    if node1.row_object.id == res[0]:
        # node2 is small
        if node1.node_left:
            _compare_node(node1.node_left, node2)
        else:
            node1.set_node_left(node2)
    else:
        # node2 is big
        if node1.node_right:
            _compare_node(node1.node_right, node2)
        else:
            node1.set_node_right(node2)

def _run(stream_list):
    """
    Execute model and compare adjacent node
    :param stream_list:
    :param split:
    :return:
    """
    root = Node(stream_list[0])

    for each_item in stream_list[1:]:
        node = Node(each_item)
        _compare_node(root, node)
    return root

def _traverse_depth_first_search_node(node, stack):
    """
    Traverse binary tree and collect the sorted result
    :param node:
    :param stack:
    :return:
    """

    if node.node_left:
        _traverse_depth_first_search_node(node.node_left, stack)

    stack.append(node.row_object.id)

    if node.node_right:
        _traverse_depth_first_search_node(node.node_right, stack)


def get_sorted_result(features_list):
    row_obj_dict = namedtuple('row_object', ["id", "feature1", "feature2"])
    row_object_list = [row_obj_dict(**feature) for feature in features_list]
    if len(row_object_list) <= 5:
        return execute_model(row_object_list)

    root = _run(row_object_list)
    output_list = []
    _traverse_depth_first_search_node(root, output_list)
    output_list.sort(reverse=True)
    return output_list
