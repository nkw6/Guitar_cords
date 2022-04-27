data = {
    "1":{
        "id":"1",
        "type":"major",
        "letter":"C",
        "name":"C Major",
        "image":"c_major.png",
        "sound":"c_major.mp3"
    },
    "2":{
        "id":"2",
        "type":"major",
        "letter":"D",
        "name":"D Major",
        "image":"d_major.png",
        "sound":"d_major.mp3"
    },
    "3":{
        "id":"3",
        "type":"major",
        "letter":"E",
        "name":"E Major",
        "image":"e_major.png",
        "sound":"e_major.mp3"
    },
    "4":{
        "id":"4",
        "type":"major",
        "letter":"F",
        "name":"F Major",
        "image":"f_major.png",
        "sound":"f_major.mp3"
    },
    "5":{
        "id":"5",
        "type":"major",
        "letter":"G",
        "name":"G Major",
        "image":"g_major.png",
        "sound":"g_major.mp3"
    },
    "6":{
        "id":"6",
        "type":"major",
        "letter":"A",
        "name":"A Major",
        "image":"a_major.png",
        "sound":"a_major.mp3"
    },


    #data for minors
    "7":{
        "id":"7",
        "type":"minor",
        "letter":"C",
        "name":"C Minor",
        "image":"c_minor.png",
        "sound":"/data/sound/majorC.mp3"
    },
    "8":{
        "id":"8",
        "type":"minor",
        "letter":"D",
        "name":"D Minor",
        "image":"d_minor.png",
        "sound":"d_minor.mp3"
    },
    "9":{
        "id":"9",
        "type":"minor",
        "letter":"E",
        "name":"E Minor",
        "image":"e_minor.png",
        "sound":"e_minor.mp3"
    },
    "10":{
        "id":"10",
        "type":"minor",
        "letter":"F",
        "name":"F Minor",
        "image":"f_minor.png",
        "sound":"f_minor.mp3"
    },
    "11":{
        "id":"11",
        "type":"minor",
        "letter":"G",
        "name":"G Minor",
        "image":"g_minor.png",
        "sound":"g_minor.mp3"
    },
    "12":{
        "id":"12",
        "type":"minor",
        "letter":"A",
        "name":"A Minor",
        "image":"a_minor.png",
        "sound":"a_minor.mp3"
    },




    #7 datas
    "13":{
        "id":"13",
        "type":"7",
        "letter":"C",
        "name":"C7",
        "image":"c7.png",
        "sound":"c7.mp3"
    },
    "14":{
        "id":"14",
        "type":"7",
        "letter":"D",
        "name":"D7",
        "image":"d7.png",
        "sound":"d7.mp3"
    },
    "15":{
        "id":"15",
        "type":"7",
        "letter":"E",
        "name":"E7",
        "image":"e7.png",
        "sound":"e7.mp3"
    },
    "16":{
        "id":"16",
        "type":"7",
        "letter":"F",
        "name":"F7",
        "image":"f7.png",
        "sound":"f7.mp3"
    },
    "17":{
        "id":"17",
        "type":"7",
        "letter":"G",
        "name":"G7",
        "image":"g7.png",
        "sound":"g7.mp3"
    },
    "18":{
        "id":"18",
        "type":"7",
        "letter":"A",
        "name":"A7",
        "image":"a7.png",
        "sound":"a7.mp3"
    }

}


quiz_data = {
        "1": {
        "id":"1",
        "nextID": "2",
        "question":"What chord is shown below?",
        "image0":data["1"],
        "choices":["F Major", "C Major", "E7", "C Minor"],
        "correct": 1
    },
        "2": {
        "id":"2",
        "nextID": "3",
        "question":"What chord is shown below?",
        "image0":data["2"],
        "choices":["A Major", "D7", "D Major", "E Minor"],
        "correct": 2
    },
    "3":{
        "id":"3",
        "nextID": "4",
        "question":"Which of the following is an A major scale?",
        "image0":data["6"],
        "image1":data["10"],
        "image2":data["10"],
        "image3":data["10"]
    },
    "4":{
        "id":"4",
        "nextID": "5",
        "question":"Which of the following is an A major scale?",
        "image0":data["6"],
        "image1":data["10"],
        "image2":data["10"],
        "image3":data["10"]
    },
    "5": {
        "id":"5",
        "nextID": "6",
        "question":"Drag the following chords into their respective categories.",
        "image0":data["13"],
        "image1":data["5"],
        "image2":data["3"],
        "image3":data["13"],
        "image4":data["17"],
        "image5":data["18"]
    },
}