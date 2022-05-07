current_answ = 0;

function displayNames(data) {
  //empty old data
  $("#people_container").empty();

  //insert all new data
  $.each(data, function (i, datum) {
    let new_name = $("<div>" + datum["name"] + "</div>");
    $("#people_container").append(new_name);
  });
}
function setAnsw(user_answ) {
  current_answ = user_answ;
}
function quiz1_submit(id, nextID) {
  var ele = document.getElementsByName("answer");

  for (i = 0; i < ele.length; i++) {
    if (ele[i].checked) current_answ = ele[i].value;
    //document.getElementById("result").innerHTML = "Gender: " + ele[i].value;
  }
  // if (current_answ === 0) {
  //   console.log("please select  your answer");
  //   answ_error.style.visibility = "visible";
  //   answ_error_text.textContent = " Please select your answer ";
  //   return;
  // }
  submitAnsw(id, nextID);
}
function submitAnsw(id, nextID) {
  // if (current_answ === 0) {
  //   answ_error.style.visibility = "visible";
  //   answ_error_text.textContent = " Please select your answer ";
  //   return;
  // }
  answ_to_send = {
    answ: current_answ,
    id: id,
  };
  $.ajax({
    type: "POST",
    url: "../../submit_answ",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(answ_to_send),
    success: function (result) {
      console.log("success! printing return of ajax post");
      console.log(result);
      current_score = result["data"];
      console.log(current_score);
      return;
    },
    error: function (request, status, error) {
      console.log("Error");
      console.log(request);
      console.log(status);
      console.log(error);
    },
  });

  current_answ = 0;
  window.location.href = "/quiz/" + nextID + "/";
}
