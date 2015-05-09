from flask import Flask, jsonify

app = Flask(__name__)

libros = {
  "books": [
    {
      "title": "El Quijote",
      "author": "Miguel de Cervantes",
      "isbn": "1234-5678-9012",
      "price": 15,
      "seller_name": "Julio de la Cruz",
      "seller_phone": "787-123-4567",
      "seller_email": "julio@example.com",
      "other_information": "El libro esta en perfectas condiciones."
    }
  ]
}

@app.route('/')
def hello():
  return "The API is at <a href='/books'>/books</a>"

@app.route('/books')
def books():
  return jsonify(libros)


if __name__ == '__main__':
  app.run(debug=True)