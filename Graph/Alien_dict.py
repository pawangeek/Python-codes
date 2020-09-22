"""
IDEA (Using topological sorting)

1. Create a graph(g)

2. do following on every pair of word
    (i) Let the current pair of words be w1 and w2
    (ii) One by one compare chars from both and find first mismatch
    (iii) Create an edge from mismatched w1 to w2

3. Print topo sort for above graph 

"""

# Why topological sort ??

# Topological sort takes a directed acyclic graph and produces a linear ordering of all its vertices 
# such that if the graph G contains an edge (v,w) 
# then the vertex v comes before the vertex w in the ordering and thats what we want

from collections import defaultdict

class Graph:

    def __init__ (self):
        self.graph = defaultdict(list)

    # Simple recursive dfs Function
    def dfs(self, visited, v, result):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] is False:
                self.dfs(visited, i, result)

        result.append(v)
    
    def aliendict(self, dictionary):

        for i in range(1, len(dictionary)):

            # Take the two words from dictionary
            w1 = dictionary[i-1]
            w2 = dictionary[i]

            # Break each on first mismatch and create edge between w1(as vertex 1) and w2(vertex 2)
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    self.graph[w1[j]].append(w2[j])
                    break

        visited = {}
        alpha = []

        # Traversing all words 
        # 1. Make dictionary for each word(visited) and initialize value as False
        # 2. Append all words in alpha

        for word in dictionary:
            for char in word:
                if char not in visited:
                    visited[char] = False
                    alpha.append(char)

        result = []

        for i in alpha:
            if visited[i] is False:
                self.dfs(visited, i, result)

        print(result[::-1])
        print(''.join(result[::-1]))


if __name__ == "__main__":
    dictionary = ["baa", "abcd" ,"abca" ,"cab" ,"cad"]

    g = Graph()
    g.aliendict(dictionary)