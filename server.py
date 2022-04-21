from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 2

data = {
    "1":{
        "id":1,
        "type":"major",
        "letter":"C",
        "image":"../data/image/majorC.png",
        "sound":"/data/sound/majorC.mp3"
    },
    "2":{

    },
    ##etc...

}


quiz_data = {
    "1":{
        "id":"1",
        "question":"Which of the following is an A major scale?",
        "image0":data["1"],
        # "image1":data["4"],
        # "image2":data["5"],
        # "image3":data["2"],
    },
    "2": {
        "id":"2",
        "question":"Drag the following chords into their respective categories.",
        "image0":data["1"],
        # "image1":data["4"],
        # "image2":data["5"],
        # "image3":data["2"],
    },
    "3": {
        "id":"3",
        "question":"What chord is shown below?",
        "image0":data["1"]
    }

}
# ROUTES

@app.route('/hi')
def hello():
   return 'Hi hi hi hi hi hi hi hi hi'


@app.route('/')
def home():
   return render_template('home.html')   


@app.route('/major')
def major():
    return render_template('major.html') 

@app.route('/minor')
def minor():
    return render_template('minor.html')

@app.route('/7th')
def seventh():
    return render_template('7th.html')

@app.route('/quiz/<no>/')
def quiz(no = None):
    return render_template('quiz.html',quiz_data[no])

@app.route('/objectives')
def objectives():
    return render_template('objectives.html') 

@app.route('/people')
def people():
    return render_template('people.html', data=data)  


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




