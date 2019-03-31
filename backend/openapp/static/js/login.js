$(document).ready(function () {

    $('#loginButton').on('click', function() {

        var postdata = {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'username': $('input[name=username]').val(),
            'password': $('input[name=password]').val()
        }

         $.post('http://localhost:8000/openapp/login', postdata, function(data) {
            if (data['rc'] === 'OK') {
                $('.alert').remove();
                $('.card-body').prepend('<div class="alert alert-primary hidden" role="alert">Login successsful.</div>');
                window.location.replace("/openapp/");
            } else {
                $('.alert').remove();
                $('.card-body').prepend('<div class="alert alert-danger hidden" role="alert">' + data["errormessage"] + '</div>');
            }

         });
    })
});