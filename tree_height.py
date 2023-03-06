# python3
#221RDB376 Maksims Jakusevs 17.grupa

import sys
import threading
import numpy


def path_to_root(node, parents, node_visited_statuses, node_paths_to_root):

    if parents[node] == -1:
        return 1
    else:
        if node_visited_statuses[parents[node]]:
            return 1 + node_paths_to_root[parents[node]]
        else:
            node_paths_to_root[node] = 1 + path_to_root(parents[node], parents, node_visited_statuses, node_paths_to_root)
            node_visited_statuses[node] = True
            return node_paths_to_root[node]
        

def compute_height(n, parents):
    max_height = 0
    node_paths_to_root = numpy.zeros(n)
    node_visited_statuses = numpy.full(n, False)

    for i in range(n):
        node_paths_to_root[i] = path_to_root(i, parents, node_visited_statuses, node_paths_to_root)

    max_path = node_paths_to_root[0]
    for node_path_to_root in node_paths_to_root[1:]:
        if node_path_to_root > max_path:
            max_path = node_path_to_root

    max_height = int(max_path)
    return max_height


def main():
    in_type = input()

    if "i" in in_type.lower():
        node_count = int(input())
        parent_input = str(input())
        parent_list = [int(num) for num in parent_input.split(" ")]
        print(compute_height(node_count, parent_list))

    elif "f" in in_type.lower():
        file_name = str(input())
        path = "test/" + file_name
        if not "a" in path:
            with open(path, 'r') as file:
                node_count = int(file.readline())
                parent_input = str(file.readline())
                parent_list = [int(num) for num in parent_input.split(" ")]
                print(compute_height(node_count, parent_list))


sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()