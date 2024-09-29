class Solution:
    def alienOrder(self, words: List[str]) -> str:
        dictionary = defaultdict(list)
        in_degree = {char:0 for word in words for char in word}
        for i in range(len(words)-1):
            word1 , word2 = words[i],words[i+1]
            if(len(word1)>len(word2) and word1.startswith(word2)):
                return ""
            for char1,char2 in zip(word1,word2):
                if(char1!=char2):
                    dictionary[char1].append(char2)
                    in_degree[char2]+=1
                    break
        print(in_degree)
        print(in_degree,dictionary)
        queue = deque([node for node in in_degree if in_degree[node]==0])
        alienOrder = []
        while(queue):
            curr_letter=  queue.popleft()
            alienOrder.append(curr_letter)
            for neighbour in dictionary[curr_letter]:
                print(neighbour,"decreasing 1")
                in_degree[neighbour]-=1
                print(in_degree,alienOrder)
                if(in_degree[neighbour]==0):
                    queue.append(neighbour)
        print(alienOrder)
        if(len(alienOrder) == len(in_degree)):
            return ''.join(alienOrder)
        else:
            return ""        
