function requestModalUpdate(id) {

    var data = {
        'id': id
    }

    $.get('/openapp/getRequest', data, function(data) {
        console.log(data)
        $('[name=request_id]').val(id)
        $('[name=sched_id]').val(data['sched_id'])
        $('[name=info_name]').val(data['info_name'])
        $('[name=info_id]').val(data['info_id'])
        $('[name=info_college]').val(data['info_college'])
        $('[name=info_yrcourse]').val(data['info_yrcourse'])
        $('[name=info_studentyear]').val(data['info_studentyear'])
        $('[name=info_gender]').val(data['info_gender'])
        $('[name=info_location]').val(data['info_location'])
    })
}

function declineButton() {
    $('.declinedmodal').modal({'show': true})
}

$(document).ready(function() {
    
})