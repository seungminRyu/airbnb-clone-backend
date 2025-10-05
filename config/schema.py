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


@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> typing.List[Movie]:
        return movie_db

    @strawberry.field
    def movie(self, movie_pk: int) -> Movie:
        return movie_db[movie_pk - 1]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_movie(
        self,
        title: str,
        year: int,
        rating: int,
    ) -> Movie:
        new_movie = Movie(
            pk=len(movie_db) + 1,
            title=title,
            year=year,
            rating=rating,
        )
        movie_db.append(new_movie)
        return new_movie


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
