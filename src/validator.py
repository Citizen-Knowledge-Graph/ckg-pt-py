from src.models.person import Person
from src.models.person_query import PersonQuery


def validate(person: Person, query: PersonQuery):
    constraint_violations = []
    for domain, constraint in query.__dict__.items():
        match domain:
            case "target_type":
                if person.type != constraint:
                    constraint_violations.append(domain)

            case "personal_data":
                for _property, condition in constraint.__dict__.items():
                    validation_property = person.personal_data.__dict__[_property]
                    match condition.constraint_type:
                        case "min":
                            if not validation_property >= condition.constraint_features.min:
                                constraint_violations.append(condition)
                        case "max":
                            if not validation_property <= condition.constraint_features.max:
                                constraint_violations.append(condition)
                        case "min_max":
                            if (not validation_property >= condition.constraint_features.min
                                    and validation_property <= condition.constraint_features.max):
                                constraint_violations.append(condition)
                        case _:
                            print('default')

    if len(constraint_violations) > 0:
        print("Validation failed with constraint violations:", constraint_violations)
        raise Exception("Validation failed")
    print("Validation passed")
