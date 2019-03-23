function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}


$(document).ready(function () {


    $('#generateButton').on('click', function() {

        // Remove/hide elements
        $(this).hide();
        $('#generateTitle').hide();
        $('#generateText').hide();

        /**
         * [GET] /generate-code/
         * @return rc Return code status
         * @return errormessage The message error
         * @return code The generated code
         */

        // Update elements
        $('#generateTitle').text('5AH6E209Z').show();
        $('#generateText').text('Use the code above as your code to register.').show();
    })
});