class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        graph=self.build_graph(rooms)
        visited=[False]*n
        if visited[0]==False:
            self.dfs(0,graph,visited)
        for i in range(n):
            if visited[i]==False:
                return False
        return True
        
    def dfs(self,node,graph,visited):
        visited[node]=True
        for nbr in graph[node]:
            if not visited[nbr]:
                self.dfs(nbr,graph,visited)
        
        
    def build_graph(self,rooms):
        n=len(rooms)
        g=dict()
        for i in range(n):
            g[i]=list()
        for i in range(n):
            curr=rooms[i]
            for each_node in curr:
                g[i].append(each_node)
        return g
        
