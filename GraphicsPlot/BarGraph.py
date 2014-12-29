__author__ = 'gk'

# Draws Bar graph with a given user Rank List

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def barPlot(userRankList,topX=15):
    people = list()
    score = list()
    if len(userRankList) >= topX:
        size = topX
    else:
        size = len(userRankList)
    for user in userRankList[:size]:
        people.append(user.name)
        score.append(user.score)
    x_pos = np.arange(len(people))
    ind = np.arange(len(people))
    width = 0.2
    fig,ax = plt.subplots()
    ax.bar(x_pos,score,align='center')
    ax.set_xticks(ind+width*1.0)
    plt.ylabel('PageRank Score')
    plt.xticks(x_pos,people,rotation='vertical')
    title = "Top " + repr(size) + " Twitter Users Rank"
    plt.title(title)
    plt.subplots_adjust(left=0.20,bottom=0.28)
    plt.show()