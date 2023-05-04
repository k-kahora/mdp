# current pos must be a tulpe
# map is the grid world

    



states = {}
def mdp(grid_world):
    # Easily adjust living_reward to get differnt policys
    # Should be negative to get a time insentive
    # print(grid_world)
    living_reward = 0
    goal_reward = 1.00

    # Assing states to dict
    for i in range(len(grid_world)):
        for j in range(0, len(grid_world[i])):
            states[(i, j)] = {"living_reward": living_reward,"tile": grid_world[i][j]}

            # You can jump left or right
            # These values are daterministic
    actions = {"up": (0, -1),
               "right": (1,0),
               "down": (0,1),
               "left": (0,-1)}
               # "jump": {
               #     "left": (-2,0),
               #     "right": (2,0)
               # }}

    # ASsing the awards
    find_goal_and_prizes(grid_world, states)
    # print(states)

    return value_iteration(states, actions)

    # 8 is a cheryy so 100 pts
    # 9 is is a 500 point bag
    # 10 is a 1000 point bag
    # The agent needs to get all points in the least amount of time
    ## This meants to me prioritize time over points
    ## So order gets all points in minimum time
    ## 8 9 and 10 are equal rewards because they must all be snagged

    # s in unmodified
def valid_move(s,a,s_prime):
    # 1 to ignore the floor
    # only go up if state above is a 6
    # Code is reduntdant just trying to get it working
    up_check = check_bounds(s_prime, (s_prime[0] - 1, s_prime[1]))
    right_check = check_bounds(s_prime,  (s_prime[0] + 1, s_prime[1]))
    left_check = check_bounds(s_prime,  (s_prime[0] + 1, s_prime[1]))
    if a == "up":
        # You can only go up if previous state was a 6
        if states[s]["tile"] == 6:
            return s_prime
    if a == "left":
        if states[left_check]["tile"] == 4 or states[right_check]["tile"] == 6:
            return s_prime
    if a == "right":
        if states[right_check]["tile"] == 4 or states[right_check]["tile"] == 6:
            return s_prime
    if a == "down":
        if states[s_prime]["tile"] == 6:
            return s_prime
    return s

def check_bounds(s, a):
    # 1 to ignore the floor
    if a[0] >= 0 and a[0] <= 11:
        if a[1] >= 0 and a[1] <= 19:
            return a
    return s
    
    # Assume all states prizes are equal
    # Not a typical transition functioin
    # This just takes the given state and action and determinines the next state

    # This a perfect oppuertunity to do a unit test on this funtion
def T(s, a):
    action = (0,0)
    if a == "up":
        action = (-1,0)
    if a == "right":
        action = (0,1)
    if a == "left":
        action = (0,-1)
    if a == "down":
        action = (1,0)
    # s_prime is within the game bounds
    s_prime = (s[0] + action[0], s[1] + action[1])
    # s_prime is no checked within the game logic bounds
    s_prime = check_bounds(s, s_prime)
    s_prime = valid_move(s,a,s_prime)

    return s_prime

    # S is all states
    # A is all actions (they are all determinisc to no probabilities needed)
def value_iteration(S, A, gamma=0.9):
    # One to start to see if each iteration is making sense
    # As I gain confidence in the algo I will increase iteratiions 
    MAX_ITERATIONS = 1000

    V = {s: 0 for s in S}

    count = 0
    # test case
    # print(T((9,4),"left"))
    # print(states[(11,1)]["tile"])
    optimal_policy = {s: 0 for s in S}
    while count <= MAX_ITERATIONS:
        # Dynamic programming keep copy of previous calculation
        V_prev = V.copy()
        count += 1
        count_s = 0
        for s in S:
            count_s += 1
            Q = {}
            for a in A:
                s_next = T(s,a)
                Q[a] = states[s_next]["living_reward"] + gamma * V_prev[s_next]

            # print(s_next)
            # if count_s == 3:
            #     return

            V[s] = max(Q.values())
            optimal_policy[s] = max(Q, key=Q.get)
            
    return optimal_policy
    # First iteration will be all zero's
    # Next iteraiton will set rewards based on locatioin of the rewards
    # print(V)

def find_goal_and_prizes(grid_world, states):
        
    # set all states with a points on them to have a higher reward 
    for i in range(len(grid_world)):
        for j in range(0, len(grid_world[i])):
          # print(grid_world[i][j], end="")
          if grid_world[i][j] == 8 or  grid_world[i][j] == 9 or grid_world[i][j] == 10:
              states[(i,j)]["living_reward"] = 1
        # print("")
          


