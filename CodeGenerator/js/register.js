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
        console.log('oks');
        var postdata = {
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        }

         $.post('http://localhost:8000/openapp/register', postdata, function(data) {
            console.log(data);
         });
    })
});