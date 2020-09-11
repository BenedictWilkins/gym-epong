import os
from gym.envs.registration import register

from . import envs
from .utils import maps

_all__ = ('envs', )

register(
    id='epong-v0',
    entry_point='gym_epong.envs:EPong'
)

