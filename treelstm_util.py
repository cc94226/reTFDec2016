def set_spans(tree)
	if tree.num_children == 0:
		tree.lo, tree.hi = tree.leaf_idx, tree.leaf_idx
	return
	
	for i in range (1, tree.num_children):
		set_spans(tree.children[i])

	tree.lo, tree.hi = tree.children[1].lo, tree.children.hi
	for i in range(2, tree.num_children):
		tree.lo = min (tree.lo, tree.children[i].lo)
		tree.hi = max( tree.hi, tree.children[i].hi)

def addToSet(dic, key):
	dic[key] = True
