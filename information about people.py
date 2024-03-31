peoples= {
    "one": {
        "first": "Kevin",
        "last": "Evans",
        "location": "Washington"
    },
    "two" : {
        "first" : "Adam" ,
        "last" : "Davies" ,
        "location" : "Bakersfield"
        },
    "three" : {
        "first" : "Ben" ,
        "last" : "Gilbert" ,
        "location" : "Madison"
    }
}
for piople, peop_info in peoples.items():
    print(f"People: {piople}")
    full_name = f'{peop_info["first"]} {peop_info["last"]}'
    location = peop_info["location"]
    print(f"Full Name: {full_name.title()}")
    print(f"Location: {location.title()}")
