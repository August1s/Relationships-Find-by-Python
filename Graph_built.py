#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
from pylab import mpl


def Graph_show():
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
    G=nx.Graph()
    # 在NetworkX中，节点可以是任何哈希对象，像一个文本字符串，一幅图像，一个XML对象，甚至是另一个图或任意定制的节点对象
    with open('e:/PY/relationship_find/edge.txt','r') as f:
        for i in f.readlines():
            line=str(i).split()
            if line == []:
                continue
            if int(line[2])<=50:
                continue
            G.add_weighted_edges_from([(line[0],line[1],int(line[2]))])
    nx.draw(G,pos=nx.shell_layout(G),node_size=1000,node_color = '#A0CBE2',edge_color='#A0CBE1',with_labels = True,font_size=12)
    plt.show()