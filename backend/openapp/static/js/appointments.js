var day = null;

function generateNoScheduleError(errormessage) {
    var elem =
        '<div class="col-sm-12 text-center">' +
            '<div class="alert alert-warning" role="alert">' +
                errormessage +
            '</div>' +
        '</div>';

    return elem;
}

function generateSlots(sched) {
    var elem =
        '<div class="col-sm-6">' +
            '<p>' + sched.time + '</p>' +
        '</div>' +
        '<div class="col-sm-6">' +
            '<div onclick="deleteappointment(' + sched.id+ ')" class="alert alert-danger alert-notavail" role="alert">' +
                '<b>DELETE APPOINTMENT</b>' +
            '</div>' +
        '</div>';


    return elem;
}

function deleteappointment(id) {
    var data = {
        'id': id
    }

    console.log(data)

    $.get("http://localhost:8000/openapp/deleteappointments", data, function(data) {
        $('input[name=createappointments]').val('');
        $('#modalBbutton').click();

    });
}

function getSchedules(day) {

    var counselor = $('input[name=college]').val();
    this.day = day;

    var data = {
        'counselor': counselor,
        'day': this.day
    }

    console.log(JSON.stringify(data))

    // Get the schedules for this college guidance counselor
    $.get("http://localhost:8000/openapp/getAppointmentSchedules/" + counselor, data, function(data) {

        if(data.rc === 'OK') {
            $('#slotter').empty();
            for(var i = 0; i < data.schedules.length; i++) {
                var sched = data.schedules[i];
                $('#slotter').append(generateSlots(sched));
            }

        } else {
            $('#slotter').empty().append(generateNoScheduleError(data.message));
        }
    });

}

function createappointments() {

    var schedule = $('input[name=createappointments]').val();

    var data = {
        'schedule': schedule,
        'day': this.day
    }

    console.log(data);

    $.get('http://localhost:8000/openapp/createappointments', data, function(data) {
        console.log(data)
    })

    $('input[name=createappointments]').val('');
    $('#modalBbutton').click();
}

$(document).ready(function() {

})