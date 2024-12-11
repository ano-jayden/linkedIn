import spacy


nlp = spacy.load('en_core_web_sm')


def read_movies(file_path):
    movies = {}
    with open(file_path, 'r') as file:
        for line in file:
            title, description = line.split(':', 1)
            movies[title.strip()] = description.strip()
    return movies


def find_most_similar_movie(user_description, movies):
    user_doc = nlp(user_description)
    max_similarity = -1
    most_similar_title = None

    for title, description in movies.items():
        movie_doc = nlp(description)
        similarity = user_doc.similarity(movie_doc)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_title = title

    return most_similar_title

if __name__ == '__main__':
    
    movies = read_movies('movies.txt')

    planet_hulk_description = (
        "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, "
        "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. "
        "Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    )


    similar_movie = find_most_similar_movie(planet_hulk_description, movies)
    print(f"The most similar movie to 'Planet Hulk' is: {similar_movie}")
