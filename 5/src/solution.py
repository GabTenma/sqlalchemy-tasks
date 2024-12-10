from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie, Director
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def get_movies_with_directors(session):
    query = select(Movie.title, Movie.release_date, Movie.duration, Movie.genre, Movie.rating, Director.name) \
        .select_from(Movie) \
        .join(Director, Movie.director_id == Director.id) \
        .order_by(Movie.title)

    movies_with_directors = session.execute(query).fetchall()

    formatted_movies = [
        f"{movie[0]} by {movie[5]}, released on {movie[1]}, duration: {movie[2]} min, genre: {movie[3]}, rating: {movie[4]}"
        for movie in movies_with_directors
    ]

    return formatted_movies
# END
