import arcade
import game_core
import threading
import time
import os
import pygame
import markov
# Our custom AI 

class Agent(threading.Thread):

    def __init__(self, threadID, name, counter, show_grid_info=True):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.show_grid_info = show_grid_info

        self.game = []
        self.move_grid = []
        self.kill_grid = []
        self.isGameClear = False
        self.isGameOver = False
        self.current_stage = 0
        self.time_limit = 0
        self.total_score = 0
        self.total_time = 0
        self.total_life = 0
        self.tanuki_r = 0
        self.tanuki_c = 0

    #############################################################
    #      YOUR SUPER COOL ARTIFICIAL INTELLIGENCE HERE!!!      #
    #############################################################
    def ai_function(self):
        ai = markov.Markovs.get_instance()
        # print("In AI fn")
        current_position = (self.tanuki_r, self.tanuki_c)
        space = self.move_grid
        if ai.flag:
            ai.flag = False
            ai.optimal_policy = markov.mdp(space)

        if markov.states[current_position]["living_reward"] > 0:
            space[current_position[0]][current_position[1]] = 1
            print(ai.optimal_policy)
            print(space)
            print("current_pos")
            print(current_position)
            ai.flag = True
        current_move = ai.optimal_policy[current_position]
        previous_move = current_move
        # pseudo
        # if we reached a goal then make sure to remove the item at theat point
        # and then recall the mdp

        match current_move:
           case "right":
              self.game.on_key_press(arcade.key.RIGHT, None)      
           case "left":
              self.game.on_key_press(arcade.key.LEFT, None)      
           case "down":
              self.game.on_key_press(arcade.key.DOWN, None)
           case "up":
              self.game.on_key_press(arcade.key.UP, None)
           case "jump_left":
              if previous_move == "left":
                  self.game.on_key_press(arcade.key.SPACE, None)
              else:
                  self.game.on_key_press(arcade.key.LEFT, None)
                  self.game.on_key_press(arcade.key.SPACE, None)
           case "jump_right":
              if previous_move == "right":
                  self.game.on_key_press(arcade.key.SPACE, None)
              else:
                  self.game.on_key_press(arcade.key.RIGHT, None)
                  self.game.on_key_press(arcade.key.SPACE, None)


        return


    def run(self):
        print("Starting " + self.name)

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50+320, 50)
        if self.show_grid_info:
            pygame.init()

        # Prepare grid information display (can be turned off if performance issue exists)
        if self.show_grid_info:
            screen_size = [200, 120]
            backscreen_size = [40, 12]

            screen = pygame.display.set_mode(screen_size)
            backscreen = pygame.Surface(backscreen_size)
            arr = pygame.PixelArray(backscreen)
        else:
            time.sleep(0.5)  # wait briefly so that main game can get ready
            
        # roughly every 50 milliseconds, retrieve game state (average human response time for visual stimuli = 25 ms)
        go = True
        while go and (self.game is not []):
            # Dispatch events from pygame window event queue
            if self.show_grid_info:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        go = False
                        break
                        
            if self.game is []:
                break

            # RETRIEVE CURRENT GAME STATE
            self.move_grid, self.kill_grid, \
                self.isGameClear, self.isGameOver, go, self.current_stage, self.time_limit, \
                self.total_score, self.total_time, self.total_life, self.tanuki_r, self.tanuki_c \
                = self.game.get_game_state()

            self.ai_function()

            # Display grid information (can be turned off if performance issue exists)
            if self.show_grid_info:
                for row in range(12):
                    for col in range(20):
                        c = self.move_grid[row][col] * 255 / 12
                        arr[col, row] = (c, c, c)
                    for col in range(20, 40):
                        if self.kill_grid[row][col-20]:
                            arr[col, row] = (255, 0, 0)
                        else:
                            arr[col, row] = (255, 255, 255)

                pygame.transform.scale(backscreen, screen_size, screen)
                pygame.display.flip()

            # We must allow enough CPU time for the main game application
            # Polling interval can be reduced if you don't display the grid information
            time.sleep(0.05)

        print("Exiting " + self.name)


def main():
    ag = Agent(1, "My Agent", 1, True)

    ag.game = game_core.GameMain()
    ag.game.set_location(50, 50)

    # Uncomment below for recording
    # ag.game.isRecording = True
    # ag.game.replay('replay.rpy')  # You can specify replay file name or it will be generated using timestamp

    # Uncomment below to replay recorded play
    # ag.game.isReplaying = True
    # ag.game.replay('replay.rpy')

    ag.game.reset()
    ag.start()
    arcade.run()


if __name__ == "__main__":
    main()
