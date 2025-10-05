import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def ping(self) -> str:
        return "pong"

    @strawberry.field
    def hello(self, name: str = "world!") -> str:
        return f"Hello, {name}"


schema = strawberry.Schema(query=Query)
