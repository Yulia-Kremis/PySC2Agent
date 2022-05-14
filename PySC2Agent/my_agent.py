import random
import math
import os

import numpy as np
import pandas as pd
from IPython.display import display

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

class SparseAgent(base_agent.BaseAgent):
    def __init__(self):
        super(SparseAgent, self).__init__()
        
        self.qlearn = QLearningTable(actions=list(range(len(smart_actions))))
        
        self.previous_action = None
        self.previous_state = None
        
        self.cc_y = None
        self.cc_x = None
        
        self.move_number = 0
        
        if os.path.isfile(DATA_FILE + '.gz'):
            self.qlearn.q_table = pd.read_pickle(DATA_FILE + '.gz', compression='gzip')
