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


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store['items'].append(new_item)
            return store, 201
    return {"message": "Sorry no store by that name"}, 404


@app.get("/store/<string:name>/item")
def get_store_items(name):
    for store in stores:
        if store['name'] == name:
            return store['items'], 200

    return {"message": "Sorry no store by that name"}, 404
