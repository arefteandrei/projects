from pymongo import MongoClient

client = MongoClient()
db = client.test

film_title = input("Enter film title: ")
movie_type = input("Enter movie type: ")
launch_year = input("Enter launch year: ")

films = db.films
film_details = {
    'film_title': film_title,
    'type': movie_type,
    'launch_year': launch_year
}

films.insert_one(film_details)

result = films.find()

for i in result:
    print("FilmTitle: {} | MovieType: {} | LaunchYear: {}".format(i['film_title'], i['movie_type'], i['launch_year']))

