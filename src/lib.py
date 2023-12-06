import json

from src.models.person import Person, PersonParser
from src.models.person_query import PersonQuery, PersonQueryParser
from src.validator import validate

# load profile from file
path = "../db/profiles/citizen-a.json"
person: Person = PersonParser.validate_python(json.load(open(path)))
print("Loading person:", person)

# load query from file
path = "../db/queries/solar-funding.json"
query: PersonQuery = PersonQueryParser.validate_python(json.load(open(path)))
print("Loading person query:", query)

# # validate person against query
validate(person, query)
