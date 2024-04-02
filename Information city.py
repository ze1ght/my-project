cities= {
    "Saratow": {
        "country": "Russia",
        "population": "850000",
        "fact": "none"
    },
    "Moscow" : {
        "country": "Russia",
        "population": "1500000",
        "fact": "none"
        },
    "Novosibirsk" : {
        "country": "Russia",
        "population": "1200000",
        "fact": "none"
    }
}
for city, city_info in cities.items():
    print(f"City: {city}")
    print(f"Country: {city_info['country']}")
    print(f"Population: {city_info['population']}")
    print(f"Fact: {city_info['fact']}")