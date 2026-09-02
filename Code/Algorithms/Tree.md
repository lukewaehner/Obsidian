```python
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.children = []
		
	def add_child(self, child_val):
		child = Node(child_val)
		self.children.append(child)
		return child
		
	def traverse(self, depth=0):
		print(" " * depth + str(self.val))
		for child in self.children:
			child.traverse(depth + 1)
```


**DFS** -> Recursive, stack-based. Go all the way deep first.

```python
def dfs(node):
	print(node.val)
	for c in node.children:
		dfs(c)
```

```python
def dfs(node):
	if node is None:
		return
	stack = [node]
	while stack:
		node = stack.pop()
		print(node.val)
		stack.append(node.left)
		stack.append(node.right)
		
	
```


Preorder -> Visit, Left, Right
```python
def preorder(node):
	if node == null: 
		return
	print(node.val)
	preorder(node.left)
	preorder(node.right)
```
O(n)

In-order -> Left, visit, right

```python
def inorder(node):
	if node == null: 
		return
	inorder(node.left)
	print(node.val)
	inorder(node.right)
```

Post-order -> Left, Right, Visit

```python
def postorder(node):
	if node == null: 
		return
	postorder(node.left)
	postorder(node.right)
	print(node.val)
```


**BFS** -> Visit all the children first

```python
from collections import deque
def bfs(root):
	q = deque([root])
	while q:
		node = q.popleft()
		print(node.val)
		q.extend(node.children)
```

Level-Order
```python
def levelorder(root)
	if root is None:
		returen
	q = deque([root])
	while q:
		node = q.popleft()
		print(node.value)
		if node.left:
			q.append(node.left)
		if node.right:
			q.extend(node.right)
```

Traversal visits each node once -> O(n)
Space = O(h) for recursion or O(n) for BFS

Parsing html/xml trees, abstract syntax trees
Hierarchies

General tree: unordered, any arity
N-ary tree: each node limited to <= N children

Binary Search Tree:

```python
class BST():
	class Node():
		def __init__(self, val):
			self.val = val
			self.left = None
			self.right = None
			
	def __init__(self):
		self.root = None
	
	# add to a tree
	def add(self, val):
		# empty tree
		if self.root is None:
			self.root = Node(val)
			return
		
		# start with root to figure out where to place
		node = self.root
		while True:
			if val < node.val:
				if node.left:
					# iterate the tree
					node.left = node.left
					node = node.left
				else:
					node.left = Node(val)
					break
			elif val > node.right:
				if node.right:
					node.right = node.right
					node = node.right
				else:
					node.right = Node(val)
					break
			else:
				break
```