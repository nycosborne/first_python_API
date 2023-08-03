from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "Super Store",
        "items": [
            {
                "name": "table",
                "price": 15.99
            }
        ]
    }
]


@app.get("/store")
def get_store():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


# @app.post("/store/<string:name>")
# def create_item(name):
#     return name, 201
