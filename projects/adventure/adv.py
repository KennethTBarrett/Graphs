# Nodes are rooms
# Edges are pathways between rooms


from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack

# Load world
world = World()
# Instantiate our player.
player = Player(world.starting_room)

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Our traversal path.
traversal_path = []
# Track the paths traversed using a Stack.
paths = Stack()
# Visited is a dictionary of rooms already traveled.
visited = set()


def shortest_path(direction):
    """Helper function to determine the inverse direction."""
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"


# Ensure we haven't visited all rooms.
while len(visited) < len(world.rooms):
    # Get the available exits.
    exits = player.current_room.get_exits()
    path = []

    # Check each available exit. If the exit existed and wasn't in set, append
    # to our path.
    for exit in exits:
        if (exit is not None and
           player.current_room.get_room_in_direction(exit) not in visited):
                path.append(exit)
    # Add the current room to our set of visited rooms.
    visited.add(player.current_room)

    # If we have a path, make a random move based upon our path length.
    if len(path) > 0:
        move = random.randint(0, len(path)-1)
        # Push our path at randomly selected index from Stack.
        paths.push(path[move])
        player.travel(path[move])  # Make the specified move.
        traversal_path.append(path[move])  # Append to traversal path.
    else:  # If there's no path...
        end = paths.pop()  # Pop from stack
        # Travel to the inverse path based upon `end`
        player.travel(shortest_path(end))
        # Append to traversal path.
        traversal_path.append(shortest_path(end))


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
