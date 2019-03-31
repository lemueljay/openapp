$(document).ready(function () {

    $('#registerButton').on('click', function() {

        /**
         * [POST] /register/
         * @param refcode The reference code
         * @param username Preferred username
         * @param password Preferred password
         *
         * @return rc Return code status
         * @return errormessage The message error
         * @return token The access token for profiling
         */

        var postdata = {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'refcode': $('input[name=refcode]').val(),
            'username': $('input[name=username]').val(),
            'password': $('input[name=password]').val()
        }

         $.post('http://localhost:8000/openapp/register', postdata, function(data) {
            if (data['rc'] === 'OK') {
                $('.alert').remove();
                $('.card-body').prepend('<div class="alert alert-primary hidden" role="alert">User successfully created.</div>');
                window.location.replace("/openapp/");
            } else {
                $('.alert').remove();
                $('.card-body').prepend('<div class="alert alert-danger hidden" role="alert">' + data["errormessage"] + '</div>');
            }
         });


    })
});