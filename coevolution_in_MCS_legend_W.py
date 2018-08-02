import networkx as nx
import matplotlib.pyplot as plt
from numpy import arange
from time import time
from multiprocessing import Pool
from os import cpu_count
from qvoter_model import qvoter_coevolution


def simulation(runs):
    start_time = time()
    w_runs = []

    for w in w_values:
        runs_sim = []
        for i in range(runs):
            print('w:', w, 'run:', i+1)
            g = nx.watts_strogatz_graph(N, K, beta)
            runs_sim.append(qvoter_coevolution(g, q=4, h=h, w=w, p=p, f=f, steps=MC))
            print(time() - start_time)
        w_runs.append([sum(i)/len(runs_sim) for i in zip(*runs_sim)])

    return w_runs


if __name__ == '__main__':
    MC = 1000
    sim_num = 80
    p = 0.05
    N = 800
    f = 0.1
    h = 0.08
    K = 8
    beta = 0.1
    w_values = [0.0, 0.05, 0.1, 0.15, 0.2, 0.4]

    cpu_num = cpu_count()
    runs = int(sim_num / cpu_num)
    name = 'qvoter_coevolution_MC' + str(MC) + '_run' + str(sim_num) + 'legend_w_from' + str(min(w_values)).replace('.', '') + \
            '_to' + str(max(w_values)).replace('.', '') + '_p' + str(p).replace('.', '') + '_h' + str(h).replace('.', '') + \
           '_f' + str(f).replace('.', '') + '_N' + str(N) + '_K' + str(K) + '_beta' + str(beta).replace('.', '')

    p_multip = Pool(cpu_num)
    result = p_multip.map(simulation, [runs for i in range(cpu_num)])
    result = [i for i in zip(*result)]
    result_0 = [sum(i)/cpu_num for i in zip(*result[0])]
    result_1 = [sum(i)/cpu_num for i in zip(*result[1])]
    result_2 = [sum(i)/cpu_num for i in zip(*result[2])]
    result_3 = [sum(i)/cpu_num for i in zip(*result[3])]
    result_4 = [sum(i)/cpu_num for i in zip(*result[4])]
    result_5 = [sum(i)/cpu_num for i in zip(*result[5])]

    with open(name, "w") as text_file:
        print(result, file=text_file)

    plt.plot(arange(MC), result_0, 'r-', arange(MC), result_1, 'b-', arange(MC), result_2, 'g-',
             arange(MC), result_3, 'k--', arange(MC), result_4, 'm--', arange(MC), result_5, 'y--')
    plt.legend(['w=' + str(w_values[0]), 'w=' + str(w_values[1]), 'w=' + str(w_values[2]),
                'w=' + str(w_values[3]), 'w=' + str(w_values[4]), 'w=' + str(w_values[5])])
    plt.title("Fraction of adopted for h={}, p={}, f={},\n"
            r"Watts-Strogatz network with N={}, K={}, $\beta$={}".format(h, p, f, N, K, beta))
    plt.xlabel('Monte Carlo steps')
    plt.ylabel('Fraction of adopted')
    plt.savefig(name)
    plt.show()


