function chatPopup() {

    var chatOptions = {
        title: '<p class="notifHeader"><b>Messages</b></p>',
        content: '<h1>HELLO</h1>',
        html: true,
        placement: 'bottom'
    }

    $('#notifChat[data-toggle="popover"]').popover(chatOptions)
}

function notifPopup() {
    var imgpath = $('input[name=imgpath]').val()
    var username = $('input[name=username]').val()
    options = {
        title: '<img class="poppic" src="' + imgpath + '"><h4 class="text-center">' + username + '</h4>',
        content:
            '<div class="popoptions text-center">' + 
                '<a href="/openapp/settings" class="popoption">Settings</a>' + 
                '<a href="/openapp/logout" class="popoption">Logout</a>' + 
            '</div>',
        html: true,
        placement: 'bottom'
    }
    $('#myprofile[data-toggle="popover"]').popover(options);

    notifOptions = {
        title: '<p class="notifHeader"><b>REQUESTS</b></p>',
        content:
            '<div id="notifBox">' + 
                '<div>No new notifications.</div>' +
                '<hr>' +
                // '<div>1 unread message</div>' +                    
            '</div>' + 
            '<div class="text-center">' +
                '<a href="/openapp/requests">View All Requests</a>' +  
            '</div>'
            ,
        html: true,
        placement: 'bottom'
    }
    $('#notifbell[data-toggle="popover"]').popover(notifOptions)
}

function pollNotifs(){
    $.get('/openapp/notifications', function(data) {
        
        // console.log(data)

        var notifs = data['notifs'] 

        $('#notifBox').empty();
        
        notifs.forEach(function(notif) {
            if(notif['notifType'] === 'APPOINTMENT') {
                
                $('#notifBox').append('<div>' + notif['message'] + '</div><hr>');
            }
        })

        $('#notifLen').text(data['len'])

        setTimeout(pollNotifs, 1000);
    });
}

$(document).ready(function() {

    chatPopup();
    notifPopup();
    pollNotifs();


})