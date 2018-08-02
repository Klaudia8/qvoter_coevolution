from random import choice


# First neighbour who disagree - randomly choose one random neighbour
def link_changing_first_neighbour_who_disagree_to_random_new_neighbour(G, op, spinson, qpanel):
    removed = 0
    for neighbour in qpanel:
        if op[neighbour] != op[spinson] and removed == 0:
            neighbs = G.neighbors(spinson)
            nodes = G.nodes()
            nodes.remove(spinson)
            nodes = [i for i in nodes if i not in neighbs]
            G.remove_edge(spinson, neighbour)
            G.add_edge(spinson, choice(nodes))
            removed = 1