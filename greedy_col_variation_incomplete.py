import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    

def find_smallest_colour(G,i):
    n = len(G.nodes())
    edges = G.edges(i)

    colour = 0

    for edge in edges:
        node_colour = G.node[edge[1]]["colour"]

        if node_colour == "never coloured":
            continue

        if node_colour > colour:
            colour = node_colour

    return colour + 1

def greedy(G):
    n = len(G.nodes())
    global kmax
    global visited_counter

    #need to determine condition
    while True:
        next_vertex = find_next_vertex(G)
    
    

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.node[i]['colour'])
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
