

$(document).ready(function () {

    $('.fa-align-justify').on('click', function () {
        $('#sidebar, #content').toggleClass('active');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });

    
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

});
