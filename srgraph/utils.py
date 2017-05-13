import pandas as pd
import networkx as nx
import numpy as np
master_df = pd.read_pickle('master_df.p')
master_df_ = master_df[master_df.notnull()]

master_df_u = master_df_.drop_duplicates('subreddit')
master_df_u = master_df_u.drop(master_df_u.index[master_df_u.subreddit=='/r/track__subreddits_'])
graph = {x:y for x, y in zip(master_df_u.subreddit, master_df_u.related)}

G=nx.Graph()
G=nx.from_dict_of_lists(graph)
#making the graph undirected takes all of the vertices between nodes and makes them bi-directional
G1 = G.to_undirected()


def short_path():
    choices = np.random.choice(master_df_u.subreddit, 2)
    if nx.has_path(G1, choices[0], choices[1]) == True:
        path = nx.shortest_path(G1, choices[0], choices[1])
        return choices[0] + ' and ' + choices[1] + ' are joined by: \n' + str(path)
    else:
        return "No path exists between " + choices[0] + ' and ' + choices[1]


def graph_():

    print("OK")
    return short_path()
