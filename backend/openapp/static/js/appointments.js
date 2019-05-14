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

    console.log(JSON.stringify(data));

    $.get("http://localhost:8000/openapp/gccAppointmentSchedules/" + counselor, data, function(data) {

        console.log(JSON.stringify(data))

        $('#morning_session').empty()
        $('#noon_session').empty()

        if(data['morning_sched']) {
            data['morning_sched'].forEach(function(sched) {
                if(sched['sched_available']) {
                    $('#morning_session').append('' +
                        '<div class="timebox">' +
                            '<span>' + sched['sched_time'] + '</span>' +
                            '<span class="timebutton btn-group btn-group-toggle" data-toggle="buttons">' +
                            '<label onclick="setAvailable(\'' + sched['sched_time'] + '\')" class="btn btn-outline-primary active">' +
                                '<input type="radio" name="optionB" autocomplete="off" checked> A' +
                            '</label>' +
                            '<label onclick="setNotAvailable(\'' + sched['sched_time'] + '\')" class="btn btn-outline-primary">' +
                                '<input type="radio" name="optionA" autocomplete="off" value="b"> NA' +
                            '</label>' +
                        '</div>' +
                    '')
                } else {
                    $('#morning_session').append('' +
                    '<div class="timebox">' +
                        '<span>' + sched['sched_time'] + '</span>' +
                        '<span class="timebutton btn-group btn-group-toggle" data-toggle="buttons">' +
                        '<label onclick="setAvailable(\'' + sched['sched_time'] + '\')" class="btn btn-outline-primary">' +
                            '<input type="radio" name="optionB" autocomplete="off" checked> A' +
                        '</label>' +
                        '<label onclick="setNotAvailable(\"' + sched['sched_time'] + '\")" class="btn btn-outline-primary active">' +
                            '<input type="radio" name="optionA" autocomplete="off" value="b"> NA' +
                        '</label>' +
                    '</div>' +
                '')
                }
            })
        }

        if(data['noon_sched']) {
            data['noon_sched'].forEach(function(sched) {
                if(sched['sched_available']) {
                    $('#noon_session').append('' +
                        '<div class="timebox">' +
                            '<span>' + sched['sched_time'] + '</span>' +
                            '<span class="timebutton btn-group btn-group-toggle" data-toggle="buttons">' +
                            '<label onclick="setAvailable(\'' + sched['sched_time'] + '\')" class="btn btn-outline-primary active">' +
                                '<input type="radio" name="optionB" autocomplete="off" checked> A' +
                            '</label>' +
                            '<label onclick="setNotAvailable(\'' + sched['sched_time'] + '\')" class="btn btn-outline-primary">' +
                                '<input type="radio" name="optionA" autocomplete="off" value="b"> NA' +
                            '</label>' +
                        '</div>' +
                    '')
                } else {
                    $('#noon_session').append('' +
                    '<div class="timebox">' +
                        '<span>' + sched['sched_time'] + '</span>' +
                        '<span class="timebutton btn-group btn-group-toggle" data-toggle="buttons">' +
                        '<label onclick="setAvailable(\'' + sched['sched_time'] + '\')" class="btn btn-outline-primary">' +
                            '<input type="radio" name="optionB" autocomplete="off" checked> A' +
                        '</label>' +
                        '<label onclick="setNotAvailable(\'' + sched['sched_time'] + '\')" class="btn btn-outline-primary active">' +
                            '<input type="radio" name="optionA" autocomplete="off" value="b"> NA' +
                        '</label>' +
                    '</div>' +
                '')
                }
            })
           
        }
        // // Update data
        // if(data[0]) {
        //     $('#0A').addClass('active')
        //     $('#0B').removeClass('active')
        // } else {
        //     $('#0A').removeClass('active')
        //     $('#0B').addClass('active')
        // }

        // if(data[1]) {
        //     $('#1A').addClass('active')
        //     $('#1B').removeClass('active')
        // } else {
        //     $('#1A').removeClass('active')
        //     $('#1B').addClass('active')
        // }

        // if(data[2]) {
        //     $('#2A').addClass('active')
        //     $('#2B').removeClass('active')
        // } else {
        //     $('#2A').removeClass('active')
        //     $('#2B').addClass('active')
        // }

        // if(data[3]) {
        //     $('#3A').addClass('active')
        //     $('#3B').removeClass('active')
        // } else {
        //     $('#3A').removeClass('active')
        //     $('#3B').addClass('active')
        // }

        // if(data[4]) {
        //     $('#4A').addClass('active')
        //     $('#4B').removeClass('active')
        // } else {
        //     $('#4A').removeClass('active')
        //     $('#4B').addClass('active')
        // }

        // if(data[5]) {
        //     $('#5A').addClass('active')
        //     $('#5B').removeClass('active')
        // } else {
        //     $('#5A').removeClass('active')
        //     $('#5B').addClass('active')
        // }

        // if(data[6]) {
        //     $('#6A').addClass('active')
        //     $('#6B').removeClass('active')
        // } else {
        //     $('#6A').removeClass('active')
        //     $('#6B').addClass('active')
        // }

        // if(data[7]) {
        //     $('#7A').addClass('active')
        //     $('#7B').removeClass('active')
        // } else {
        //     $('#7A').removeClass('active')
        //     $('#7B').addClass('active')
        // }
        $('[name=createappointments], #saveButton').hide();
        $('#createButton').show()
        $('#scheduleModal').modal('show')
    });
    

    
}

function createappointments() {

    var schedule = $('input[name=createappointments]').val();

    if(schedule !== ''){
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
}

function setAvailable(sched) {

    var data = {
        'status': 'AVAILABLE',
        'sched': sched,
        'day': this.day
    }
    console.log(JSON.stringify(data))

    $.get('http://localhost:8000/openapp/setGccAppointmentSchedule', data, function(data) {
        console.log(data)
    })
}

function setNotAvailable(sched) {

    var data = {
        'status': 'NOT_AVAILABLE',
        'sched': sched,
        'day': this.day
    }
    
    $.get('http://localhost:8000/openapp/setGccAppointmentSchedule', data, function(data) {
        console.log(data)
    })
}

function showCreateButton() {
    $('#createButton').hide()
    $('[name=createappointments], #saveButton').show()
}

$(document).ready(function() {

    $('[name=createappointments], #saveButton').hide();

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
    
})