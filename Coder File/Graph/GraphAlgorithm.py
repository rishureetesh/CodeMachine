class GraphAlgorithm:
    def __init__(self):
        self.adj_list = [[], [2], [1,3,4], [2,5], [2,6], [3,6], [4,5], [8], [7]]
        self.nums = 8
        self.visited = [False for i in range(self.nums+1)]
        self.store = []
        self.bfs_store = []
    
    def bfs(self, nums, adj_list, visited, store):
        self.bfs_store.append(store[0])
        while self.bfs_store:
            nums = self.bfs_store.pop(0)
            visited[nums] = True
            for num in adj_list[nums]:
                if not visited[num]:
                    visited[num] = True
                    self.store.append(num)
                    self.bfs_store.append(num)
            
    
    def dfs(self, nums, adj_list, visited, store):
        self.store.append(nums)
        visited[nums] = True
        for num in adj_list[nums]:
            if not visited[num]:
                self.dfs(num, adj_list, visited, store)
        return
    
    def run_dfs(self):
        for num in range(1, self.nums+1):
            if not self.visited[num]:
                self.dfs(num, self.adj_list, self.visited, self.store)
        self.print()
    
    def run_bfs(self):
        for num in range(1, self.nums+1):
            if not self.visited[num]:
                self.store.append(num)
                self.bfs(num, self.adj_list, self.visited, self.store)
        self.print()
    
    def print(self):
        print(self.store)

    
    def pilot(self):
        self.run_dfs()

obj = GraphAlgorithm()
obj.pilot()
    
