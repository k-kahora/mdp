# The sprite data and level design were adopted from <Bong Bong> (1989) written by
# T.K. Lee while in Computer Science Department at Yonsei University, Korea.
# The program and the data had been open-sourced in a Korean online game community.
# Python scripts were written from scratch, but the data below was excerpted from the 1989 game.
#
# <Bong Bong> was a remake of <PONPOKO (ポンポコ)> (1982) from Sigma Enterprise, Japan.
# More about the original game can be found here: https://en.wikipedia.org/wiki/Ponpoko

data_path = 'data/'  # base image path

time_limit = 100  # each stage should be completed within 100 seconds
time_bonus = 100  # upon completion of each stage, (remaining seconds)x(time_bonus) is time bonus

life_limit = 3    # max number of trials

img_world = ['01.png',  # background
             '02.png', '03.png', '04.png', '05.png',  # left / right / rectangle / island platform
             '06.png',  # ladder
             '07.png',  # needle
             '08.png']  # bonus

img_tanuki = [['tl.png', ['tlj1.png', 'tlj2.png']],  # left / left jump motions
              ['tr.png', ['trj1.png', 'trj2.png']],  # right / right jump motions
              'to.png',  # up motion
              ['tx1.png', 'tx2.png', 'tx3.png', 'tx4.png', 'tx5.png'],  # dead / fall animation
              ['al.png', 'ar.png'],  # left / right small bonus
              ['bl.png', 'br.png']]  # left / right large bonus

img_enemy1 = [['cl1.png', 'cl2.png'],  # left motion
              ['cr1.png', 'cr2.png']]  # right motion

img_enemy2 = ['el.png', 'er.png']  # left / right

img_fruit = ['f0.png', 'f1.png', 'f2.png', 'f3.png', 'f4.png',
             'f5.png', 'f6.png', 'f7.png', 'f8.png', 'f9.png']  # fruit images of all stages

enemy_speeds = [[0, 0, 0, 0, 0]]  # enemy2 information (location / speed) followed by enemy1 information (speed)

# Stage Information: Each stage is (rows x cols) = (12 x 20) cells
# .	empty
# 2	platform / left half-circle
# 3	platform / right half-circle
# 4	platform / rectangle
# 5	platform / island
# 6	ladder
# 7	needle
# #	target (100 points)
# a	bonus (500 points)
# b	bonus (1000 points)
# c	enemy1 (always appear on the right)
stages = [
    ['....................',
     '....................',
     '4644444644444444444.',
     '.6.....6............',
     '.6.....6............',
     '4444446444444444464.',
     '......6..........6..',
     '#.....6..........6..',
     '4444644444444446444.',
     '....6..........6....',
     '....6..........6....',
     '44444444444444444444']  # stage 1
]
