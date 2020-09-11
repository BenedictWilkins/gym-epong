#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 08-09-2020 16:28:49

    [Description]
"""
__author__ = "Benedict Wilkins"
__email__ = "benrjw@gmail.com"
__status__ = "Development"

import gym
import numpy as np
import copy

class Object:

    def __init__(self, p, size, v=np.array([0,0],dtype=np.float32)):
        self.p = p
        self.size = size
        self.v = v

    def update(self):
        self.p += self.v 

class EPong(gym.Env):

    def __init__(self, size=(64,64)):
        self.state = np.zeros((3,size[1],size[0]), dtype=np.float32)  # CHW format
        

        margin = size[0] // 12

        self.player1 = Object(np.array([margin, size[1]/2 -  size[1]//16]), np.array([size[0]//32, size[0]//8]))
        self.place_obj(self.state, self.player1)

        self.player2 = Object(np.array([size[0] - margin - size[0]//32, size[1]/2 - size[1]//16]), np.array([size[0]//32, size[1]//8]))
        self.place_obj(self.state, self.player2)

        ball_size = min(size) // 32
        self.ball = Object(np.array([size[0]//2 - ball_size / 2, size[1]//2 - ball_size / 2]), 
                           np.array([ball_size,ball_size]))

        self.place_obj(self.state, self.ball)

        self.physics = np.array([[0,-1], [0,1], [0,0]]) # UP, DOWN, NOOP
        self.player_speed = 1
        self.ball_speed = 3
        self.max_angle = 70 * np.pi / 180.

        self.ball.v = np.array([-1,0]) * self.ball_speed

        self.action_space = gym.spaces.Discrete(self.physics.shape[0])
        self.observation_space = gym.spaces.Box(np.float32(0), np.float32(1), shape=self.state.shape, dtype=np.float32)

        self.__initial_state = copy.deepcopy((self.player1, self.player2, self.ball))

    def place_obj(self, state, obj):
        p = obj.p.astype(np.int64)
        s = obj.size.astype(np.int64)
        state[:, p[1]:p[1]+s[1], p[0]:p[0]+s[0]] = 1.

    def bounce_velocity(self, player, ball):
        pass


    def action_meanings(self):
        return ["UP", "DOWN", "NOOP"]

    def step(self, action):
        done, reward = False, 0.
        self.state = np.zeros_like(self.state)
        self.player1.v = self.physics[action] * self.player_speed
        self.player2.v = self.physics[action] * self.player_speed

        #check collision with player1
        if self.player1.p[0] + self.player1.size[0] >= self.ball.p[0] and self.player1.p[0] <= self.ball.p[0] + self.ball.size[0]:
            
            if self.ball.p[1] + self.ball.size[1] > self.player1.p[1] and self.ball.p[1] < self.player1.p[1] + self.player1.size[1]:
                iby = self.ball.p[1] + self.ball.size[1] / 2
                ipy = self.player1.p[1] + self.player1.size[1] / 2
                iry = self.max_angle * (ipy - iby)  / (self.player1.size[1] / 2)
                self.ball.v = self.ball_speed * np.array([np.cos(iry), -np.sin(iry)])

        #check collision with player2
        if self.player2.p[0] == self.ball.p[0] + self.ball.size[0]:
            pass
        
        # check collesion with upper/lower walls
        if self.ball.p[1] + self.ball.v[1] <= 0:
            self.ball.v[1] = - self.ball.v[1]
        elif self.ball.p[1] + self.ball.size[1] + self.ball.v[1] >= self.state.shape[1]:
            self.ball.v[1] = - self.ball.v[1]

        print(self.player1.p, self.player1.v, self.ball.p)

        self.player1.update()
        self.player2.update()
        self.ball.update()
        
        self.place_obj(self.state, self.player1)
        self.place_obj(self.state, self.player2)
        self.place_obj(self.state, self.ball)

        if self.ball.p[0] <= 0:
            done, reward = True, 1.
        elif self.ball.p[0] + self.ball.size[0] >= self.state.shape[2]:
            done, reward = True, -1.

        return self.state, reward, done, None

    def reset(self):
        self.state = np.zeros_like(self.state)
        self.player1, self.player2, self.ball = copy.deepcopy(self.__initial_state)

        self.place_obj(self.state, self.player1)
        self.place_obj(self.state, self.player2)
        self.place_obj(self.state, self.ball)

        return self.state

    def render(self, *args, **kwargs):
        pass
        