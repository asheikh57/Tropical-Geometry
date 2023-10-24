from Graph import Graph as Graph
from Tropical import Tropical as Tropical

if __name__ == "__main__":
    ## User Area
    # TODO implement UI such that functions can be input on application level

    f = lambda x : Tropical(-4)*x*x + Tropical(10)*x + Tropical(1)
    graph = Graph()
    graph.add_func(f)
    f = lambda x : Tropical(-11)*x**3 + Tropical(-10)*x*x + Tropical(-7)*x + Tropical(-1)
    graph.add_func(f)
    graph.plot()
