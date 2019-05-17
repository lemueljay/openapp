function notifPopup() {
    console.log('updating...')
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
}

function pollNotifs(){

    $.get('/openapp/notifications', function(data) {
    
        var notifs = data['notifs']

        var notifCount = 0;
        var elements = ''

        if(notifs.length != 0) {
        
            $('#notifBox').empty();
            
            notifs.forEach(function(notif) {
                if(notif['notifType'] === 'APPOINTMENT') {
                    
                    // $('#notifBox').append('<div>' + notif['message'] + '</div><hr>');
                    elements += '<div>' + notif['message'] + '</div><hr>'
                }

                notifCount++;
                if(notifCount == 3) {            
                    return;
                }
            })
        }


        if(data['len'] === 0) {
            
        } else {
            $('#notifLen').show().text(data['len'])
        }

        if(elements === '') {
            notifOptions = {
                title: '<p class="notifHeader"><b>NOTIFICATIONS</b></p>',
                content:
                    '<div id="notifBox">' + 
                        '<div>No new notifications.</div>' +
                        '<hr>' +
                    '</div>' + 
                    '<div class="text-center">' +
                        '<a href="/openapp/requests">View All Requests</a>' +  
                    '</div>'
                    ,
                html: true,
                placement: 'bottom'
            }
        } else {
            notifOptions = {
                title: '<p class="notifHeader"><b>NOTIFICATIONS</b></p>',
                content:
                    '<div id="notifBox">' +                         
                        elements +                 
                    '</div>' + 
                    '<div class="text-center">' +
                        '<a href="/openapp/requests">View All Requests</a>' +  
                    '</div>'
                    ,
                html: true,
                placement: 'bottom'
            }
        }

       
        $('#notifbell[data-toggle="popover"]').popover(notifOptions)

        // setTimeout(pollNotifs, 1000);

        
    });
}

function badger() {

    $.get('/openapp/notifications', function(data) {
        
        var len = $('#notifLen').text()

        if(len != data['len']) {
            if(window.location.pathname === '/openapp/book') {
                window.location.replace('/openapp/')
            } else {
                window.location = window.location.pathname;
            }
        } else {
            console.log('BADGER POLLING...')
        }
        
    });
    
    setTimeout(badger, 1000);
}

$(document).ready(function() {

    notifPopup();     
    pollNotifs();
    badger();
})