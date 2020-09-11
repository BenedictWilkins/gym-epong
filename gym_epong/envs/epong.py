#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 08-09-2020 16:28:49

    [Description]
"""
__author__ = "Benedict Wilkins"
__email__ = "benrjw@gmail.com"
__status__ = "Development"

from .. import utils

import gym
import numpy as np

class EPong(gym.Env):

    def __init__(self):
        pass 

    def action_meanings(self):
        return ["UP", "DOWN", "NOOP"]

    def step(self, action):
        pass 

    def reset(self):
        pass

    def render(self, *args, **kwargs):
        pass
        