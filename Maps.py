import openrouteservice
api="5b3ce3597851110001cf6248f05149ce402b4633920433f30aab79df"
coords = ((77.107374,28.530765),(77.109903,28.532033))

client = openrouteservice.Client(key='5b3ce3597851110001cf6248f05149ce402b4633920433f30aab79df') # Specify your personal API key
routes = client.directions(coords,profile="foot-walking",geometry_simplify=True,format="geojson")

print (routes)