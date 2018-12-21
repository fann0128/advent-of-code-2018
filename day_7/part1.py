from sets import Set

file = 'example_input.txt'
# file = 'input.txt'

res = ''

with open(file, 'r') as myfile :
    steps = myfile.readlines()

for idx, step in enumerate(steps) :
    steps[idx] = [step.split(' must be finished before step ')[0].replace('Step ',''), step.split(' must be finished before step ')[1].replace(' can begin.','').replace('\n', '')]

def get_next_step(steps) :
    next_steps = Set([])
    blocked_steps = Set([])
    for x in range(len(steps)) :
        next_steps.add(steps[x][0])
        blocked_steps.add(steps[x][1])
    if len(blocked_steps) :
        return next_steps.difference(blocked_steps)
        
print (get_next_step(steps))

# while (len(steps)) :
#     # get the first entry, for each in side of the
#     if (next_step) :
#         print(next_step)
#     else :
        

#     print(steps[len(steps) - 1])
#     steps.pop()

# blocked_steps = blocked_steps.union(starting_steps)

# print(start_step)
# print(blocked_steps)
# print(ending_steps_list)

# get_next_step(starting_steps_list[0], steps, starting_steps_list, blocked_steps_list, ending_steps_list)

# [['A', 'B'],
#  ['C', 'A'],
#  ['C', 'F'],
#  ['A', 'D'],
#  ['B', 'E'],
#  ['D', 'E'],
#  ['F', 'E']]

# c a b e
# c a d e
# c f e