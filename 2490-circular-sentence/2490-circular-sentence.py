class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split()
        i = 0 
        while i < len(arr):
            if i == len(arr)-1:
                if ascii(arr[i][-1]) != ascii(arr[0][0]): 
                    return False
            
            else:
                if ascii(arr[i][-1]) != ascii(arr[i+1][0]):
                    return False
            i+=1
        
        return True