# current pos must be a tulpe
# map is the grid world
def mdp(curentPos, grid_world):
    # Easily adjust living_reward to get differnt policys
    # Should be negative to get a time insentive
    # print(grid_world)
    living_reward = -0.04
    goal_reward = 1.00
    states = {}
    for i in range(len(grid_world)):
        for j in range(0, len(grid_world[i])):
            states[(i, j)] = living_reward

            # You can jump left or right
    actions = {"up": (0, -1),
               "right": (1,0),
               "down": (0,1),
               "left": (0,-1),
               "jump": {
                   "left": (-2,0),
                   "right": (2,0)
               }}

    # ASsing the awards
    find_goal_and_prizes(grid_world, states)
    # print(states)
    # 8 is a cheryy so 100 pts
    # 9 is is a 500 point bag
    # 10 is a 1000 point bag
    # The agent needs to get all points in the least amount of time
    ## This meants to me prioritize time over points
    ## So order gets all points in minimum time
    ## 8 9 and 10 are equal rewards because they must all be snagged

    
    # goal states for start level
# (1, 3)
# (1, 6)
# (1, 17)
# (4, 5)
# (4, 18)
# (7, 7)
# (7, 14)
# (10, 11)
def find_goal_and_prizes(grid_world, states):
        
    # set all states with a points on them to have a higher reward 
    for i in range(len(grid_world)):
        for j in range(0, len(grid_world[i])):
          # print(grid_world[i][j], end="")
          if grid_world[i][j] == 8 or  grid_world[i][j] == 9 or grid_world[i][j] == 10:
            states[(i,j)] = 1.0
        # print("")
          

            
