from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

taught = []
score_count = 0

data = {
    "1":{
        "id":"1",
        "type":"major",
        "letter":"C",
        "name":"C Major",
        "image":"c_major.png",
        "audio":"c_major.mp3"
    },
    "2":{
        "id":"2",
        "type":"major",
        "letter":"D",
        "name":"D Major",
        "image":"d_major.png",
        "audio":"d_major.mp3"
    },
    "3":{
        "id":"3",
        "type":"major",
        "letter":"E",
        "name":"E Major",
        "image":"e_major.png",
        "audio":"e_major.mp3"
    },
    "4":{
        "id":"4",
        "type":"major",
        "letter":"F",
        "name":"F Major",
        "image":"f_major.png",
        "audio":"f_major.mp3"
    },
    "5":{
        "id":"5",
        "type":"major",
        "letter":"G",
        "name":"G Major",
        "image":"g_major.png",
        "audio":"g_major.mp3"
    },
    "6":{
        "id":"6",
        "type":"major",
        "letter":"A",
        "name":"A Major",
        "image":"a_major.png",
        "audio":"a_major.mp3"
    },


    #data for minors
    "7":{
        "id":"7",
        "type":"minor",
        "letter":"C",
        "name":"C Minor",
        "image":"c_minor.png",
        "audio":"c_minor.mp3"
    },
    "8":{
        "id":"8",
        "type":"minor",
        "letter":"D",
        "name":"D Minor",
        "image":"d_minor.png",
        "audio":"/data/audio/majorD.mp3"
    },
    "9":{
        "id":"9",
        "type":"minor",
        "letter":"E",
        "name":"E Minor",
        "image":"e_minor.png",
        "audio":"e_minor.mp3"
    },
    "10":{
        "id":"10",
        "type":"minor",
        "letter":"F",
        "name":"F Minor",
        "image":"f_minor.png",
        "audio":"f_minor.mp3"
    },
    "11":{
        "id":"11",
        "type":"minor",
        "letter":"G",
        "name":"G Minor",
        "image":"g_minor.png",
        "audio":"g_minor.mp3"
    },
    "12":{
        "id":"12",
        "type":"minor",
        "letter":"A",
        "name":"A Minor",
        "image":"a_minor.png",
        "audio":"a_minor.mp3"
    },




    #7 datas
    "13":{
        "id":"13",
        "type":"7",
        "letter":"C",
        "name":"C7",
        "image":"c7.png",
        "audio":"c7.mp3"
    },
    "14":{
        "id":"14",
        "type":"7",
        "letter":"D",
        "name":"D7",
        "image":"d7.png",
        "audio":"d7.mp3"
    },
    "15":{
        "id":"15",
        "type":"7",
        "letter":"E",
        "name":"E7",
        "image":"e7.png",
        "audio":"e7.mp3"
    },
    "16":{
        "id":"16",
        "type":"7",
        "letter":"F",
        "name":"F7",
        "image":"f7.png",
        "audio":"/f7.mp3"
    },
    "17":{
        "id":"17",
        "type":"7",
        "letter":"G",
        "name":"G7",
        "image":"g7.png",
        "audio":"g7.mp3"
    },
    "18":{
        "id":"18",
        "type":"7",
        "letter":"A",
        "name":"A7",
        "image":"a7.png",
        "audio":"a7.mp3"
    }

}


quiz_data = {
        "1": {
        "id":"1",
        "nextID": "2",
        "answ" : "1",
        "question":"What chord is shown below?",
        "image0":data["1"]
    },
        "2": {
        "id":"2",
        "nextID": "3",
        "answ": "1",
        "question":"What chord is shown below?",
        "image0":data["2"]
    },
    "3":{
        "id":"3",
        "nextID": "4",
        "answ":"1",
        "question":"Which of the following is an A major scale?",
        "image0":data["6"],
        "image1":data["10"],
        "image2":data["10"],
        "image3":data["10"]
    },
    "4":{
        "id":"4",
        "nextID": "5",
        "answ":"1",
        "question":"Which of the following is an A major scale?",
        "image0":data["6"],
        "image1":data["10"],
        "image2":data["10"],
        "image3":data["10"]
    },
    "5": {
        "id":"5",
        "nextID": "results",
        "question":"Drag the following chords into their respective categories.",
        "answ":"1",
        "image0":data["13"],
        "image1":data["5"],
        "image2":data["3"],
        "image3":data["13"],
        "image4":data["17"],
        "image5":data["18"],
        "img_0_chord":"major",
        "img_1_chord":"major",
        "img_2_chord":"major",
        "img_3_chord":"major",
        "img_4_chord":"major",
        "img_5_chord":"major",
    },
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

@app.route('/quiz_start')
def quiz_start():
    global score_count
    
    score_count = 0 # reset the score
    
    return render_template('quiz_start.html')
@app.route('/quiz/<no>/')
def quiz(no = None):
    if (int(no) < 3):
        return render_template('quiz_1.html',quiz_data = quiz_data[no], score = score_count)
    if (int(no) < 5):
        return render_template('quiz_2.html',quiz_data = quiz_data[no], score = score_count)
    if (int(no) == 5):
        return render_template('quiz_3.html',quiz_data = quiz_data[no], score = score_count)

@app.route('/objectives')
def objectives():
    return render_template('objectives.html', taught = taught )

@app.route('/results')
def results():
    return render_template('results.html', score = score_count )

# AJAX FUNCTIONS
@app.route('/submit_answ', methods=['POST'])
def submit_answ():
    global quiz_data 
    global score_count 

    json_data = request.get_json()   
    answ = json_data["answ"] 
    question_id = json_data["id"]  
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    if(str(answ) == quiz_data[str(question_id)]["answ"]):
        score_count += 1
    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = score_count)

if __name__ == '__main__':
   app.run(debug = True)




