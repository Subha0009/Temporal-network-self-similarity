from configs import babu_config as config   # import configs for corresponding data file

import resource
import glob
#resource.setrlimit(resource.RLIMIT_AS, (int(6e9),int(6e9)))
from boxes import boxes
import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
import pickle
from multiprocessing import Process
import os
if not os.path.exists(config['save_path']):
    os.makedirs(config['save_path'])
####################### Network generation ####################################

E = []
with open(config['FILENAME'], 'r') as f:
  for line in f.read().split('\n'):
    if len(line.split(config['DELIM']))==config['LINELEN'] and int(line.split(config['DELIM'])[2])>=config['S'] and int(line.split(config['DELIM'])[2])<config['S']+config['Delta']:
      E.append((int(line.split(config['DELIM'])[0]), int(line.split(config['DELIM'])[1]), int(line.split(config['DELIM'])[config['TPOS']])))
#print("File reading complete")
###########################Box covering and plot#########################


def get_boxes(box_size, time_size, start, end):
  time_size *= config['TS']
  print('Running for time size {} days'.format(time_size/config['TS']))
  num_boxes = {(box_size, time_size):[]}
  t = start
  count = 0
  while t<end:
    G = nx.Graph()
    for edge in E:
      if edge[-1]>=t and edge[-1]<t+time_size:
        G.add_edge(edge[0], edge[1])
    t += time_size
    comps = sorted(nx.connected_components(G), key=len, reverse=True)
    #c_sizes = [len(c) for c in comps]
    #print("Time size {}; Component sizes {}".format(time_size, c_sizes))
    #for c in comps:
    if len(comps):
      count += 1
      G0 = G.subgraph(comps[0])
      N_0 = len(G0)
      G0 = boxes.network(G0)
      num_boxes[(box_size, time_size)].append([boxes.memb(G0, box_size,boxing=True), N_0])
      print("Done for time size {} box size {} {} of {}".format(time_size/config['TS'], box_size, count, (end-start)/time_size))
  with open(config['save_path']+'/results-{}.pkl'.format(time_size), 'wb') as f:
    pickle.dump(num_boxes, f)
  return num_boxes

for dt, b in config['boxlist']:
  get_boxes(b, dt, config['S'], config['S']+config['Delta'])
