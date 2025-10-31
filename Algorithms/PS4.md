1) Book
	1) Directed Acyclic Graph
	2) Find the longest path from the first page, that ends at a page with no further techniques.
	3) Starting at the first page, compute dp[u] = 1 + max (v = of all adj[u]) dp[v]. Use DFS to search out
		1) Need psuedocode here
	4) The algorithm works since every page's longest path depends on the longest path of the pages it's linked to. We look at all possible next pages for the length of a page plus 1, if no next pages exist, thats the base case with path length 1. Since we explore every path once, and always choose the longest path, the final value at the first page will give the maximum number of techniques you can learn before reaching the end.
	5) O(V + E) -> 
2) 