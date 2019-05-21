function requestModalUpdate(id) {

    var data = {
        'id': id
    }

    $.get('/openapp/getRequest', data, function(data) {
        console.log(data)

        $('#answer1').text(data['answer1'])
        $('#answer2').text(data['answer2'])
        $('#answer3').text(data['answer3'])
        $('#answer4').text(data['answer4'])
        $('#answer5').text(data['answer5'])
        $('#answer6').text(data['answer6'])
        $('#answer7').text(data['answer7'])
        $('#answer8').text(data['answer8'])
        $('#answer9').text(data['answer9'])
        $('#answer10').text(data['answer10'])
        $('#answer11').text(data['answer11'])

        $('#sched_timedate').text(data['sched_date'] + ' (' + data['sched_time'] + ')')
        $('[name=request_id]').val(id)
        $('[name=sched_id]').val(data['sched_id'])
        $('[name=info_name]').val(data['info_name'])
        $('[name=info_contact_number]').val(data['info_contact_number'])
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
    $('#exampleModalLong').on('hidden.bs.modal', function() {
        $('#requestModal').modal('show')
    })
})