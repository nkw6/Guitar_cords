from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

data = {
    "1":{
        "id":"1",
        "type":"major",
        "name":"C",
        "image":"c_major.png",
        "sound":"/data/sound/majorC.mp3"
    },
    "2":{
        "id":"2",
        "type":"major",
        "name":"D",
        "image":"d_major.png",
        "sound":"/data/audio/majorD.mp3"
    },
    "3":{
        "id":"3",
        "type":"major",
        "name":"E",
        "image":"e_major.png",
        "sound":"/data/audio/majorE.mp3"
    },
    "4":{
        "id":"4",
        "type":"major",
        "name":"F",
        "image":"f_major.png",
        "sound":"/data/audio/majorF.mp3"
    },
    "5":{
        "id":"5",
        "type":"major",
        "name":"G",
        "image":"g_major.png",
        "sound":"/data/audio/majorG.mp3"
    },
    "6":{
        "id":"6",
        "type":"major",
        "name":"A",
        "image":"a_major.png",
        "sound":"/data/audio/majorA.mp3"
    },


    #data for minors
    "7":{
        "id":"7",
        "type":"minor",
        "name":"C",
        "image":"c_minor.png",
        "sound":"/data/sound/majorC.mp3"
    },
    "8":{
        "id":"8",
        "type":"minor",
        "name":"D",
        "image":"d_minor.png",
        "sound":"/data/audio/majorD.mp3"
    },
    "9":{
        "id":"9",
        "type":"minor",
        "name":"E",
        "image":"e_minor.png",
        "sound":"/data/audio/majorE.mp3"
    },
    "10":{
        "id":"10",
        "type":"minor",
        "name":"F",
        "image":"f_minor.png",
        "sound":"/data/audio/majorF.mp3"
    },
    "11":{
        "id":"11",
        "type":"minor",
        "name":"G",
        "image":"g_minor.png",
        "sound":"/data/audio/majorG.mp3"
    },
    "12":{
        "id":"12",
        "type":"minor",
        "name":"A",
        "image":"a_minor.png",
        "sound":"/data/audio/majorA.mp3"
    },




    #7 datas
    "13":{
        "id":"13",
        "type":"7",
        "name":"C",
        "image":"c7.png",
        "sound":"/data/sound/majorC.mp3"
    },
    "14":{
        "id":"14",
        "type":"7",
        "name":"D",
        "image":"d7.png",
        "sound":"/data/audio/majorD.mp3"
    },
    "15":{
        "id":"15",
        "type":"7",
        "name":"E",
        "image":"e7.png",
        "sound":"/data/audio/majorE.mp3"
    },
    "16":{
        "id":"16",
        "type":"7",
        "name":"F",
        "image":"f7.png",
        "sound":"/data/audio/majorF.mp3"
    },
    "17":{
        "id":"17",
        "type":"7",
        "name":"G",
        "image":"g7.png",
        "sound":"/data/audio/majorG.mp3"
    },
    "18":{
        "id":"18",
        "type":"7",
        "name":"A",
        "image":"a7.png",
        "sound":"/data/audio/majorA.mp3"
    }

}


quiz_data = {
    "1":{
        "id":"1",
        "question":"Which of the following is an A major scale?",
        "image0":data["6"],
        "image1":data["10"],
        "image2":data["10"],
        "image3":data["10"]
    },
    "2": {
        "id":"2",
        "question":"Drag the following chords into their respective categories.",
        "image0":data["13"],
        "image1":data["5"],
        "image2":data["3"],
        "image3":data["13"],
        "image4":data["17"],
        "image5":data["18"]
    },
    "3": {
        "id":"3",
        "question":"What chord is shown below?",
        "image0":data["1"]
    }

}

# ROUTES
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/major')
def major():
    major = dict()

    # for dat in data:   #useful if unordered
    #     if dat["type"] == "major":
    #         major[dat["name"]] = dat

    for i in range(1,7):#loops through ordered data gets the first 6
        major[data[str(i)]["name"]] = data[str(i)]

    return render_template('major.html',major = major)

@app.route('/minor')
def minor():
    minor = dict()

    for i in range(7,13):#loops through ordered data gets the minors
        minor[data[str(i)]["name"]] = data[str(i)]

    return render_template('minor.html',minor = minor)

@app.route('/7th')
def seventh():
    seventh = dict()

    for i in range(13, 19):  # loops through ordered data gets the minors
        seventh[data[str(i)]["name"]] = data[str(i)]

    return render_template('7th.html',seventh = seventh)

@app.route('/quiz/<no>/')
def quiz(no = None):
    return render_template('quiz.html',quiz_data = quiz_data[no])

<<<<<<< HEAD
@app.route('/q1')
def q1():
    return render_template('q1.html') 

@app.route('/q2')
def q2():
    return render_template('q2.html')

@app.route('/q3')
def q3():
    return render_template('q3.html')

@app.route('/q4')
def q4():
    return render_template('q4.html')

@app.route('/q5')
def q5():
    return render_template('q5.html')

@app.route('/people')
def people():
    return render_template('people.html', data=data)  
=======
>>>>>>> 8fe281dff911d1ea9f94078c32b0e31d901871ac


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




