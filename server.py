from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

taught = []
last_seen = 1
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
        "audio":"d_minor.mp3"
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

modules = {
   "1": {
     "id": 1,
     "name": "Major Chords",
     "summary":"""A basic major chord always consists of three notes 
         (or pitches). But since the guitar consists of six strings,
         some of the notes are unavoidably duplicated. All major chords are
         based on the major scale. The C major, C major 7th and so on are 
         consequently based on the C major scale.""",
     "chords": [data["1"], data["2"], data["3"], data["4"], data["5"], data["6"]]
   },
   "2": {
     "id": 2,
     "name": "Minor Chords",
     "summary":"""The minor chords are together with the major chords the most 
        important chords to learn for guitarists. This chord type consists of a
         root note, a minor third and a fifth. Like the major chords, they are 
        named after the scale of the root note and generally have a more somber 
        sound/characteristic.""",
     "chords": [data["7"], data["8"], data["9"], data["10"], data["11"], data["12"]]
   },
   "3": {
     "id": 3,
     "name": "7th Chords",
     "summary":"""The 7th chord (also known as dominant 7th) adds another tone 
        to the major triad chord. As the name implies, the added tone is seven 
        steps from the root (following the scale). These chords are also called 
        dominant chords, and they are especially common in blues.""",
     "chords": [data["13"], data["14"], data["15"], data["16"], data["17"], data["18"]]
   },
}

quiz_data = {
        "1": {
        "id":"1",
        "nextID": "2",
        "answ" : "1",
        "answer":data["1"],
        "question":"What chord is shown below?",
        "option1":data["1"],
        "option2":data["18"],
        "option3":data["4"],
        "option4":data["11"],
    },
        "2": {
        "id":"2",
        "nextID": "3",
        "answ": "3",
        "answer":data["2"],
        "question":"What chord is shown below?",
        "option1":data["6"],
        "option2":data["3"],
        "option3":data["2"],
        "option4":data["9"],
    },
    "3":{
        "id":"3",
        "nextID": "4",
        "answ":"1",
        "answer":data["6"],
        "question":"Which of the following is an A major scale?",
        "option1":data["6"],
        "option2":data["7"],
        "option3":data["10"],
        "option4":data["1"]
    },
    "4":{
        "id":"4",
        "nextID": "5",
        "answ":"2",
        "answer":data["16"],
        "question":"Which of the following is an F7 chord?",
        "option1":data["4"],
        "option2":data["16"],
        "option3":data["2"],
        "option4":data["8"]
    },
    "5": {
        "id":"5",
        "nextID": "6",
        "question":"choose the correct sound",
        "answ":"4",
        "answer":data["13"],
        "option1":data["16"],
        "option2":data["5"],
        "option3":data["3"],
        "option4":data["13"],
    },
     "6": {
        "id":"6",
        "nextID": "7",
        "question":"choose the correct sound",
        "answ":"3",
        "answer":data["4"],
        "option1":data["1"],
        "option2":data["18"],
        "option3":data["4"],
        "option4":data["11"],
    },
    "7": {
        "id":"7",
        "nextID": "results",
        "question":"Drag the following chords into their respective categories",
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

@app.route('/learn/<id>')
def learn(id=None):
   #  major = dict()

   #  for i in range(1,7):#loops through ordered data gets the first 6
   #      major[data[str(i)]["letter"]] = data[str(i)]

    return render_template('learn.html', data = modules[str(id)])

@app.route('/objectives')
def objectives():
   return render_template('objectives.html', taught = taught, last_seen = last_seen)

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
    if (int(no) < 7):
        return render_template('quiz_3.html',quiz_data = quiz_data[no], score = score_count)
    if (int(no) == 7):
        return render_template('quiz_4.html',quiz_data = quiz_data[no], score = score_count)

@app.route('/feedback/<no>/<answ>')
def feedback(no = None, answ = None):
    return render_template('feedback.html',quiz_data = quiz_data[no], score = score_count,answ = answ)

@app.route('/results')
def results():
    return render_template('results.html', score = score_count, image="back_to_the_future.gif" )

# AJAX FUNCTIONS
# ajax for learned modules
@app.route('/learned_module', methods=['POST'])
def learned_module():
    global taught
    global last_seen

    json_data = request.get_json()   
    module = json_data["id"] 
    last_seen = module

    if(module not in taught):
      taught.append(module)

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = taught)

# ajax for quiz answers
@app.route('/submit_answ', methods=['POST'])
def submit_answ():
    global quiz_data 
    global score_count 

    json_data = request.get_json()   
    answ = json_data["answ"] 
    question_id = json_data["id"]  

    if(str(answ) == quiz_data[str(question_id)]["answ"]):
        score_count += 1
        corectness = "correct"
    else:
        corectness = "incorrect"
    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = corectness)

if __name__ == '__main__':
   app.run(debug = True)




