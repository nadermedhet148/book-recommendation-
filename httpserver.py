from flask import Flask
from flask import request, url_for, jsonify
from system import getReltedBooks

app = Flask(__name__)


@app.route('/recommend_book',  methods=['POST'])
def index():
    body = request.get_json()
    recommend_books = getReltedBooks(body['book_name'])
    # print(recommend_books[0])
    return jsonify(recommend_books)


if __name__ == '__main__':
    app.run(debug=True)
