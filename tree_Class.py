class Tree:
    parent = None
    num_children = 0
    #!!
    children = []
    #!!
    context_word_id_set = []
    size = None

    def add_child(self,child):
        child.parent = self
        self.num_children += 1
        self.children[self.num_children] = child

    def size(self):
        if self.size != None:
            return self.size

        temp_size = 1
        for j in range(1, self.num_children):
            temp_size = temp_size + self.children[j].size
        self.size = temp_size
        return temp_size

    def depth(self):
        temp_depth = 0
        if self.num_children > 0:
            for i in range(1, self.num_children):
                child_depth = self.children[i].depth()
                if child_depth > temp_depth:
                    temp_depth = child_depth
                #end if
            #end for
            temp_depth += 1
        return temp_depth

    #def depth_first_preorder(self,tree,nodes):
     #   if tree == None:
      #      return


