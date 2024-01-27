import json

from data_scrubbing import ACTORS_FILM, ACTORS_DIRECTOR, ACTOR_ACTOR
import pandas as pd


def actor_actor_film():
    """
    In this function, using the ACTORS_FILM data, we can find the relationship
    between the actors using the films they participated in.
    And we save the extracted data in csv and json formats in the archive/actor_actor_film path.
    """
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
    print(f"Data saved in json format successfully.\n{"__"*25}")


def actor_actor_director():
    """
    In this function, using ACTORS_DIRECTOR data, we can find the relationship
    between actors using the director they worked with.
    And we save the extracted data in csv and json formats in the archive/actor_actor_director path.
    """
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
    print(f"Data saved in json format successfully.\n{"__"*25}")


def actor_actor():
    """
    In this function, by using the ACTOR_ACTOR data, we can use the data to show the
    relationship of the actors through which actors have collaborated together.
    And we save the extracted data in csv and json formats in the archive/actor_actor path.
    """
    communication_actors = {}

    for actor1, actor1_re in ACTOR_ACTOR.items():
        for actor2, actor2_re in ACTOR_ACTOR.items():
            common_actors = set(actor1_re).intersection(actor2_re)
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
    csv_file_path = "archive/actor_actor/actors_relations.csv"
    df.to_csv(csv_file_path, index=False, encoding='utf-8')
    print("Data saved in csv format successfully.")

    # save file json
    json_file_path = "archive/actor_actor/actors_relations.json"
    with open(json_file_path, mode='w', encoding='utf-8') as file:
        json.dump(communication_actors, file, ensure_ascii=False, indent=2)
    print(f"Data saved in json format successfully.\n{"__"*25}")


if __name__ == "__main__":
    actor_actor_film()
    actor_actor_director()
    actor_actor()
