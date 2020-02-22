import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5

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
    global kmax
    kmax = 0

    #find and assign the colours
    for i in G.nodes():
        colour = find_smallest_colour(G, i)
        G.nodes[i]["colour"] = colour

        if colour > kmax:
            kmax = colour

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
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
