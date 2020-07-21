from random import choice, sample

import numpy as np

g_target_gene = np.array(list('unicornforyou'))
mutation_rate = 0.1
selection_rate = 0.3


def make_string(arr):
    res = ''
    for i in arr:
        res = res + str(i)
    return res


def gene_fitness(gene):
    global g_target_gene
    cnt = 0
    for i, j in zip(g_target_gene, gene):
        if i == j:
            cnt += 1
    return float(cnt / len(g_target_gene))


class Rat(object):
    def __init__(self, given_gene=None):
        global g_target_gene
        self.gene = given_gene
        if given_gene is None:
            self.gene = np.vectorize(lambda x: chr(x))(np.random.randint(97, 123, len(g_target_gene)))
        self.fitness = gene_fitness(self.gene)

    def mutation(self):
        for i in sample(range(len(self.gene)), 3):
            self.gene[i] = chr(np.random.randint(97, 123))


class Population(object):
    def __init__(self):
        self.content = [Rat() for i in range(10)]

    def best(self):
        res = 0
        for i in self.content:
            res = max(res, i.fitness)
        return res

    def best_one(self):
        res = None
        cp = 0
        for i in self.content:
            if cp < i.fitness:
                cp = i.fitness
                res = i
        return res

    def crossover(self):
        global mutation_rate, g_target_gene
        new_ones = []
        for i in self.content:
            for j in self.content:
                if i is not j:
                    gene = []
                    for k in range(len(i.gene)):
                        if i.gene[k] == j.gene[k]:
                            gene.append(i.gene[k])
                        elif i.gene[k] == g_target_gene[k]:
                            gene.append(i.gene[k])
                        elif j.gene[k] == g_target_gene[k]:
                            gene.append(j.gene[k])
                        else:
                            gene.append(choice([i.gene[k], j.gene[k]]))
                    child = Rat(gene)
                    if np.random.binomial(1, mutation_rate) == 1:
                        child.mutation()
                    new_ones.append(child)
        self.content = self.content + new_ones

    def selection(self):
        global selection_rate
        self.content = sorted(self.content, key=lambda x: x.fitness)
        if len(self.content) >= 100:
            selection_rate = (len(self.content) - 100) / len(self.content)
        else:
            selection_rate = 0.3
        for i in range(int(len(self.content) * selection_rate)):
            if self.content is []:
                break
            del (self.content[0])

    def simulate(self, method='rc', converge_time=None):
        if method == 'rc':
            cnt = 0
            while self.best() < 0.95:
                cnt += 1
                self.crossover()
                self.selection()
                print('Round ', cnt, ' best fitness is ', self.best(), ', best gene is ',
                      make_string(self.best_one().gene))
                if self.content is []:
                    break
            return cnt


def work():
    global g_target_gene
    print('The target string we want to match is "', make_string(g_target_gene), '"')
    my_pop = Population()
    print('Iterated ', my_pop.simulate(), ' times')
    print('---end---')


if __name__ == '__main__':
    work()
