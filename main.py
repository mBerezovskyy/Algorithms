graph = {
    "A": [[], 4],
    "B": [["A"], 3],
    "C": [["A"], 1],
    "D": [["B"], 2],
    "E": [["B", "C"], 1],
    "F": [["C"], 5],
    "G": [["D"], 1],
    "H": [["D", "E"], 3],
    "I": [["E", "F"], 2],
    "J": [["F"], 1]
}


def dfs(graph, path, all_possible_paths=None, cost=0):
    if all_possible_paths is None:
        all_possible_paths = []
    current_node = path[-1]
    neighbours = graph[current_node][0]
    current_cost = graph[current_node][-1]
    cost += current_cost
    if neighbours:
        for neighbour in neighbours:
            new_path = path + [neighbour]
            all_possible_paths = dfs(graph, new_path, all_possible_paths, cost)
    else:
        all_possible_paths += [(path, cost)]
    return all_possible_paths


solutions_G = dfs(graph, ['G'], [])
solutions_H = dfs(graph, ['H'], [])
solutions_I = dfs(graph, ['I'], [])
solutions_J = dfs(graph, ['J'], [])

max_solution_G = max([solutions_G[i][1] for i in range(len(solutions_G))])
max_solution_H = max([solutions_H[i][1] for i in range(len(solutions_H))])
max_solution_I = max([solutions_I[i][1] for i in range(len(solutions_I))])
max_solution_J = max([solutions_J[i][1] for i in range(len(solutions_J))])

final_sollution = max([max_solution_G, max_solution_H, max_solution_I, max_solution_J])
