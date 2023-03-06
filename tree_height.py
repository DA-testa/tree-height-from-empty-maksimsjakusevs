# python3
#221RDB376 Maksims Jkusevs 17.grupa

import sys
import threading
import numpy


def path_root(node, parents, statuses, root):
    
    if parents[node] == -1:
        return 1
    
    else:
        if statuses[parents[node]]:
            return 1 + root[parents[node]]
        
        else:
            root[node] = 1 + path_root(parents[node], parents, statuses, root)
            statuses[node] = True
            return root[node]
        

def compute_height(n, parents):
    max_height = 0
    root = numpy.zeros(n)
    statuses = numpy.full(n, False)

    for i in range(n):
        root[i] = path_root(i, parents, statuses, root)
    max_path = root[0]
    
    for root in root[1:]:
        if root > max_path:
            max_path = root
    max_height = int(max_path)

    return max_height


def main():
    type = input()

    if "i" in type.lower():
        count = int(p_input())
        p_input = str(p_input())
        list = [int(num) for num in p_input.split(" ")]
        print(compute_height(count, list))

    elif "f" in type.lower():
        file_name = str(p_input())
        path = "test/" + file_name

        if not "a" in path:
            with open(path, 'r') as file:
                count = int(file.readline())
                p_input = str(file.readline())
                list = [int(num) for num in p_input.split(" ")]
                print(compute_height(count, list))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()