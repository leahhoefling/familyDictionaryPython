# Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
    "sister": {
        "name": "Ansley",
        "age": 22
    },
    "mother": {
        "name": "Davina",
        "age": 54
    },
    "father": {
        "name": "Vern",
        "age": 54
    },
    "Husband": {
        "name": "Benjamin",
        "age": 27
    },
    "Pup": {
        "name": "Harper",
        "age": 2
    }
}
# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old

# loop of all family members
for member, value in my_family.items():
    print(value["name"], f"is my {member} and is", value["age"], "years old.")
