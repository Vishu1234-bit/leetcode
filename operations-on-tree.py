class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent=parent
        self.tree = [[] for i in parent]
        for i,x in enumerate(parent):
            if(x!=-1):
                self.tree[x].append(i)
        self.locked={}
    def lock(self, num: int, user: int) -> bool:
        if(num in self.locked):
            return False
        self.locked[num]=user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if(self.locked.get(num)!=user):
            return False
        self.locked.pop(num)
        return True
    def upgrade(self, num: int, user: int) -> bool:
        if(num in self.locked):
            return False
        node = num
        while(node!=-1):
            if(node in self.locked):
                return False
            node = self.parent[node]
        
        stack=[num]
        descendant=[]
        while(stack):
            node = stack.pop()
            if(node in self.locked):
                descendant.append(node)
            for child in self.tree[node]:
                stack.append(child)
        if(len(descendant)):
            self.locked[num] = user
            for node in descendant:
                self.locked.pop(node)
            return True
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
