def editDistDP(str1, str2, m, n):

    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
 
   
    for i in range(m + 1):
        for j in range(n + 1):
 
          
            if i == 0:
                dp[i][j] = j    # Min. operations = j
 
       
            elif j == 0:
                dp[i][j] = i    # Min. operations = i
 
         
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace
 
    return dp[m][n]
 
 

str1 = "abad"
str2 = "abac"
 
print(editDistDP(str1, str2, len(str1), len(str2)))

#output- 1
