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

function incomingMessageContstructor(message, timestamp) {
    var elem =
        '<div class="incoming_msg">' +
            '<div class="received_msg">' +
                '<div class="received_withd_msg">' +
                    '<p>' + message + '</p>' +
                    '<span class="time_date">' + timestamp + '</span>' +
                '</div>' +
            '</div>' +
        '</div>'

    return elem;
}

var receiver = '';

$(document).ready(function(global) {

    var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/openapp/chat/lobby/');

    chatSocket.onopen = function(e) {
        console.log('Connected to server!');
        // chatSocket.send(JSON.stringify({
        //     'message': 'I AM A CLIENT MESSAGE'
        // }));
    };

    chatSocket.onmessage = function (event) {

        var sender = $('input[name=senderinput]').val();

        var datum = JSON.parse(event.data);

        if(sender === datum.sender && receiver === datum.receiver) {
            console.log('OUTGOING: ' + datum.message)
            $('.msghistory').append(outgoingMessageContstructor(datum.message, datum.timestamp));
        } else if(sender === datum.receiver && receiver === datum.sender) {
            console.log('INCOMING: ' + datum.message)
            $('.msghistory').append(incomingMessageContstructor(datum.message, datum.timestamp));
        }

        // $('.msghistory').animate({scrollTop: $(document).height()}, 1000);
        $('.msghistory').scrollTop($('.msghistory')[0].scrollHeight);

        console.log(event.data);
    };

    // Set the first chat list to as active
    // $('.chat_list:first-child').addClass('active_chat');

    $('.chat_list').on('click', function() {

        $('.msghistory').empty();

        $('.chat_list').removeClass('active_chat');
        $(this).addClass('active_chat');

        receiver = $(this).find('input').val();

        var data = {
            'receiver': receiver
        }

        console.log(data)

        $.get('http://localhost:8000/openapp/getmessages', data, function(data) {

            for(var i = 0; i < data.messages.length; i++) {

                if(receiver === data.messages[i].receiver) {
                    $('.msghistory').append(incomingMessageContstructor(data.messages[i].message, ''))
                } else {
                    $('.msghistory').append(outgoingMessageContstructor(data.messages[i].message, ''))
                }
            }
            $('.msghistory').scrollTop($('.msghistory')[0].scrollHeight);

        })



    })



    $('#sendButton').on('click', function() {

        var message = $('input[name=chatmessage]').val();
        var sender = $('input[name=senderinput]').val();

         if (message !== '' && receiver != '') {
             chatSocket.send(JSON.stringify({
                 'sender': sender,
                 'receiver': receiver,
                 'message': message
             }));

            $('input[name=chatmessage]').val('');
        } else {
             console.log('DO NOT ATTEMPT')
         }

    });

    $('#chatmessage').keypress(function(event){
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == '13' && receiver != ''){

            var message = $('input[name=chatmessage]').val();
            var sender = $('input[name=senderinput]').val();

            if (message !== '') {
                chatSocket.send(JSON.stringify({
                    'sender': sender,
                    'receiver': receiver,
                    'message': message
                }));

                $('input[name=chatmessage]').val('');
            }
        } else {
            console.log('DO NOT ATTEMPT')
        }
    });
})