def array_of_names(persons):
    result = []
    for first, last in persons.items():
        full_name = first.capitalize() + " " + last.capitalize()
        result.append(full_name)
    return result

# ทดสอบ
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
