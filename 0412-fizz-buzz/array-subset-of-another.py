#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
            # Your code here
            a.sort()
            b.sort()
        
            i = j = 0
            m , n = len(a), len(b)
        
            while i < m and j < n:
                if a[i] < b[j]:
                
                    i += 1  
                elif a[i] == b[j]:
                    i += 1
                   
                    j += 1  
                else:
                 
                    return False
        
            return j == n  
    
    
    
    
