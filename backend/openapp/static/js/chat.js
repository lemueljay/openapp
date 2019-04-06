function outgoingMessageContstructor(message) {

    var elem =
        '<div class="outgoing_msg">' +
            '<div class="sent_msg">' +
                '<p>' + message + '</p>' +
                '<span class="time_date"> 11:01 AM    |    June 9</span>' +
            '</div>' +
        '</div>'

    return elem;
}

$(document).ready(function() {

    var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/openapp/chat/lobby/');

    chatSocket.onopen = function(e) {
        console.log('Connected to server!');
        chatSocket.send(JSON.stringify({
            'message': 'I AM A CLIENT MESSAGE'
        }));
    };

    chatSocket.onmessage = function (event) {
        console.log(event.data);
    };

    $('#sendButton').on('click', function() {

        var message = $('input[name=chatmessage]').val();

         if (message === '') {

        } else {
            $('.msghistory').append(outgoingMessageContstructor(message));

             $('.msghistory').animate({
                         scrollTop: $(document).height()
                     },
                     1000);
            $('input[name=chatmessage]').val('');
        }

    });

    $('#chatmessage').keypress(function(event){
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == '13'){

            var message = $('input[name=chatmessage]').val();

             if (!(message === '')) {
                var postdata = {
                     'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                     'message': message,
                     'college': $('input[name=destination]').val()
                }

                $.post('http://localhost:8000/openapp/chat', postdata, function(data) {

                         $('.msghistory').append(outgoingMessageContstructor(message));

                         $('.msghistory').animate({
                                     scrollTop: $(document).height()
                                 },
                                 1000);
                        $('input[name=chatmessage]').val('');

                 });
             }
        }
    });

});