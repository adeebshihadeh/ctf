function ready() {
    if ($("#question").length === 0) {
        setTimeout(ready, 50);
    } else {
        solve();
    }
}

ready();

function next() {
    var empty = true;
    $("input").each(function() {
        if (($(this).prop('type') == "text" && $(this).val() != "") || $(this).prop('checked')) {
            empty = false;
        }
    });

    setTimeout(empty ? solve : next, 50);
}

function solve() {
    var t = $("#question").text().split("a(n) ")[1].split(" of")[0];
    var a = $("#question").text().split(" of ")[2];
    
    var q = "";
    
    if(t == "name") {
        q = "[name='" + a + "']";
    } else if (t == "class") {
        q = "." + a;
    } else if (t == "id") {
        q = "#" + a;
    }

    var b = eval($($(q).find("*")[1]).text());
    b = Math.round(b - 0.5);
    var id = $(q).attr('id');
    q = "#" + id;

    console.log("q: " + q);
    console.log("b: " + b);
    
    if ($(q).find("*").html().includes('type="radio"')) {
        for(var i = 0; i < 4; i++) {
            if ($("#" + id + "-" + i).parent().text() == b) {
                console.log("selected #" + i);
                $("#" + id + "-" + i).prop('checked', true).trigger("change");
            }
        }
    } else {
        $(q).find("input").val(b).trigger("change");
    }
    $(q)[0].scrollIntoView();

    setTimeout(next, 50);
}
