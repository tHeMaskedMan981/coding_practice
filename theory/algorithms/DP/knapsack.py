# A Dynamic Programming based Python 
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can 
# be put in a knapsack of capacity W 
# We initialize the matrix with -1 at first. 

  
def knapsack_topdown(wt, val, W, n): 
  
    # base conditions 
    if n == 0 or W == 0: 
        return 0
    if t[n][W] != -1: 
        return t[n][W] 
  
    # choice diagram code 
    if wt[n-1] <= W: 
        t[n][W] = max( 
            val[n-1] + knapsack_topdown( 
                wt, val, W-wt[n-1], n-1), 
            knapsack_topdown(wt, val, W, n-1)) 
        return t[n][W] 
    elif wt[n-1] > W: 
        t[n][W] = knapsack_topdown(wt, val, W, n-1) 
        return t[n][W] 
  
  


  
def knapSack_bottomup(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    
    for i in range(n + 1): 
        for w in range(W + 1): 
            if wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                          + K[i-1][w-wt[i-1]],   
                              K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  
  
# Driver code 
val = [60, 100, 120, 45] 
wt = [10, 20, 30, 37] 
W = 100
n = len(val) 

t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
  
print(knapSack_bottomup(W, wt, val, n)) 
print(knapsack_topdown(wt, val, W, n)) 
  