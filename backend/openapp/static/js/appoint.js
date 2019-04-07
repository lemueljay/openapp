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

    var elem =
        '<div class="col-sm-6">' +
            '<p>' + sched.time + '</p>' +
        '</div>' +
        '<div class="col-sm-6">' +
            '<div onclick="setAppointment(' + sched.id+ ')" class="alert alert-success alert-available" role="alert">' +
                '<b>SET APPOINTMENT</b>' +
            '</div>' +
        '</div>';


    return elem;
}

function generateNotAvailableSlot(sched) {

    var assignee = $('input[name=assignee]').val();

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

    // Get the schedules for this college guidance counselor
    $.get("http://localhost:8000/openapp/getAppointmentSchedules/" + counselor, data, function(data) {

        if(data.rc === 'OK') {
            $('#slotter').empty();
            for(var i = 0; i < data.schedules.length; i++) {
                var sched = data.schedules[i];
                if(sched.assignee === '') {
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
