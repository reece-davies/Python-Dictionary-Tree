# COMP3002 assignment - Task 2B
# Depth First & Breadth First Traversal with Dictionary-based binary trees

# Depth First search (preorder)
def depthFirstSearch(tree):

    # Set to keep track of visited nodes
    visited = set()

    # Recursive function
    def search(tree, visited):

        # If selected value for node has not been given already, run the following
        if tree['value'] not in visited:

            # Output node value and add it to visited set
            print("Node value = ", tree['value'])
            visited.add(tree['value'])

            # If current node has children
            if tree['children'] is not None:

                # Perform search for all children of current node
                for i in range(len(tree['children'])):
                    search(tree['children'][i], visited)

    # First node search
    search(tree, visited)



# Breadth First search (preorder)
def breadthFirstSearch(tree):
    
    # Queue to keep track of what levels (for the tree) need to be searched
    queue = []
    queue.append(tree)

    # While queue still contains items, perform leveled search
    while(len(queue) > 0):
        
        # Output node value and remove it from queue
        print("Node value = ", queue[0]['value'])
        tree = queue.pop(0)

        # If current node has children
        if tree['children'] is not None:

            # Add all children of current node to the queue
            for i in range(len(tree['children'])):
                queue.append(tree['children'][i])



# Non-binary dictionary tree
# Each node has non-negative integer value, and list of children
dictionaryTree = {
    'value' : 5,
    'children' : [
        {
            'value' : 8,
            'children' : [
                {
                    'value' : 4,
                    'children' : []               
                },
                {
                    'value' : 7,
                    'children' : [
                        {
                            'value' : 12,
                            'children' : []
                        },
                        {
                            'value' : 9,
                            'children' : []
                        }] 
                }]
        },
        {
            'value' : 3,
            'children' : []
        },
        {
            'value' : 10,
            'children' : [
                {
                    'value' : 1,
                    'children' : []               
                }]
        }]
    }


print("Tree = ", dictionaryTree)
# Tree visualisation
# 		    5
# 	     / 	|  \ 
# 	    8	3	10
#     /   \	     |
#    4	   7	 1
# 	     /	|
# 	   12	9

print("\n -- Depth first traversal (preorder) -- ")
print("Expected output: 5 8 4 7 12 9 3 10 1")
depthFirstSearch(dictionaryTree)

print("\n -- Breadth first traversal (preorder) -- ")
print("Expected output: 5 8 3 10 4 7 1 12 9")
breadthFirstSearch(dictionaryTree)

input("\nProgram finished. Press any key to continue...")
