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
            '<div class="alert alert-primary alert-available text-center" role="alert" data-dismiss="modal" data-toggle="modal" data-target=".bd-example-modal-sm">' +
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

function bookAppointment(sched) {
    this.global_sched = sched;
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
        
        console.log(data)

        if(data[0]) {
            $('#0box').empty().append('<input onclick=bookAppointment("' + data['id0'] + '") type="button" class="btn btn-primary" value="BOOK APPOINTMENT" data-dismiss="modal" data-toggle="modal" data-target=".bd-example-modal-sm">')
        } else {
            $('#0box').empty().append('<input type="button" class="form-control btn btn-danger" value="     NOT AVAILABLE     " disabled>')
        }

        if(data[1]) {
            $('#1box').empty().append('<input onclick=bookAppointment("' + data['id1'] + '") type="button" class="btn btn-primary" value="BOOK APPOINTMENT" data-dismiss="modal" data-toggle="modal" data-target=".bd-example-modal-sm">')
        } else {
            $('#1box').empty().append('<input type="button" class="btn btn-danger" value="     NOT AVAILABLE     " disabled>')
        }

        if(data[2]) {
            $('#2box').empty().append('<input onclick=bookAppointment("' + data['id2'] + '") type="button" class="btn btn-primary" value="BOOK APPOINTMENT" data-dismiss="modal" data-toggle="modal" data-target=".bd-example-modal-sm">')
        } else {
            $('#2box').empty().append('<input type="button" class="btn btn-danger" value="     NOT AVAILABLE     " disabled>')
        }

        if(data[3]) {
            $('#3box').empty().append('<input onclick=bookAppointment("' + data['id3'] + '") type="button" class="btn btn-primary" value="BOOK APPOINTMENT" data-dismiss="modal" data-toggle="modal" data-target=".bd-example-modal-sm">')
        } else {
            $('#3box').empty().append('<input type="button" class="btn btn-danger" value="     NOT AVAILABLE     " disabled>')
        }

        if(data[4]) {
            $('#4box').empty().append('<input onclick=bookAppointment("' + data['id4'] + '") type="button" class="btn btn-primary" value="BOOK APPOINTMENT" data-dismiss="modal" data-toggle="modal" data-target=".bd-example-modal-sm">')
        } else {
            $('#4box').empty().append('<input type="button" class="btn btn-danger" value="     NOT AVAILABLE     " disabled>')
        }

        if(data[5]) {
            $('#5box').empty().append('<input onclick=bookAppointment("' + data['id5'] + '") type="button" class="btn btn-primary" value="BOOK APPOINTMENT" data-dismiss="modal" data-toggle="modal" data-target=".bd-example-modal-sm">')
        } else {
            $('#5box').empty().append('<input type="button" class="btn btn-danger" value="     NOT AVAILABLE     " disabled>')
        }

        if(data[6]) {
            $('#6box').empty().append('<input onclick=bookAppointment("' + data['id6'] + '") type="button" class="btn btn-primary" value="BOOK APPOINTMENT" data-dismiss="modal" data-toggle="modal" data-target=".bd-example-modal-sm">')
        } else {
            $('#6box').empty().append('<input type="button" class="btn btn-danger" value="     NOT AVAILABLE     " disabled>')
        }

        if(data[7]) {
            $('#7box').empty().append('<input onclick=bookAppointment("' + data['id7'] + '") type="button" class="btn btn-primary" value="BOOK APPOINTMENT" data-dismiss="modal" data-toggle="modal" data-target=".bd-example-modal-sm">')
        } else {
            $('#7box').empty().append('<input type="button" class="btn btn-danger" value="     NOT AVAILABLE     " disabled>')
        }

    });

}

$(document).ready(function() {

    $('#prevslide').on('click', function() {
        $(this).toggleClass('fas').toggleClass('far')
        $('#nextslide').toggleClass('fas').toggleClass('far')
        $('#carouselExampleControls').carousel('prev')
    })

    $('#nextslide').on('click', function() {
        $(this).toggleClass('fas').toggleClass('far')
        $('#prevslide').toggleClass('fas').toggleClass('far')
        $('#carouselExampleControls').carousel('next')
    })
});
