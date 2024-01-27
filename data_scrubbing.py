import pymongo
from config import HOST_PORT, DATABASE_NAME, COLLECTION_NAME


FILM_STARS = {}
FILM_IMDB = {}
ACTORS_FILM = {}
ACTORS_DIRECTOR = {}
ACTORS = []
FILMS = []
DIRECTORS = []


def _get_datas():
    client = pymongo.MongoClient(HOST_PORT)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    global ACTORS, DIRECTORS, FILMS, ACTORS_DIRECTOR, ACTORS_FILM, FILM_IMDB, FILM_STARS

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

            if data['director'] != None:
                if actor not in ACTORS_DIRECTOR.keys():
                    ACTORS_DIRECTOR[actor] = [data["director"]]
                elif data["director"] not in ACTORS_DIRECTOR[actor]:
                    ACTORS_DIRECTOR[actor].append(data["director"])

    ACTORS = set(n_actors)
    DIRECTORS = set(n_director)

    client.close()


_get_datas()
