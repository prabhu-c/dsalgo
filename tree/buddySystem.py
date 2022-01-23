from typing import List

"""
buddy system bitmap
    Given a complete binary tree with nodes of values of either 1 or 0, the following rules always hold:
    (1) a node's value is 1 if and only if all its subtree nodes' values are 1
    (2) a leaf node can have value either 1 or 0
    Implement the following 2 APIs:
    set_bit(offset, length), set the bits at range from offset to offset+length-1
    clear_bit(offset, length), clear the bits at range from offset to offset+length-1
    
    i.e. The tree is like:
                 0
              /     \
             0        1
           /  \      /  \
          1    0    1    1
         /\   / \   / 
        1  1 1   0 1
        Since it's complete binary tree, the nodes can be stored in an array:
        [0,0,1,1,0,1,1,1,1,1,0,1] 
        
"""

"""
Problem:
1. Given an offset & length
2. Set & Clear nodes starting from offset upto length

Solution:
1. dfs to update the nodes
2. preorder: update the nodes within the range
3. postorder: update the parent nodes
4. start updating from offset index
5. keep track of the length

Assumptions:
1. Force set all the child nodes for set_bit
2. No action on child nodes for clear_bit

"""

def dfs_update_allnodes(arr: List[int], index:int, value:int):

    # base case
    if index > len(arr):
        return None

    # recursive case
    # preorder - update the child nodes
    arr[index-1] = value

    dfs_update_allnodes(arr, index * 2, value)

    dfs_update_allnodes(arr, (index * 2)+1, value)

    return None

def buddySystem_set_bits(arr: List[int], offset, length):

    if arr == None or len(arr) == 0:
        return None

    def dfs_set_nodes(arr: List[int], index:int):

        # base case
        arrSize = len(arr)
        if index > arrSize:
            return False

        # recursive case
        left = index * 2
        right = (index * 2) + 1
        end = True
        # preorder
        # update the nodes within the range
        if index < offset + length:
            if index >= offset:     #nodes within the range
                arr[index-1] = 1
                end = False
                # force update all children to 1
                dfs_update_allnodes(arr, index, 1)
            else:
                # This node is less than offset, check its children
                end = dfs_set_nodes(arr, left)

                if end == False:                # already reached length no need to traverse further
                    dfs_set_nodes(arr, right)
        else:
            return end

        # postorder
        # update the parent node
        # should have a left child and optional right child
        if (left <= arrSize and arr[left-1] == 1) and (right > arrSize or arr[right-1] == 1):
            arr[index-1] = 1

        return end

    # lauch dfs to set nodes by offset
    dfs_set_nodes(arr, 1)

    return None

def buddySystem_clear_bits(arr: List[int], offset, length):

    if arr == None or len(arr) == 0:
        return None

    def dfs_clear_nodes(arr: List[int], index:int):

        # base case
        arrSize = len(arr)
        if index > arrSize:
            return False

        # recursive case
        left = index * 2
        right = (index * 2) + 1
        end = True
        # preorder
        # update the nodes within the range
        if index < offset + length:
            if index >= offset:     #nodes within the range
                arr[index-1] = 0
                end = False
                # no action to the children
                    # force update 0
                    # dfs_update_allnodes(arr, index, 0)
            else:
                # This node is less than offset, check its children
                end = dfs_clear_nodes(arr, left)

                if end == False:             # already reached length no need to traverse further
                    end = dfs_clear_nodes(arr, right)
        else:
            return end

        # postorder
        # update the parent node
        # one of the child is zero
        if (left <= arrSize and arr[left-1] == 0) or (right <= arrSize and arr[right-1] == 0):
            arr[index-1] = 0

        return end

    # lauch dfs to clear nodes from offset
    dfs_clear_nodes(arr, 1)

    return None
