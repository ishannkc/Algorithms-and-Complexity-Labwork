import time
import random
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor


# -----------------------------------------
# Generate Random Graph
# -----------------------------------------

def generate_graph(vertices):

    graph = {}

    for i in range(vertices):
        graph[i] = []


    # Generate random edges
    edges = vertices * 2


    for _ in range(edges):

        u = random.randint(0, vertices-1)
        v = random.randint(0, vertices-1)


        if u != v and v not in graph[u]:

            graph[u].append(v)
            graph[v].append(u)


    return graph



# -----------------------------------------
# Sequential DFS
# -----------------------------------------

def dfs(graph, node, visited, component):

    visited.add(node)
    component.append(node)


    for neighbour in graph[node]:

        if neighbour not in visited:

            dfs(
                graph,
                neighbour,
                visited,
                component
            )



def sequential_components(graph):

    visited=set()
    components=[]


    for node in graph:

        if node not in visited:

            component=[]

            dfs(
                graph,
                node,
                visited,
                component
            )

            components.append(component)


    return components



# -----------------------------------------
# Parallel DFS
# -----------------------------------------

def parallel_task(data):

    graph,node=data

    visited=set()
    component=[]


    dfs(
        graph,
        node,
        visited,
        component
    )


    return component



def parallel_components(graph, processors):

    tasks=[]


    for node in graph:

        tasks.append(
            (graph,node)
        )


    components=[]

    global_visited=set()



    with ThreadPoolExecutor(
        max_workers=processors
    ) as executor:


        results=executor.map(
            parallel_task,
            tasks
        )


        for result in results:

            new=[]


            for node in result:

                if node not in global_visited:

                    global_visited.add(node)

                    new.append(node)


            if new:

                components.append(new)


    return components



# -----------------------------------------
# Complexity Graph
# -----------------------------------------

def complexity_graph(vertices, processors):

    x=[]
    sequential=[]
    parallel=[]


    for v in range(10, vertices+10, 10):

        x.append(v)


        # Assume E = 2V

        e = 2*v


        sequential.append(
            v+e
        )


        parallel.append(
            (v+e)/processors
        )



    plt.figure(figsize=(8,5))


    plt.plot(
        x,
        sequential,
        color="red",
        marker="o",
        label="Sequential O(V+E)"
    )


    plt.plot(
        x,
        parallel,
        color="green",
        marker="s",
        label=f"Parallel O((V+E)/P), P={processors}"
    )


    plt.xlabel(
        "Number of Vertices"
    )


    plt.ylabel(
        "Operations"
    )


    plt.title(
        "Connected Components: Sequential vs Parallel"
    )


    plt.legend()

    plt.grid(True)

    plt.show()



# -----------------------------------------
# Main Program
# -----------------------------------------

print("Connected Components using Parallel Algorithm")
print("----------------------------------------------")


vertices=int(
    input(
        "Enter number of vertices: "
    )
)


processors=int(
    input(
        "Enter number of processors: "
    )
)



# Create graph automatically

graph = generate_graph(vertices)



print("\nGraph Generated Successfully")


# Sequential

start=time.time()


seq_result = sequential_components(
    graph
)


seq_time=time.time()-start



# Parallel

start=time.time()


par_result = parallel_components(
    graph,
    processors
)


par_time=time.time()-start



# Results

print("\n----------- RESULT -----------")


print(
    "Number of Connected Components:",
    len(seq_result)
)


print(
    "\nSequential Components:"
)

print(
    seq_result
)


print(
    "\nParallel Components:"
)

print(
    par_result
)



print("\nExecution Time")

print(
    "Sequential DFS:",
    seq_time,
    "seconds"
)


print(
    "Parallel DFS:",
    par_time,
    "seconds"
)



print("\nComplexity")

print(
    "Sequential: O(V+E)"
)


print(
    "Parallel: O((V+E)/P)"
)



# Show complexity graph

complexity_graph(
    vertices,
    processors
)