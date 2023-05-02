# current pos must be a tulpe
# map is the grid world
def mdp(curentPos, grid_world):
    print(grid_world)
    living_reward = -0.04
    goal_reward = 1.00
    states = {}
    for i in range(len(grid_world)):
        for j in range(i, len(grid_world[i])):
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
    # 8 is cherry so a reward of 100 points
    #  is the goal so I an thinking a reward of 5000 points
    #  

    
def find_goal_and_prizes(grid_world, states):
        
    for i in range(len(grid_world)):
        for j in range(i, len(grid_world[i])):
          # print(grid_world[i][j])
          if grid_world[i][j] == "a":
            states[(i,j)] = 1.0
          

            
