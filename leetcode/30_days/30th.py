# @Date:   2020-04-30T16:46:12+05:30
# @Last modified time: 2020-04-30T17:10:21+05:30

#1. Determine if there is a part that matches the list.
#2. If there is, start searching for the next index to the left or right of the node.

def ValidSequence(self,node,arr) :

    if  arr  == []:
        if node != None :
            return False
        return True

    if node == None :
        return False

    if node.val == arr[0] :
        left = self.ValidSequence(node.left,arr[1:])
        right = self.ValidSequence(node.right,arr[1:])

        if  len ( arr [ 1 :]) ==  0 :
            return left and right
        return left or right

    else :
        return False

def isValidSequence(self, root, arr):

    if root == None or arr == [] :
        return False

    return self.ValidSequence(root,arr)
