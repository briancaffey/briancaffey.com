import pandas as pd
import networkx as nx
import numpy as np
from .models import Subreddit

#import the dataframe from pickle file and filter out null values
master_df = pd.read_pickle('master_df.p')
master_df_ = master_df[master_df.notnull()]

#cleanup and remove duplicates in the pandas dataframe
master_df_u = master_df_.drop_duplicates('subreddit')
master_df_u = master_df_u.drop(master_df_u.index[master_df_u.subreddit=='/r/track__subreddits_'])
graph = {x:y for x, y in zip(master_df_u.subreddit, master_df_u.related)}

G=nx.Graph()
G=nx.from_dict_of_lists(graph)
#making the graph undirected takes all of the vertices between nodes and makes them bi-directional
G1 = G.to_undirected()

def path(sr_one, sr_two):
    data = {'one':sr_one, 'two':sr_two}
    if nx.has_path(G1, sr_one, sr_two):
        path = [x+'\n' for x in nx.shortest_path(G1, sr_one, sr_two)]
        data['path'] = path
        collection = list(Subreddit.objects.filter(name__in=path))
        collection.sort(key=lambda t:path.index(t.name))
        data['collection']  = collection
        return data
