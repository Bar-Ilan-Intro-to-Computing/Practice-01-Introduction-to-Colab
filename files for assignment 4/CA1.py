
def CA1file2mat(file_path):
    """ Read the graph from text file CA1_data.txt, which is in this format:
        First row is the title, then space-separated data
        source in the first field, target in the 6th.
        Returns an adjacency matrix representing the graph
        and the list of nodes names.
    """
    f = open(file_path)
    f.readline() #discard title row

    #generate the nodes list
    nodes = []
    line = f.readline() #first edge
    while line != "": #while more lines to read
        line = line.split(" ") #split to fields
        source = line[0]
        target = line[5]
        if source not in nodes:
            nodes += [source]
        if target not in nodes:
            nodes += [target]
        line = f.readline() #next line

    #create adjacency matrix representing the graph
    n = len(nodes)
    G = [[0 for j in range(n)] for i in range(n)] # initialized with 0
    
    #assign 1 for existing edges
    f.seek(0, 0) #go to beginning of file
    f.readline() #discard title row

    line = f.readline() #first edge
    while line != "": #while more lines to read
        line = line.split(" ") #split to fields
        source = line[0]
        target = line[5]
        source_ind = nodes.index(source)
        target_ind = nodes.index(target)
        G[source_ind][target_ind] = 1

        line = f.readline() #next line

    f.close()

    return G,nodes



CA1,nodes = CA1file2mat("./CA1_data.txt")


