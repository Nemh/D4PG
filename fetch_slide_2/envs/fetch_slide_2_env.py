import os
import numpy as np

from gym.utils import EzPickle
from gym.envs.robotics.fetch_env import FetchEnv

# Ensure we get the path separator correct on windows
MODEL_XML_PATH = os.path.join('fetch', 'slide.xml')

class FetchSlide2(FetchEnv, EzPickle):
   def __init__(self, reward_type='sparse', assets_file='slide.xml'):
       '''
       slide2.xml: deformable
       slide3.xml: normal but with surrounding box
       '''
       initial_qpos = {
           'robot0:slide0': 0.05,
           'robot0:slide1': 0.48,
           'robot0:slide2': 0.0,
           'object0:joint': [1.32441906, 0.75018422, 0.5, 1., 0., 0., 0.],
       }
       self.max_angle = 25. / 180. * np.pi
       FetchEnv.__init__(
           self, 'fetch/{}'.format(assets_file),
           has_object=True, block_gripper=True, n_substeps=20,
           gripper_extra_height=-0.02, target_in_the_air=False, target_offset=np.array([0.4, 0.0, 0.0]),
           obj_range=0.1, target_range=0.3, distance_threshold=0.05,
           initial_qpos=initial_qpos, reward_type=reward_type)
       EzPickle.__init__(self)
