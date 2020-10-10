import flask
from flask import request, jsonify
app=flask.Flask(__name__) #Creates flask aplication object--> contains data about app and its methods
app.config["DEBUG"] = True #Starts debugger

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=[ 'GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/v1/resources/books/all',methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    #Checks if an ID was provided as part of the url
    #if no id is provided, display and error in the browser

    #127.0.0.1:5000/api/v1/resources/books?id=0
    #data passed throguh urls after '?' are called query parameters

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id"

    #Create an empty list for our results
    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)






app.run()