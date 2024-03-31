peoples= {
    "one": {
        "first": "k",
        "last": "k",
        "location": "K"
    },
    "two" : {
        "first" : "b" ,
        "last" : "b" ,
        "location" : "B"
        },
    "three" : {
        "first" : "d" ,
        "last" : "d" ,
        "location" : "d"
    }
}
for piople, peop_info in peoples.items():
    print(f"People: {piople}")
    full_name = f'{peop_info["first"]} {peop_info["last"]}'
    location = peop_info["location"]
    print(f"Full Name: {full_name.title()}")
    print(f"Location: {location.title()}")