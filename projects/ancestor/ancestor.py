from collections import deque

def earliest_ancestor(ancestors, starting_node):
    cache = {}
    for i in ancestors:
        # 0th index is parent
        # 1st index is child
        parent = i[0]
        child = i[1]

        # Determine whether child is in cache. If not...
        if child not in cache:
            # Set the child's value to be an array
            # for easy append.
            cache[child] = []
        cache[child].append(parent)

    # Our queue.
    queue = deque()
    queue.append([starting_node])
    
    anc = [1, -1]  # Base ancestors (this will fulfill the `-1` return requirement)

    while len(queue) > 0:
        current = queue.popleft()
        last_anc = current[-1]
        # Check if last ancestor is in cache.
        if last_anc not in cache:
            # Determine parent / child status.
            if len(current) > anc[0] or len(current) == anc[0] and last_anc < anc[1]:
                # Redefine ancestors.
                anc = [len(current), last_anc]
        # If last ancestor is in cache:
        else:
            # Iterate through items in the last ancestor's entry in our cache.
            for i in cache[last_anc]:
                # And append the current ancestor and item.
                queue.append(current + [i])
    # Return the 1st index of our ancestors (earliest ancestor).
    return anc[1]