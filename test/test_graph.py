import pytest
import random
from src.graph import Graph


@pytest.mark.parametrize(
    "random_seed, n, weight, undirected, src, dest, expected_cost, expected_path",
    [(20, 5, 20, False, 1, 5, 21, [5, 3, 2, 1]),],
)
def test_dijkstra(
    random_seed, n, weight, undirected, src, dest, expected_cost, expected_path
):
    random.seed(random_seed)
    g = Graph.init_random_graph(n, weight, undirected)
    path = g.dijkstra(src, dest)
    assert g.nodes[dest].distance == expected_cost
    assert path == expected_path
