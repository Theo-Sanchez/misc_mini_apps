def set_current_node(visited, currentDistances):
    # visited is a set that contains the names of the nodes marked as visited. E.g. {'A', 'C'}.
    # currentDistances is a dictionary that contains the current minimum distance of each node. E.g. {'A': 0, 'B': 3, 'C': 5}
    for k,v in sorted(currentDistances.items(), key=lambda item: item[1]):
        if k not in visited:
            return k
    return 'all nodes are already visited'
    # for key,val in currentDistances.items():
    #     if key not in visited:
    #         if val < to_visit['test']:
    #             to_visit['test'] = val
    #             to_visit['next'] = key
    # return to_visit['next'] #fix me: return the label of the node that should be set as "current node".


currentDistances = {'A': 9, 'B': 3, 'C': 10, 'D': 3, 'E': 8}
visited = {'A', 'C'}
print(set_current_node(visited, currentDistances))

# sorted_t = sorted(nodes.items(), key=lambda item:item[1])
# print(sorted_t)

nodes = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 7, 'D': 5, 'E': 1},
    'C': {'A': 1, 'B': 7, 'D': 2},
    'D': {'B': 5, 'C': 2, 'E': 7},
    'E': {'B': 1, 'D': 7}
} # AC : 1, AB: 3, ACD: 3, ABE : 4

# AB: 3
#     ABC: 10
#         ABCD: 12
#             ABCDE: 19
#     ABD: 8
#         ABDC: 10
#         ABDE: 15
#     ABE: 4
#         ABED: 11
# AC: 1,
#     ACB: 8,
#         ACBD: 13
#             ACBDE: 20
#         ACBE: 9
#             ACBED: 16
#     ACD: 3,
#         ACDB: 8
#             ACDBE: 9
#         ACDE: 10
#             ACDEB: 11



def init_nodes(current, nodes):

    distance = {}
    for key in nodes.keys():
        distance[key] = 0 if key == current else float('inf')
    return distance
# distances = []
# for elem in nodes.keys():
#     distances += [init_nodes(elem, nodes)]

distance = init_nodes('A', nodes)
print(distance)



# 1.    Mark your selected initial node with a current distance of 0 and the rest with infinity.
# 2.    Set the non-visited node with the smallest current distance as the current node C.
# 3.    For each neighbour N of your current node C:
    #       add the current distance of C with the weight of the edge connecting C-N.
    #       If it's smaller than the current distance of N, set it as the new current distance of N.
# 4.    Mark the current node C as visited.
# 5.    If there are non-visited nodes, go to step 2.