import numpy as np
import random
import time


class SimbolicRegression(object):
    def __init__(self, pop_size=50,
                 seed=np.random.randint(time.time()),
                 crossover_probability=0.9,
                 mutation_probability=0.1,
                 internal_node_selection_bias=0.9, ):
        self.pop_size = pop_size
        self.seed = seed
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.internal_node_selection_bias = internal_node_selection_bias

    def fit(self, X, y):
        self.num_features = X.shape[0]
        random.seed(self.seed)
        np.random.seed(self.seed)

    def score(self):
        pass

    def print_best_individuals(self):
        """Print the error and string representation of best_individuals_
        :return:
        """
        if self.best_individuals_ is None:
            raise RuntimeError('Cannot print best individuals. Model has not yet been fit!')
        for ind in self.best_individuals_:
            print(str(ind.error) + ' : ' + str(ind))


def target_func(x):
    return - 0.4 * (x ** 2) + 0.1 * (x ** 3) + 3 * x - 0.01 * (x ** 4)


def work():
    X = np.linspace(-10, 10, 200, endpoint=True)
    y = target_func(X)
    sr = SimbolicRegression()
    sr.fit(X, y)
    score = sr.score()
    print('Score: ' + str(score))
    print('Best Individuals:')
    sr.print_best_individuals()


if __name__ == '__main__':
    work()
