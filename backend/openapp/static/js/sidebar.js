$(document).ready(function () {

    $('.fa-align-justify').on('click', function () {
                $('#sidebar, #content').toggleClass('active');
                $('.collapse.in').toggleClass('in');
                $('a[aria-expanded=true]').attr('aria-expanded', 'false');
            });

    // $('li').on('click', function() {
    //     $('li').removeClass('active');
    //     $(this).addClass('active');
    // });
    
    $('#myFile').change(function() {
        console.log('Upload button triggered')
        $('#uploadButton').click()
    })

    $('.containers').on('click', function() {
        console.log('')
        $('input[name=myfile]').click()        
    })

    $('#notifbell').on('click', function() {

    })

    $(function () {
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
        $('[data-toggle="popover"]').popover(options)
    })

});
