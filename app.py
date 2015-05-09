import os

from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:////tmp/test.db")
db = SQLAlchemy(app)

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80))
  author = db.Column(db.String(80))
  isbn = db.Column(db.String(20))
  price = db.Column(db.String(8))
  seller_name = db.Column(db.String(80))
  seller_phone = db.Column(db.String(10))
  seller_email = db.Column(db.String(80))
  other_information = db.Column(db.String(140))

  def __init__(self, title, author, isbn, price, seller_name, seller_phone, seller_email, other_information):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.price = price
    self.seller_name = seller_name
    self.seller_phone = seller_phone
    self.seller_email = seller_email
    self.other_information = other_information

  def __repr__(self):
    return '<Book> %s' % self.title

  def asdict(self):
    return self.__dict__

@app.route('/')
def hello():
  return "The API is at <a href='/books'>/books</a>"

@app.route('/books', methods=['GET', 'POST'])
def books():
  if request.method == 'POST':
    bookJson = request.get_json(force=True)
    newBook = Book(bookJson['title'], bookJson['author'], bookJson['isbn'], bookJson['price'], bookJson['seller_name'], bookJson['seller_phone'], bookJson['seller_email'], bookJson['other_information'])
    db.session.add(newBook)
    db.session.commit()
  books = Book.query.all()
  realbooks = []
  for book in books:
    book = book.asdict()
    book.pop('_sa_instance_state', None)
    realbooks.append(book)
  return jsonify({"books": realbooks})


if __name__ == '__main__':
  app.run(debug=True)