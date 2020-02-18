import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5

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
    global kmax
    kmax = 0

    #visit each node in order
    for i in G.nodes():
        node_colour = find_smallest_colour(G, i)
        G.node[i]["colour"] = node_colour
        if node_colour > kmax:
            kmax = node_colour

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.node[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)

print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)
