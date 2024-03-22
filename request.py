import requests

url = 'https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer'
datos = {
    "name": "Jose Gutierrez",
    "mail": "jose.gutierrez.salas.12@gmail.com",
    "github_url": "https://github.com/joseguty12/latam-challenge.git"
}

respuesta = requests.post(url, json=datos)

print(respuesta.text)