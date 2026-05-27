import json

def search(title_query):
    # load data/moves.json
    with open('data/movies.json', 'r') as f:
        movies = json.load(f)
#    print(movies["movies"][0]["title"])

    # create results list
    results = []

    # iterate over movies and find matching queries
    for movie in movies["movies"]:
        if title_query in movie["title"]:
            results.append(movie["title"])

    return results
