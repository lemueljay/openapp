function getchatlist() {

    console.log('getchatlist()')

    // $.get('/openapp/getchatlist', function(data) {
    //     console.log(data)
    // })

    setTimeout(getchatlist, 2000);
}

$(document).ready(function() {
    getchatlist()
})