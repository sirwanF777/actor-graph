import json

from data_scrubbing import ACTORS_FILM, ACTORS_DIRECTOR, FILMS, DIRECTORS
import pandas as pd


def actor_actor_film():
    communication_actors = {}

    for actor1, films1 in ACTORS_FILM.items():
        for actor2, films2 in ACTORS_FILM.items():
            common_actors = set(films1).intersection(films2)
            if common_actors and actor1 != actor2:
                if actor1 in communication_actors.keys():
                    communication_actors[actor1].append(actor2)
                else:
                    communication_actors[actor1] = []

    node_size = len(communication_actors.keys())
    edge_size = sum([len(i) for i in communication_actors.values()])
    print(f"node size: {node_size}\nedge size: {edge_size}\n")

    # save file "csv"
    df = pd.DataFrame([(actor, relation) for actor, relations in communication_actors.items() for relation in relations],
                      columns=["actor", "Relationship"])
    csv_file_path = "archive/actor_actor_film/actors_relations.csv"
    df.to_csv(csv_file_path, index=False, encoding='utf-8')
    print("Data saved in csv format successfully.")

    # save file json
    json_file_path = "archive/actor_actor_film/actors_relations.json"
    with open(json_file_path, mode='w', encoding='utf-8') as file:
        json.dump(communication_actors, file, ensure_ascii=False, indent=2)
    print("Data saved in json format successfully.")


def actor_actor_director():
    communication_actors = {}

    for actor1, director1 in ACTORS_DIRECTOR.items():
        for actor2, director2 in ACTORS_DIRECTOR.items():
            common_actors = set(director1).intersection(director2)
            if common_actors and actor1 != actor2:
                if actor1 in communication_actors.keys():
                    communication_actors[actor1].append(actor2)
                else:
                    communication_actors[actor1] = []

    node_size = len(communication_actors.keys())
    edge_size = sum([len(i) for i in communication_actors.values()])
    print(f"node size: {node_size}\nedge size: {edge_size}\n")

    # save file "csv"
    df = pd.DataFrame(
        [(actor, relation) for actor, relations in communication_actors.items() for relation in relations],
        columns=["actor", "Relationship"])
    csv_file_path = "archive/actor_actor_director/actors_relations.csv"
    df.to_csv(csv_file_path, index=False, encoding='utf-8')
    print("Data saved in csv format successfully.")

    # save file json
    json_file_path = "archive/actor_actor_director/actors_relations.json"
    with open(json_file_path, mode='w', encoding='utf-8') as file:
        json.dump(communication_actors, file, ensure_ascii=False, indent=2)
    print("Data saved in json format successfully.")


if __name__ == "__main__":
    actor_actor_director()
