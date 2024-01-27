import pymongo
from config import HOST_PORT, DATABASE_NAME, COLLECTION_NAME
# example: HOST_PORT = "localhost:27017"; DATABASE_NAME = "....."; COLLECTION_NAME = "...."

FILM_STARS = {}
FILM_IMDB = {}
ACTORS_FILM = {}
ACTORS_DIRECTOR = {}
ACTOR_ACTOR = {}
ACTORS = []
FILMS = []
DIRECTORS = []


def _get_datas():
    """
    In this function, we load the movie information using the pymongo library. Then we
    extract the following information from these loaded data:

    1: ACTORS_FILM: Here we have shown which movies each actor has acted in. Its format is:
    {
    "actor1": ["film1", "film2", ...],
    "actor2": ["film1", "film3", ...],
    ...
    }

    2: ACTORS_DIRECTOR: Here we show which directors each actor has worked with. Its format is:
    {
    "actor1": ["director1", "directo2", ...],
    "actor2": ["director1", "director3", ...],
    ...
    }

    3: ACTOR_ACTOR: Here we show which actors each actor has co-starred with. Its format is:
    {
    "actor1": ["actor2", "actor3", ...],
    "actor2": ["actor1", ...],
    "actor3": ["actor1", ...],
    ...
    }
    """

    client = pymongo.MongoClient(HOST_PORT)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    global ACTORS, DIRECTORS, FILMS, ACTORS_DIRECTOR, ACTORS_FILM, FILM_IMDB, FILM_STARS, ACTOR_ACTOR

    result = collection.find()

    n_actors = []
    n_director = []

    for data in result:
        FILM_STARS[data["name"]] = data["stars"].split(", ")
        FILM_IMDB[data["name"]] = float(data["IMDB"].split("/")[0])
        actors = data["stars"].split(", ")
        n_actors.extend(actors)
        FILMS.append(data["name"])

        if data["director"] != None:
            n_director.append(data["director"])

        for actor in actors:
            if actor not in ACTORS_FILM.keys():
                ACTORS_FILM[actor] = [data["name"]]
            else:
                ACTORS_FILM[actor].append(data["name"])

            if actor not in ACTOR_ACTOR.keys():
                t = actors.copy()
                t.remove(actor)
                ACTOR_ACTOR[actor] = t
            else:
                t = actors.copy()
                t.remove(actor)
                ACTOR_ACTOR[actor].extend(t)

            if data['director'] != None:
                if actor not in ACTORS_DIRECTOR.keys():
                    ACTORS_DIRECTOR[actor] = [data["director"]]
                elif data["director"] not in ACTORS_DIRECTOR[actor]:
                    ACTORS_DIRECTOR[actor].append(data["director"])

    for actor in ACTOR_ACTOR.keys():
        ACTOR_ACTOR[actor] = set(ACTOR_ACTOR[actor])

    ACTORS = set(n_actors)
    DIRECTORS = set(n_director)

    client.close()


_get_datas()
