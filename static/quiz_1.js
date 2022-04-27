$(document).ready(function() {
    populateMC(quiz_data);
    $(".next-btn").click(function(e) {
        e.preventDefault();
        checkAnswer();
    })
})

function populateMC(quiz_data) {
    $("#mc_choices").empty();
    $.each(quiz_data["choices"], function(i, val) {
        const choice = $("<input type=\"radio\" id=" + i + "value=" + val + ">" +
        "<label for=" + val + ">" + val + "</label><br>");
        console.log(choice)
        $("#mc_choices").append(choice);
    });
}

function checkAnswer() {
    const correct = quiz_data["correct"];
    $.each($("#mc_choices").elements, function(i, val) {
        console.log(val)
    })
}