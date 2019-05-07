function validateInformationForm() {

    var schedule = $('[name=schedule]').val()
    var name = $('[name=name]').val()
    var id = $('[name=id]').val()
    var college = $('[name=college]').val()
    var yrcourse = $('[name=yrcourse]').val()
    var inlineRadioOptions = $('[name=inlineRadioOptions]').val()
    var studentyear = $('[name=studentyear]').val()
    var location = $('[name=location]').val()

    var req = {
        'schedule': schedule,
        'name': name,
        'id': id,
        'college': college,
        'yrcourse': yrcourse,
        'inlineRadioOptions': inlineRadioOptions,
        'location': location
    }

    var hasError = false;

    if (name === '') {
        hasError = true;
        $('[name=name]').removeClass('valid').addClass('invalid')
    } else {
        $('[name=name]').removeClass('invalid').addClass('valid')
    }

    if (id === '') {
        hasError = true;
        $('[name=id]').removeClass('valid').addClass('invalid')
    } else {
        $('[name=id]').removeClass('invalid').addClass('valid')
    }

    if (college === '') {
        hasError = true;
        $('[name=college]').removeClass('valid').addClass('invalid')
    } else {
        $('[name=college]').removeClass('invalid').addClass('valid')
    }

    if (yrcourse === '') {
        hasError = true;
        $('[name=yrcourse]').removeClass('valid').addClass('invalid')
    } else {
        $('[name=yrcourse]').removeClass('invalid').addClass('valid')
    }

    if (studentyear === '') {
        hasError = true;
        $('[name=studentyear]').removeClass('valid').addClass('invalid')
    } else {
        $('[name=studentyear]').removeClass('invalid').addClass('valid')
    }

    if (location === '') {
        hasError = true;
        $('[name=location]').removeClass('valid').addClass('invalid')
    } else {
        $('[name=location]').removeClass('invalid').addClass('valid')
    }

    if (hasError) {
        $('#errorcontainer').removeClass('hidden')
    } else {
        $('#errorcontainer').addClass('hidden')
        $('#informationForm').submit()
    }

}
