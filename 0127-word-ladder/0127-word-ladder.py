class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endWord not in wordList:
            # return 0
        queue = []
        visited = [beginWord]
        for word in wordList:
            if self.compare(beginWord, word) == 1:
                queue.append((word,1))
        count = 0
        flag = 0
        while queue:
            (temp,count) = queue.pop(0)
            if temp == endWord:
                flag = 1
                break
            if temp  in visited:
                continue
            visited.append(temp)
            for word in wordList:
                if self.compare(temp,word) == 1:
                    queue.append((word,count+1))
            wordList.remove(temp)
        if count == 0 or flag == 0:
            return 0
        return count + 1

    def compare(self,word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i]==word2[i]:
                continue
            count+=1
        return count
