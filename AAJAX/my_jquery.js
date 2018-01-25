    $(document).ready(function () {
        $("#hideandshow").click(function () {
            $("img").toggle();
            var display = $("img").css("display");
            if(display == 'none'){
                $("#hideandshow").text("显示");
            }else {
                $("#hideandshow").text("隐藏");
            }
        });
        // $("#p1").css("color","red").slideUp(2000).slideDown(2000);
        $("#btn1").click(function () {
            $("#p1").text(function (i,origText) {
                return "Old text: " + origText + " New text: Hello world!(index:"+i+")";
            })
        });
        $("#btn2").click(function () {
            $("#p2").html(function (i,originHtml) {
                return "Old HTML: "+originHtml+"New HTML: Hello World!(index: "+i+")";
            })
        });
        $("#btn3").click(function () {
            $("input").val("Hello World!!")
        });
        $("#btn4").click(function () {
            $("#a-cgb").attr("href","http://www.zenofpy.cn");
            $("#btn4").text("href added");
        });
        $("#btn5").click(function () {
            $("img").attr('title',function (i,orignAttr) {
                return orignAttr+"ccccc";
            })
        });
        $("#btn6").click(function () {
            $("#p2").append("<b>append content</b>");
        });
        $("#btn7").click(function () {
            $("#p1").prepend("<b>prepend content</b>");
        });

        $("#btn8").click(function () {
            var text1 = "<b>text111</b>";
            var text2 = $("<p></p>").text("text222");
            var text3 = document.createElement("p");
            text3.innerHTML="text333";
            $("#p2").before(text1,text2,text3);
        })
    });