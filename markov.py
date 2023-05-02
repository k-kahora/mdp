# current pos must be a tulpe
# map is the grid world
def mdp(curentPos, grid_world):
    states = []
    for i in range(len(grid_world)):
        for j in range(i, len(grid_world[i])):
            states.append((i,j))

            
    print(states)
