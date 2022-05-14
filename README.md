# PySC2Agent
create SC2 agent using Q-Learning

The project contains 3 test SC2 agents: simple_agent,smart_agent,sparse_agent. 

The following line is used to start the agent:
python -m pysc2.bin.agent --map Tarialis --agent PySC2Agent.sparse_agent.SparseAgent --agent_race zerg --max_agent_steps 0 -norender

Requirements:
1. installed game StarCraft II
2. download map Tarialis and add it to repository C:\Program Files (x86)\StarCraft II\Maps
3. open file in Python\Python39\Lib\site-packages\pysc2\maps\melee.py , find the definition of list melee_maps and add to it "Tarialis"
4. Python 3.9..., PySC2 3.0..., 
