import networkx as nx
import matplotlib.pyplot as plt
import json

with open('imdb_movies.json', 'r') as file:
    movies_data = json.load(file)

G = nx.DiGraph()

for movie in movies_data:
    actors = movie["actors"]
    # for actor_data in actors:
    #     actor_id, actor_name = actor_data
    #     G.add_node(actor_id, name=actor_name)
    #     for other_actor_data in actors:
    #         other_actor_id, _ = other_actor_data
    #         if actor_id != other_actor_id:
    #             G.add_edge(actor_id, other_actor_id)

