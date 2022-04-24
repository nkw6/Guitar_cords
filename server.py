from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

data = {
    "1":{
        "id":1,
        "type":"major",
        "name":"C Major",
        "image":"../data/image/c_major.png",
        "sound":"/data/sound/majorC.mp3"
    },
    "2":{
        "id":2,
        "type":"major",
        "name":"D Major",
        "image":"../data/images/d_major.png",
        "sound":"/data/audio/majorD.mp3"
    },
    "3":{
        "id":3,
        "type":"major",
        "name":"E Major",
        "image":"../data/images/e_major.png",
        "sound":"/data/audio/majorE.mp3"
    },
    "4":{
        "id":4,
        "type":"major",
        "name":"F Major",
        "image":"../data/images/f_major.png",
        "sound":"/data/audio/majorF.mp3"
    },
    "5":{
        "id":5,
        "type":"major",
        "name":"G Major",
        "image":"../data/images/g_major.png",
        "sound":"/data/audio/majorG.mp3"
    },
    "6":{
        "id":6,
        "type":"major",
        "name":"A Major",
        "image":"../data/images/a_major.png",
        "sound":"/data/audio/majorA.mp3"
    },


    #data for minors
    "7":{
        "id":7,
        "type":"minor",
        "name":"C",
        "image":"../data/image/c_minor.png",
        "sound":"/data/sound/majorC.mp3"
    },
    "8":{
        "id":8,
        "type":"minor",
        "name":"D",
        "image":"../data/images/d_minor.png",
        "sound":"/data/audio/majorD.mp3"
    },
    "9":{
        "id":9,
        "type":"minor",
        "name":"E",
        "image":"../data/images/e_minor.png",
        "sound":"/data/audio/majorE.mp3"
    },
    "10":{
        "id":10,
        "type":"minor",
        "name":"F",
        "image":"../data/images/f_minor.png",
        "sound":"/data/audio/majorF.mp3"
    },
    "11":{
        "id":11,
        "type":"minor",
        "name":"G",
        "image":"../data/images/g_minor.png",
        "sound":"/data/audio/majorG.mp3"
    },
    "12":{
        "id":12,
        "type":"minor",
        "name":"A",
        "image":"../data/images/a_minor.png",
        "sound":"/data/audio/majorA.mp3"
    },




    #7 datas
    "13":{
        "id":13,
        "type":"7",
        "name":"C",
        "image":"../data/image/c7.png",
        "sound":"/data/sound/majorC.mp3"
    },
    "14":{
        "id":14,
        "type":"7",
        "name":"D",
        "image":"../data/images/d7.png",
        "sound":"/data/audio/majorD.mp3"
    },
    "15":{
        "id":15,
        "type":"7",
        "name":"E",
        "image":"../data/images/e7.png",
        "sound":"/data/audio/majorE.mp3"
    },
    "16":{
        "id":16,
        "type":"7",
        "name":"F",
        "image":"../data/images/f7.png",
        "sound":"/data/audio/majorF.mp3"
    },
    "17":{
        "id":17,
        "type":"7",
        "name":"G",
        "image":"../data/images/g7.png",
        "sound":"/data/audio/majorG.mp3"
    },
    "18":{
        "id":18,
        "type":"7",
        "name":"A",
        "image":"../data/images/a7.png",
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




