import strawberry

#Output Type (for Queries/Mutations responses)
@strawberry.type
class UserType:
    id: int
    email: str
    first_name: str

#Input Type (for Mutation arguments)
@strawberry.input
class UserInput:
    email: str
    password: str
    first_name: str
    last_name: str
    phone_number: str