import json

from src.models.person import Person, PersonParser
from src.models.query import Query, QueryParser
from src.validator import validate

# load profile from file
path = "db/profiles/citizen-a.json"
person: Person = PersonParser.validate_python(json.load(open(path)))
print("Loading person:", person)

# load query from file
path = "db/queries/ecar-funding.json"
query: Query = QueryParser.validate_python(json.load(open(path)))
print("Loading query:", query)

# # validate person against query
validate(person, query)
