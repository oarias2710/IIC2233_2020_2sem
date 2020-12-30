from networking import Client
import json

with open("parametros.json", "rb") as file:
    dict_param = json.load(file)

if __name__ == "__main__":
    port = dict_param["port"]
    host = dict_param["host"]

    client = Client(port, host)