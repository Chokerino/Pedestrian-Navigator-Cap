import openrouteservice
api="5b3ce3597851110001cf6248f05149ce402b4633920433f30aab79df"
coords = ((77.268126, 28.545782),(77.26976,28.546887))

client = openrouteservice.Client(key='5b3ce3597851110001cf6248f05149ce402b4633920433f30aab79df') # Specify your personal API key
routes = client.directions(coords,profile="foot-walking",format="geojson")

current = routes["features"][0]["properties"]["segments"][0]["steps"][0]

curr_instruct=current["instruction"]
curr_type=current["type"]

print(curr_instruct,curr_type)