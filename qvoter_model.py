import networkx as nx
from random import sample, randint, random
from make_coevolution import link_changing_first_neighbour_who_disagree_to_random_new_neighbour


def qvoter_coevolution(g, q, h, w, p, f, steps):
    g_size = nx.number_of_nodes(g)
    op = dict((x, 0) for x in range(g_size))
    C_k = []

    for i in range(steps):
        for j in range(g_size):
            spinson = randint(0, g_size-1)

            if random() < p:
                if random() < f:
                    op[spinson] = abs(op[spinson] - 1)
            else:
                try:
                    qpanel = sample(g.neighbors(spinson), q)
                    opinions = sum([op[x] for x in qpanel])

                    if opinions in (0, q):
                        op[spinson] = op[qpanel[0]]
                    else:
                        if random() < w:
                            link_changing_first_neighbour_who_disagree_to_random_new_neighbour(g, op, spinson, qpanel)
                        if random() < h:
                            op[spinson] = 1
                except ValueError:
                    pass

        C_k.append(sum(op.values()) / g_size)

    return C_k
