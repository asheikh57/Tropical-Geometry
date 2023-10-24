import Tropical.Tropical as Tropical
import matplotlib.pyplot as plt
class Graph:

    def __init__(self,
                 x_min=0,
                 x_max=10,
                 y_min = 0,
                 y_max = 10,
                 num_samples=1000,
                 funcs=[]):
        self.x_min = x_min
        self.x_max = x_max
        self.num_samples = num_samples
        self.funcs = funcs
        self.y_min = y_min
        self.y_max = y_max

    @property
    def domain(self):
        dx = (self.x_max - self.x_min)/(self.num_samples-1)
        return [Tropical(i*dx + self.x_min) for i in range(self.num_samples)]

    def compute_codomain(self, func):
        codomain = [func(x) for x in self.domain]
        return codomain

    @property
    def func_dict(self):
        return {self.funcs[i]: self.compute_codomain(self.funcs[i]) for i in range(len(self.funcs))}

    def calibrate_y_bound(self):
        codomains = [self.compute_codomain(func) for func in self.funcs]
        self.y_min = min(codomains)
        self.y_max = max(codomains)

    def add_func(self, func):
        self.funcs.append(func)

    def plot(self):
        for func in self.funcs:
            plt.plot(self.domain, self.func_dict[func])
        plt.show()

    def clear(self):
        self.funcs = []

if __name__ == "__main__":
    f = lambda x : Tropical(-4)*x*x + Tropical(10)*x + Tropical(1)
    graph = Graph()
    graph.add_func(f)
    f = lambda x : Tropical(-11)*x**3 + Tropical(-10)*x*x + Tropical(-7)*x + Tropical(-1)
    graph.add_func(f)
    #graph.clear()
    graph.plot()
