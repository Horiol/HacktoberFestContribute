def findLongestSubSeq(str): 
	n = len(str) 

	dp = [[0 for _ in range(n+1)] for _ in range(n+1)] 

	for i in range(1, n+1): 
		for j in range(1, n+1): 
			# If characters match and indices are not same 
			if (str[i-1] == str[j-1] and i != j): 
				dp[i][j] = 1 + dp[i-1][j-1] 

			# If characters do not match 
			else: 
				dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 

	return dp[n][n] 
