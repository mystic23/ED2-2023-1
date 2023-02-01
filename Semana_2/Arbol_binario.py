class TreeNode:
    def __init__(self, value) :
        self.left = None
        self.right = None
        self.value = value
   
        
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                
            else:
                self.left.insert(value)
        else: 
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    
    def inorder_traversal(self): 
        """
        Aquí vamos más a la izquierda posible y luego
        cuando ya no podamos ir más, entonces imprimimos
        y luego vamos más a la derecha posible
        """
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
            
    def preorder_traversal(self): 
        """
        Diferencia: Aquí imprimimos al inicio
        """
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        
        if self.right:
            self.right.preorder_traversal()
    
    
    def postorder_traversal(self): 
        """
        Diferencia: Aquí imprimimos al final
        """
       
        if self.left:
            self.left.postorder_traversal()
        
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
    
    def find(self, value):
            if value < self.value:
                if self.left is None:
                    return True
                else:
                    return self.left.find(value)
            elif value > self.value:
                if self.right is None:
                    return True
                else:
                    return self.right.find(value)
            else:
                ##Aquí es donde lo encuentra
                return True
                

#probando el arbolito, forma mundana y brusca 
tree = TreeNode(10)
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(9)
tree.insert(12)
tree.insert(13)
tree.insert(18)
tree.insert(25)
tree.insert(15)

#tree.postorder_traversal()                                                                                                                                                                             
print(tree.find(9))

