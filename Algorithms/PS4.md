1) Acydia
	1) Directed Acyclic Graph
	2) Find the longest path from the first page, that ends at a page with no further techniques.
	3) Starting from the first page, use DP to find the length of each subpath from the input, and return the path with the longest length.
	4) The algorithm works since every page's longest path depends on the longest path of the pages it's linked to. We look at all possible paths for a given page and compare the length of the paths, if no next pages exist, thats the base case with the path just being the page itself. Since we explore every path once, and always choose the longest path, the final value at the first page will give the maximum number of techniques you can learn before reaching the end.
	5) Time:
		1) Scan all paqges to start tracking best_path -> O(V)
		2) Check each page with path calls, but only once -> O(V)
		3) Next page scans: scan each next page to pick the longest continuation, across the run this goes to each edge once -> O(E)
		4) O(V+E)
```
Graph Book = (Pages, Links)
next[p] // Where we can go from p
source = 1 // Page 1

// Setup
for each page in Pages:
	best_path[page] = NONE // longest path starting at u as a list
	
path(p):
	if best_path[p] != NONE: // already seen the path
		return best_path[p]
	
	if next[p] is empty: // base case its a final page
		best_path[p] = [p]
		return best_path[p]
		
	longest = []
	for each link in next[p]:
		candidate = path(next)
		if len(candidate) > len(longest):
			longest = candidate
		
	best_path[p] = [p] + longest
	return best_path[p]
	
return path(source) // find best path from the start page
```

2) Dimensions
	1) We need something similar to a bipartite graph, but it cannot be a bipartite since there can be more than two sets. A general undirected graph probably works here, since we can group into sets of non-disputing entities (planes), and try to minimize the amount of planes
	2) We can begin by creating a plane for Destruction, then we look at the unplaced entities, and find which entity has the highest amount of plane conflicts (the hardest to place), and then place it at the lowest count plane that it can fit in. If every plane is already occupied by a disputee, create a new plane.
	3) Correct because:
		1) Each entity only placed on a plane that no rivals occupy, so no disputes exist in planes
		2) If an entity can't join a plane, a new one is made
		3) We assign (after destruction) the entity who cannot occupy the highest amount of currently existing planes, if more rivals get assigned, we have less options later, and may make unnecessary planes. This idea should reduce the amount of planes needed, since we can easily slot the very peaceful ones at the end
		4) Time:
			1) Starting with setup, we need to look at each entity, to setup the plane, number of disputes, and the structures to check fits -> O(|V|).
			2) Setup after destruction placing: Each rival is checked, so O(deg(Destruction)) <= O(|V|). -> O(|V|)
			3) Run the main loop once per entity (|V| iters)
				1) Pick the next entity, so we full scan each entity -> O(|V|) x |V| iters = O(|V|^2)
				2) Find the lowest valid plane, check up to one entry per blocked plane O(|V|), each entity can have up to a value K rivals, so O(K) per placement, or <= O(|V|^2).
				3) Update the neighbors, by checking each edge when its endpoint is placed. Total work is the number of edges after all runs are finished -> O(|E|)
			4) Total: O(|V|^2 + |E|)
```
Graph G = (V, E)

for v in V:
    plane[v] = NONE
    disputes[v] = deg(v)
    nofit[v] = 0
    rival_planes[v] = {none}

// Place destruction first
plane[Destruction] = 1
assigned = {Destruction}

// Setup neighbnor data
for w in N(destruction):
    rival_planes[w] += 1
    nofit[w] = |rival_planes[w]|

while |assigned| < |V|:
    u <- entity k not in assigned, max(notfit[for all k], with max disputes[k])

	// Assigned to the lowest valid plane
    used = rival_planes[u]
    p = 1
    while p in used:
        p += 1
    plane[u] = p
    assigned += u

    for w in N(u):
        if plane[w] == NONE and p not in rival_planes[w]:
            rival_planes[w] += []
            nofit[w] = |rival_planes[w]|
```

3) Max scores
a)
Using the adjacency list, we can just run BFS to find all reachable vertiies from the start v, and track the maximum. Its correct since BFS finds each vertex u where v -> u, finding the maximum t(u) gives S(v). BFS visits each vertex and edge once so O(|V| + |E|), a scan through each vertices adds O(|V|) time, so total is O(|V| + |E|)

b) 
```
adj[v] // Use the list

order = top_sort(adj) // topo sort the adjacency list
reverse(order) // reverse it
for v in order:
	best = t(v)
	for u in adj[v]:
		if S[u] > best:
			best = S[u]
	S[v] = best

return list S
```
A DAG has every edge going from an earlier to a later node in the top order. In reverse order we can guarantee for each v, all S[u] for v-> u is already computed. We just record the max score from nodes reachable from v. Top sort takes O(V+E), the DP passthrough each vertex and edge once, again O(V+E). O(V+E) total.

c)
