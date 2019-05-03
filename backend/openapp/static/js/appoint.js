var global_sched = null;

function redirectToInformationSheet() {
    
    console.log("redirecting....")
    window.location = '/openapp/information/' + global_sched;
}

function cancelAppointment(id) {

    var data = {
        'id': id
    }

    $.get("http://localhost:8000/openapp/cancelAppointment", data, function(data) {
        $('#modalBbutton').click();
    });
}

function setAppointment(id) {

    var data = {
        'id': id,
        'assignee': $('input[name=assignee]').val()
    }

    $.get("http://localhost:8000/openapp/setAppointmentSchedule", data, function(data) {
        $('#modalBbutton').click();
    });
}

function generateNoScheduleError(errormessage) {
    var elem =
        '<div class="col-sm-12 text-center">' +
            '<div class="alert alert-warning" role="alert">' +
                errormessage +
            '</div>' +
        '</div>';

    return elem;
}

function generateAvailableSlot(sched) {

    global_sched = sched.id;

    var elem =
        '<div class="col-sm-6">' +
            '<p>' + sched.time + '</p>' +
        '</div>' +
        '<div class="col-sm-6">' +
            // '<div onclick="setAppointment(' + sched.id+ ')" class="alert alert-primary alert-available text-center" role="alert" data-toggle="modal" data-target=".bd-example-modal-sm">' +
            '<div data-dismiss="modal" class="alert alert-primary alert-available text-center" role="alert" data-toggle="modal" data-target=".bd-example-modal-sm">' +
                '<b>Book Appointment</b>' +
            '</div>' +
        '</div>';


    return elem;
}

function generateNotAvailableSlot(sched) {

    var assignee = $('input[name=username]').val();
    
    if(assignee === sched.assignee) {
        var elem =
        '<div class="col-sm-6">' +
            '<p>' + sched.time + '</p>' +
        '</div>' +
        '<div class="col-sm-6">' +
            '<div onclick="cancelAppointment(' + sched.id + ')" class="alert alert-dark alert-cancel" role="alert">' +
                '<b>CANCEL SLOT</b>' +
            '</div>' +
        '</div>';
    } else {
        var elem =
        '<div class="col-sm-6">' +
            '<p>' + sched.time + '</p>' +
        '</div>' +
        '<div class="col-sm-6">' +
            '<div class="alert alert-danger" role="alert">' +
                '<b>NOT AVAILABLE</b>' +
            '</div>' +
        '</div>';
    }

    return elem;
}

function getSchedules(day) {

    var counselor = $('input[name=college]').val();

    var data = {
        'counselor': counselor,
        'day': day
    }

    console.log(JSON.stringify(data))

    var res = day.split(' ')
    
    res = res[1].split(',')[0]

    // Get the schedules for this college guidance counselor
    $.get("http://localhost:8000/openapp/getAppointmentSchedules/" + counselor, data, function(data) {

        if(data.rc === 'OK') {
            $('#slotter').empty();
            for(var i = 0; i < data.schedules.length; i++) {
                var sched = data.schedules[i];
                console.log(sched)
                if(sched.assignee === '' && sched.status === 'AVAILABLE') {
                    $('#slotter').append(generateAvailableSlot(sched));
                } else {
                        $('#slotter').append(generateNotAvailableSlot(sched));
                }
            }

        } else {
            $('#slotter').empty().append(generateNoScheduleError(data.message));
        }
    });

}

$(document).ready(function() {


});
