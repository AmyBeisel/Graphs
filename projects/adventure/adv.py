"""
1. translate the problem into graph terminology:
vertex = room
edges = n, s, e, w linking to each different room. 
weights = 

2. Build a graph:
test_line:
{
  0: [(3, 5), {'n': 1}],
  1: [(3, 6), {'s': 0, 'n': 2}],
  2: [(3, 7), {'s': 1}]
}

ect...until it links all the rooms. 

3. Traverse your graph:
 - An incomplete list of directions. Your task is to fill this with valid traversal directions.

 - you will need to write a traversal algorithm that logs the path into `traversal_path` as it walks.
 - Start by writing an algorithm that picks a random unexplored direction from the player's current room, 
    travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal.
    When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does
    contain an unexplored path.

 - You can find the path to the shortest unexplored room by using a breadth-first search for a room with a `'?'` 
   for an exit. If you use the `bfs` code from the homework, you will need to make a few modifications.

"""

from room import Room
from player import Player
from world import World
import random
from ast import literal_eval
from collections import deque



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = [] #empty list
visited = set() #empty set
path = [] #empty list
room = {} #empty dictionary
last_room = {'n': 's','s': 'n','e': 'w','w': 'e'} #directions
counter = 0

# while we haven't visited all the rooms
while len(visited) < len(room_graph):
    # Get the id of the current room
    currRoom = player.current_room.id
    # Check if we've visited that room.
    if currRoom not in visited:
        # if not add it to visited.
        visited.add(currRoom)
        # get list of all possible exits (or edges or neighbors)
        directions = player.current_room.get_exits()
        # add them to our dictionary
        room[currRoom] = directions

    # try ALL the possible directions in the current room
    while len(room[currRoom]) >= 0:
        # if there are directions to visit.
        if len(room[currRoom]) > 0:
            #pop off whatever is on top, this is current_node
            move = room[currRoom].pop()
            # if the id of that room to be visited isn't already in visited.
            if player.current_room.get_room_in_direction(move).id not in visited:
                # add it to the path tracker
                path.append(move)
                # save the move
                traversal_path.append(move)
                # make the move to the room
                player.travel(move)
                counter += 1
                #terminate the current loop.
                break
        # if there are no directions left to move, move back
        if len(room[currRoom]) == 0:
            # take our last move from the path tracker
            last_move = path.pop()
            # find the return direction.
            prior_direction = last_room[last_move]
            # save the move
            traversal_path.append(prior_direction)
            # make the move
            player.travel(prior_direction)
            
            #terminate the current loop. 
            break



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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
