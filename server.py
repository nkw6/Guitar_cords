from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from data import *
app = Flask(__name__)

taught = []


# ROUTES
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/major')
def major():
    major = dict()

    # for dat in data:   #useful if unordered
    #     if dat["type"] == "major":
    #         major[dat["letter"]] = dat

    for i in range(1,7):#loops through ordered data gets the first 6
        major[data[str(i)]["letter"]] = data[str(i)]

    return render_template('major.html',major = major)

@app.route('/minor')
def minor():
    minor = dict()

    for i in range(7,13):#loops through ordered data gets the minors
        minor[data[str(i)]["letter"]] = data[str(i)]

    return render_template('minor.html',minor = minor)

@app.route('/7th')
def seventh():
    seventh = dict()

    for i in range(13, 19):  # loops through ordered data gets the minors
        seventh[data[str(i)]["letter"]] = data[str(i)]

    return render_template('7th.html',seventh = seventh)

@app.route('/quiz/<no>/')
def quiz(no = None):
    if (int(no) < 3):
        return render_template('quiz_1.html',quiz_data = quiz_data[no])
    if (int(no) < 5):
        return render_template('quiz_2.html',quiz_data = quiz_data[no])
    if (int(no) == 5):
        return render_template('quiz_3.html',quiz_data = quiz_data[no])

@app.route('/objectives')
def objectives():
    return render_template('objectives.html', taught = taught )

@app.route('/results')
def results():
    return render_template('results.html', taught = taught )


# AJAX FUNCTIONS

# ajax for people.js
@app.route('/add_name', methods=['GET', 'POST'])
def add_name():
    global data 
    global current_id 

    json_data = request.get_json()   
    name = json_data["name"] 
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = current_id 
    new_name_entry = {
        "name": name,
        "id":  current_id
    }
    data.append(new_name_entry)

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = data)
 


if __name__ == '__main__':
   app.run(debug = True)




