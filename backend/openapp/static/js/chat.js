function outgoingMessageContstructor(message, timestamp) {

    var elem =
        '<div class="outgoing_msg">' +
            '<div class="sent_msg">' +
                '<p>' + message + '</p>' +
                '<span class="time_date">' + timestamp + '</span>' +
            '</div>' +
        '</div>'

    return elem;
}

function incomingMessageContstructor(message, timestamp, imgpath) {
    console.log('IMGPATH: ' + imgpath)
    var elem =
        '<div class="incoming_msg">' +
            '<div class="incoming_msg_img">' + 
                '<img src="' + imgpath + '" alt="sunil">' +
            '</div>' +
            '<div class="received_msg">' +
                '<div class="received_withd_msg">' +
                    '<p>' + message + '</p>' +
                    '<span class="time_date">' + timestamp + '</span>' +
                '</div>' +
            '</div>' +
        '</div>'

    return elem;
}


$(document).ready(function() {



    var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/openapp/chat/lobby/');

    chatSocket.onopen = function(e) {
        // console.log('Connected to server!');
        // chatSocket.send(JSON.stringify({
        //     'message': 'I AM A CLIENT MESSAGE'
        // }));
    };

    chatSocket.onmessage = function (event) {

        var sender = $('input[name=senderinput]').val();
        var receiver = $('input[name=receiverinput]').val();

        var datum = JSON.parse(event.data);

        if(sender === datum.sender && receiver === datum.receiver) {
            console.log('OUTGOING: ' + datum.message)
            $('.msghistory').append(outgoingMessageContstructor(datum.message, datum.timestamp));
        } else if(sender === datum.receiver && receiver === datum.sender) {
            console.log('INCOMING: ' + datum.message)
            $('.msghistory').append(incomingMessageContstructor(datum.message, datum.timestamp, datum.imgpath));
        }

        // $('.msghistory').animate({scrollTop: $(document).height()}, 1000);
        $('.msghistory').scrollTop($('.msghistory')[0].scrollHeight);

        console.log(event.data);
    };

    $('#sendButton').on('click', function() {

        var message = $('input[name=chatmessage]').val();
        var sender = $('input[name=senderinput]').val();
        var receiver = $('input[name=receiverinput]').val();


         if (message !== '') {
             chatSocket.send(JSON.stringify({
                 'sender': sender,
                 'receiver': receiver,
                 'message': message
             }));

            $('input[name=chatmessage]').val('');
        }

    });

    $('#chatmessage').keypress(function(event){
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == '13'){

            var message = $('input[name=chatmessage]').val();
            var sender = $('input[name=senderinput]').val();
            var receiver = $('input[name=receiverinput]').val();

            if (message !== '') {
                chatSocket.send(JSON.stringify({
                    'sender': sender,
                    'receiver': receiver,
                    'message': message
                }));

                $('input[name=chatmessage]').val('');
            }
        }
    });

    // $('.msghistory').animate({scrollTop: $('.msghistory div:last').offset().top}, 1000);
    $('.msghistory').scrollTop($('.msghistory')[0].scrollHeight);
});