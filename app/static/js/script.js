$(function() {
    $('#btnSendAjax').click(function () {
        // 入力値取得
        var name = $('input[name=name]').val();
        var message = $('input[name=message]').val();
        $.ajax({
            url: "/api/hello/post",
            type: "POST",
            data: JSON.stringify({name: name, message: message}),
            dataType: "json",
            contentType: "application/json",
            success: function (XMLHttpRequest, textStatus, errorThrown) {
                if (textStatus == 'success' || textStatus == 'nocontent') {
                    // 成功時
                    $('#lblInput1').text(XMLHttpRequest.input1);
                    $('#listInputs').append($("<li>").text(input));
                } else {
                    // エラー時
                    console.error(XMLHttpRequest.responseJSON.Message);
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                // エラー時
                console.error(XMLHttpRequest.responseJSON.Message);
            },
        });
        return false;
    });
});