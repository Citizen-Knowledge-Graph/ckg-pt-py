from src.models.person import Person
from src.models.query import Query


def validate(person: Person, query: Query):
    constraint_violations = []
    for constraint in query.constraints:
        try:
            _property = list(filter(lambda x: x.property_class == constraint.constraint_class, person.properties))[0]
        except IndexError:
            print(f"Constraint class {constraint.constraint_class} not found in person")
            constraint_violations.append(constraint.constraint_class)
            continue
        for constraint_field, constraint_set in constraint.constraint_fields:
            if constraint_set:
                _property_field = getattr(_property.property_fields, constraint_field)
                try:
                    validate_property(_property_field, constraint_set)
                except BaseException as e:
                    print(f"Validation for {constraint_field} failed with:\n{e}")
                    constraint_violations.append(constraint_field)
    if len(constraint_violations) > 0:
        print(f"Validation failed for {constraint_violations}")
        return False

    print("Validation successful")


def validate_property(_property_field, constraint_set):
    match constraint_set.constraint_group:
        case "int_constraint":
            validate_int_constraint(_property_field, constraint_set)
        case "string_constraint":
            validate_string_constraint(_property_field, constraint_set)
        case "bool_constraint":
            validate_bool_constraint(_property_field, constraint_set)
        case _:
            pass


def validate_bool_constraint(property_field, constraint_value):
    match constraint_value.constraint_type:
        case "match":
            if not property_field == constraint_value.constraint_features.match:
                raise Exception(
                    f"{property_field} does not exact match {constraint_value.constraint_features.match}")
        case _:
            pass


def validate_int_constraint(property_field, constraint_value):
    match constraint_value.constraint_type:
        case "min":
            if not property_field >= constraint_value.constraint_features.min:
                raise Exception(
                    f"{property_field} is not greater than {constraint_value.constraint_features.min}")
        case "max":
            if not property_field <= constraint_value.constraint_features.max:
                raise Exception(
                    f"{property_field} is not smaller than {constraint_value.constraint_features.max}")
        case "min_max":
            if not (constraint_value.constraint_features.min <=
                    property_field <= constraint_value.constraint_features.max):
                raise Exception(
                    f"{property_field} is not between {constraint_value.constraint_features.min} "
                    f"and {constraint_value.constraint_features.max}")
        case _:
            pass


def validate_string_constraint(property_field, constraint_value):
    match constraint_value.constraint_type:
        case "exact":
            if not property_field == constraint_value.constraint_features.exact:
                raise Exception(
                    f"{property_field} does not exact match {constraint_value.constraint_features.exact}")
        case _:
            pass
