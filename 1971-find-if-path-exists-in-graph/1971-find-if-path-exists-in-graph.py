class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        result = 0
        parent = [0] * (n)
        for i in range(0,n):
            parent[i] = i
        
        if n == 1:
            return True
        
        # for i in range(len(edges)):
        #     self.unionParent(parent,edges[i][0], edges[i][1])
        # print(parent)    
        # if parent[source] == parent[destination]:
        #     result = True
        # else:
        #     result = False
        # return result
        
#         for i in range(len(edges)):
#             if self.findParent(parent,edges[i][0]) == self.findParent(parent,edges[i][1]):
#                 result = True
#             else:
#                 self.unionParent(parent,edges[i][0],edges[i][1])
                
#         print(parent)    
#         if parent[source] == parent[destination]:
#             result = True
#         else:
#             result = False
#         return result
        
        
        for i in range(len(edges)):
            self.unionParent(parent,edges[i][0], edges[i][1])
        print(parent)    
        return self.findParent(parent,source) == self.findParent(parent,destination)
        

    
    def unionParent(self, parent, a, b):
        a = self.findParent(parent, a)
        b = self.findParent(parent, b)
        if a<b:
            parent[b] = a
        else:
            parent[a] = b
        
    def findParent(self, parent, x):
        if parent[x] != x:
            parent[x] = self.findParent(parent,parent[x])
        return parent[x]