"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

import collections
from platform import node
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {} # keeping track of what we visited

        def dfs(node):
            if node in visited:
                return visited[node] #termination
            
            clone = Node(node.val, []) #clone unvisited node
            visited[node] = clone      #add in visited node

            for neighbor in node.neighbors:   
                clone_neighbors = dfs(neighbor) #dfs on each neighbor
                clone.neighbors.append(clone_neighbors) 

            return clone
        
        def bfs(node):
            queue = collections.deque([node])
            visited[node] = Node(node.val, [])  # Clone the starting node
            
            while queue:
                current_node = queue.popleft()
                
                for neighbor in current_node.neighbors:
                    if neighbor not in visited:
                        visited[neighbor] = Node(neighbor.val, [])  # Clone each new neighbor
                        queue.append(neighbor)
                    
                    # Add the cloned neighbor to the current clone's neighbors
                    visited[current_node].neighbors.append(visited[neighbor])
            
            return visited[node]


        return bfs(node)



