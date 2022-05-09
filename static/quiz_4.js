const majors = new Set()
const minors = new Set()
$(document).ready(function() {
    $(".draggable").data("orDraggable",$(".draggable").offset());
    $(".draggable").hover(function() {$(this).addClass("opaque")}, function() {$(this).removeClass("opaque");});
    $(".draggable").draggable({revert:true,
        start:function() {  
        },
        stop:function() {
        }
    });
    $("#major").droppable({
        drop: function(e, ui) {
            e.preventDefault();
            e.stopPropagation();
            $("#major").removeClass("darken");
            let id = ui.draggable.attr("id");
            minors.delete(id);
            majors.add(id);
            $("#major").append(ui.draggable);
        },
        over: function() {
            $("#major").addClass("darken");
        },
        out: function() {
            $("#major").removeClass("darken");
        }
    });
    $("#minor").droppable({
        drop: function(e, ui) {
            e.preventDefault();
            e.stopPropagation();
            $("#minor").removeClass("darken");
            let id = ui.draggable.attr("id");
            majors.delete(id);
            minors.add(id);
            $("#minor").append(ui.draggable);
        },
        over: function() {
            $("#minor").addClass("darken");
        },
        out: function() {
            $("#minor").removeClass("darken");
            
        }
    });
});

function quiz4_submit() {
    console.log(majors.size);
    console.log(minors.size);
    if (majors.size + minors.size != 6) {
        let answ_error = document.getElementById("answ_error");
        console.log("Please classify all six chords");
        answ_error.style.visibility = "visible";
        return;
      }
      answ_to_send = {
        major: JSON.stringify(Array.from(majors)),
        minor: JSON.stringify(Array.from(minors))
      };
      
      $.ajax({
        type: "POST",
        url: "../../submit_multi_answ",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(answ_to_send),
        success: function (result) {
          corectness = result["data"];
          window.location.href = "/multi_feedback/" + 7 + "/" + corectness;
          //text = document.getElementById("corectness");
          //text.style.color = "red !important";
    
          return corectness;
        },
        error: function (request, status, error) {
          console.log("Error");
          console.log(request);
          console.log(status);
          console.log(error);
        },
      });
}