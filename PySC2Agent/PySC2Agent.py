import sc2reader
import sparse_agent as sa
from sparse_agent import QLearningTable as qt

replay = sc2reader.load_replay('C:/Users/Faminova_Y/Desktop/maga/roman.SC2Replay', load_map=True)
act = ['ACTION_DO_NOTHING','ACTION_BUILD_SUPPLY_DEPOT','ACTION_BUILD_BARRACKS','ACTION_BUILD_MARINE','ACTION_ATTACK']
qlearn = qt(actions=list(range(8)))
filepath = 'C:/Users/Faminova_Y/Desktop/maga/out.csv'
#qlearn.learn(str(state), act, 0.3, 'terminal')
#state = [1,2,3,4,5,6,7,8,9,10,11,2]
#qlearn.learn(str(state), act, 0.4, 'terminal')

events = [i for i in replay.events if i.name in act]
#print([i.killed_units for i in replay.players[0].units])
units1 = replay.players[0].units
cc_supDep = 0
cc_barrack = 0
cc_marine = 0
state = [cc_supDep,cc_barrack,cc_marine,units1[0].location[0],units1[0].location[1],0,0,0,0,0,0,0]
previous_state = 'terminal'
for un in units1:
    if un.name == 'SupplyDepotLowered':
        a = 1
        state[0] += 1
        state[3] = un.location[0]
        state[4] = un.location[1]
        qlearn.learn(str(previous_state), a, 0.2, 'terminal')
    if un.name == 'Barracks':
        a = 2
        state[1] += 1
        state[3] = un.location[0]
        state[4] = un.location[1]
        qlearn.learn(str(previous_state), a, 0.2, 'terminal') 
    if un.name == 'Marine':
        a = 3
        state[2] += 1
        state[3] = un.location[0]
        state[4] = un.location[1]
        qlearn.learn(str(previous_state), a, 0.2, 'terminal')
    if un.killed_units:
        a = 4
        state[3] = un.location[0]
        state[4] = un.location[1]
        for en_un in un.killed_units:
            state[5] = en_un.location[0]
            state[6] = en_un.location[1]
            qlearn.learn(str(previous_state), a, 0.3, 'terminal')
        state[5] = 0
        state[6] = 0
    previous_state = state

df = qlearn.q_table
df.to_csv(filepath)  


#print([i.units for i in replay.events if i.name==act[2]])
#print([i for i in replay.events if i.name==act[0] and i.unit.owner][0].__dict__.keys())
#for i in events:
#    if i.name == act[2] and i.unit.owner.sid == 1:
#        state[4] = i.x
#        state[5] = i.y
#   if i.name == act[0] and i.unit.owner.sid == 1:
#       a = 1
#       state[0] = 
#


#print([i for i in replay.events])

#replay = sc2reader.load_replay('C:/Users/Faminova_Y/Desktop/maga/roman.SC2Replay', load_map=True)
#print(replay.__dict__.keys())
#values = set(map(lambda x:x.name, replay.events))
#print(values)
#print([i.unit for i in replay.events if i.name in ['UnitBornEvent','UnitDiedEvent','UnitPositionEvent']])
#print([i.unit.type_history for i in [i for i in replay.events if i.name=='SetControlGroupEvent'] if i.unit_type_name == 'MineralField750'])
#print([i for i in replay.events if i.name=='GetControlGroupEvent'][0].__dict__.keys())
#print(replay.player[2].units)
#born_units = [i for i in replay.player[1].events]
#unit_types = set(map(lambda x:x, born_units))
#print([[i,i.__dict__.keys()] for i in unit_types])
#values = set(map(lambda x:x.id, replay.players[0].units))
#print((replay.end_time - replay.start_time).total_seconds())
#print([i.name for i in replay.events if i.id in values])
#values2 = set(map(lambda x:x.id, replay.players[1].units))
#values2 = []
#print([i.frame for i in replay.events])
#print(replay.player[1].units[1].id)
#print(replay.map.__dict__.keys())
#print([i for i in replay.events if i.name=='PlayerSetupEvent'][0].__dict__.keys())
#print([i for i in replay.events if i.name=='PlayerSetupEvent'][0].pid)
#print(replay.build)