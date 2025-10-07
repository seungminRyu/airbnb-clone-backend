import strawberry
import typing


@strawberry.type
class Movie:
    pk: int
    title: str
    year: int
    rating: int


movie_db = [
    Movie(pk=1, title="Godfather", year=1990, rating=10),
]


def movies() -> typing.List[Movie]:
    return movie_db


def movie(movie_pk: int) -> Movie:
    return movie_db[movie_pk - 1]


@strawberry.type
class Query:
    movies: typing.List[Movie] = strawberry.field(resolver=movies)
    movie: Movie = strawberry.field(resolver=movie)


def add_movie(title: str, year: int, rating: int) -> Movie:
    new_movie = Movie(
        pk=len(movie_db) + 1,
        title=title,
        year=year,
        rating=rating,
    )
    movie_db.append(new_movie)
    return new_movie


@strawberry.type
class Mutation:
    add_movie: Movie = strawberry.mutation(resolver=add_movie)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
