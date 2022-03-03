
def get_graph_info(adj_list):
    loops = 0
    parrallel = False
    max_node_grade = 1

    y = ''.join([''.join([str(x) for x in elem]) for elem in adj_list])
    #adj_list is the adjacency list of a graph. It's a list of lists, with each element being the two nodes connected by an edge.
    #For example, if adj_list=[[0,1],[2,3],[4,3]], we have three edges, one connecting nodes 0 and 1, another one connecting nodes 2 and 3 and a third one connecting nodes 4 and 3.
    for i in range(len(adj_list)):
        if adj_list[i][0] == adj_list[i][1]:
            loops += 1
        else:
            if [adj_list[i][1], adj_list[i][0]] in adj_list[i:]:
                parrallel = True
        node_grade0 = y[i:].count(str(adj_list[i][0]))
        node_grade1 = y[i:].count(str(adj_list[i][1]))
        if node_grade0 > max_node_grade:
            max_node_grade = node_grade0
        if node_grade1 > max_node_grade:
            max_node_grade = node_grade1
        
    return max_node_grade, loops, parrallel #fix me: for the given graph, return: maximum grade of a node, number of loops, boolean representing if there are parallel edges.

adj_list=[]
print(get_graph_info(adj_list))
