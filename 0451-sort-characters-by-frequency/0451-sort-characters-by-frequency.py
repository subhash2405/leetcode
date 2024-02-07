class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
        sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        
        sorted_string = ''
        for char, freq in sorted_dic.items():
            sorted_string += char * freq
        
        return sorted_string
