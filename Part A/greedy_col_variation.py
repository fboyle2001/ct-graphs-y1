import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5

def find_next_vertex(G):
    possible_vertices = set()

    for node in G.nodes():
        if G.nodes[node]["visited"] == "no":
            continue

        for neighbour in G[node]:
            if G.nodes[neighbour]["visited"] == "no":
                possible_vertices.add(neighbour)

    if len(possible_vertices) == 0:
        return None
        
    return min(possible_vertices)
                                  
def find_smallest_colour(G,i):
    n = len(G.nodes())
    used_colours = set()

    #find all of the neighbours colours

    for neighbour in G[i]:
        n_colour = G.nodes[neighbour]["colour"]

        if n_colour == "never coloured":
            continue

        used_colours.add(n_colour)

    #now know what colours we can't use
    #iterate until we find a colour not in the used

    colour = 1

    while colour in used_colours:
        colour += 1

    return colour

def greedy(G):
    n = len(G.nodes())
    global kmax
    global visited_counter
    kmax = 0
    visited_counter = 0

    current_node = 1

    while visited_counter != n:
        colour = find_smallest_colour(G, current_node)
        
        if colour > kmax:
            kmax = colour
            
        G.nodes[current_node]["colour"] = colour
        G.nodes[current_node]["visited"] = "yes"
        visited_counter += 1
        current_node = find_next_vertex(G)

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)
    print()



print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)
