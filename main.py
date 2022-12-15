from flask import Flask, request, render_template, jsonify

db = []

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("page.html", title='', db=db)


@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    name = data['note']
    db.append(name)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug = True)