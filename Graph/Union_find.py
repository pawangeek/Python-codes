# Disjoint set is a group of sets where no item can be in more than one set

# Find: To find which componant a particular element belongs to, 
#       Find root of that component find following the parent node until self loop is reached

# Union: To unify two elements find which are root nodes of each component
#       If root nodes are different make one parent of another

# How Union Finds Work

# We can determine whether two elements are in same subset or not by comparing result of two find ops
# If two elements are in same set, they have same representative else they belong to different sets. 
# If the union is called on two elements, we merge the two subsets which the two elements were belonging to.

class Disjoint:
    parent = {}

    def makeset(self, universe):

        # Create n disjoints sets
        for i in universe:
            self.parent[i]=i
        
    def finds(self, k):

        # if k is root
        if self.parent[k]==k:
            return k
        
        # recur for parent until we find root
        return self.finds(self.parent[k])

    def union(self, a, b):

        x = self.finds(a)
        y = self.finds(b)

        self.parent[x]=y

