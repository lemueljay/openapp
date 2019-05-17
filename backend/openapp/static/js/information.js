function validateInformationForm() {

    var schedule = $('[name=schedule]').val()
    var name = $('[name=name]').val()
    var id = $('[name=id]').val()
    var college = $('[name=college]').val()
    var yrcourse = $('[name=yrcourse]').val()
    var studentyear = $('[name=studentyear]').val()
    var inlineRadioOptions = $('[name=inlineRadioOptions]').val()    
    var location = $('[name=location]').val()

    var req = {
        'schedule': schedule,
        'name': name,
        'id': id,
        'college': college,
        'yrcourse': yrcourse,
        'studentyear': studentyear,
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

$(document).ready(function() {
    $('[name=college]').on('change', function() {
        
        var selectedCollege = $('[name=college]').val()
        $('[name=yrcourse]').empty()
        console.log('changed')
        if(selectedCollege === 'College of Computer Studies (SCS)') {
            console.log('College of Computer Studies (SCS)')
            $('[name=yrcourse]').append('<option value="DIPLOMA IN ELECTRONICS ENGINEERING TECH (Computer Electronics)">DIPLOMA IN ELECTRONICS ENGINEERING TECH (Computer Electronics)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN INFORMATION SYSTEM">BACHELOR OF SCIENCE IN INFORMATION SYSTEMS</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN INFORMATION TECHNOLOG">BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY</option>')
            $('[name=yrcourse]').append('<option value="DIPLOMA IN ELECTRONICS TECHNOLOGY">DIPLOMA IN ELECTRONICS TECHNOLOGY</option>')
            $('[name=yrcourse]').append('<option value="DIPLOMA IN ELECTRONICS TECHNOLOGY">DIPLOMA IN ELECTRONICS TECHNOLOGY</option>')
            $('[name=yrcourse]').append('<option value="DIPLOMA IN ELECTRONICS ENGINEERING TECH (Communication Electronics)">DIPLOMA IN ELECTRONICS ENGINEERING TECH (Communication Electronics)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN COMPUTER SCIEN">BACHELOR OF SCIENCE IN COMPUTER SCIENCE</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN ELECTRONICS AND COMPUTER TECHNOLOGY (EMBEDDED SYSTEMS)">BACHELOR OF SCIENCE IN ELECTRONICS AND COMPUTER TECHNOLOGY (EMBEDDED SYSTEMS)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN ELECTRONICS AND COMPUTER TECHNOLOGY (COMMUNICATIONS SYSTEM)">BACHELOR OF SCIENCE IN ELECTRONICS AND COMPUTER TECHNOLOGY (COMMUNICATIONS SYSTEM)</option>                               ')
        } else if(selectedCollege === 'College of Education (CED)') {
            console.log('College of Education (CED)')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SECONDARY EDUCATION (BIOLOGY)">BACHELOR OF SECONDARY EDUCATION (BIOLOGY)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN INDUSTRIAL EDUCATION (DRAFTING)">BACHELOR OF SCIENCE IN INDUSTRIAL EDUCATION (DRAFTING)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SECONDARY EDUCATION (CHEMISTRY)">BACHELOR OF SECONDARY EDUCATION (CHEMISTRY)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SECONDARY EDUCATION (PHYSICS)">BACHELOR OF SECONDARY EDUCATION (PHYSICS)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SECONDARY EDUCATION (MATHEMATICS)">BACHELOR OF SECONDARY EDUCATION (MATHEMATICS)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SECONDARY EDUCATION (MAPEH)">BACHELOR OF SECONDARY EDUCATION (MAPEH)</option>')
            $('[name=yrcourse]').append('<option value="Certificate Program for Teachers">Certificate Program for Teachers</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SECONDARY EDUCATION (TLE)">BACHELOR OF SECONDARY EDUCATION (TLE)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SECONDARY EDUCATION (GENERAL SCIENCE)">BACHELOR OF SECONDARY EDUCATION (GENERAL SCIENCE)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF ELEMENTARY EDUCATION (ENGLISH)">BACHELOR OF ELEMENTARY EDUCATION (ENGLISH)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF ELEMENTARY EDUCATION (SCIENCE AND HEALTH)">BACHELOR OF ELEMENTARY EDUCATION (SCIENCE AND HEALTH)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN TECHNOLOGY TEACHER EDUCATION (INDUSTRIAL TECH)">BACHELOR OF SCIENCE IN TECHNOLOGY TEACHER EDUCATION (INDUSTRIAL TECH)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN TECHNOLOGY TEACHER EDUCATION (DRAFTING TECH)">BACHELOR OF SCIENCE IN TECHNOLOGY TEACHER EDUCATION (DRAFTING TECH)</option>')
        } else if(selectedCollege === 'College of Engineering and Technology (COET)') {
            console.log('College of Engineering and Technology (COET)')
            $('[name=yrcourse]').append('<option value="DIPLOMA IN CHEMICAL ENGINEERING TECHNOLOGY">DIPLOMA IN CHEMICAL ENGINEERING TECHNOLOGY</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN CIVIL ENGINEERING">BACHELOR OF SCIENCE IN CIVIL ENGINEERING</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN CERAMICS ENGINEERING">BACHELOR OF SCIENCE IN CERAMICS ENGINEERING</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN CHEMICAL ENGINEERING">BACHELOR OF SCIENCE IN CHEMICAL ENGINEERING</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN COMPUTER ENGINEERING">BACHELOR OF SCIENCE IN COMPUTER ENGINEERING</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN ELECTRONICS & COMMUNICATIONS ENGINEERING">BACHELOR OF SCIENCE IN ELECTRONICS & COMMUNICATIONS ENGINEERING</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN ELECTRICAL ENGINEERING">BACHELOR OF SCIENCE IN ELECTRICAL ENGINEERING</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN MINING ENGINEERING">BACHELOR OF SCIENCE IN MINING ENGINEERING</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN ENVIRONMENTAL ENGINEERING TECHNOLOGY">BACHELOR OF SCIENCE IN ENVIRONMENTAL ENGINEERING TECHNOLOGY</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN MECHANICAL ENGINEERING">BACHELOR OF SCIENCE IN MECHANICAL ENGINEERING</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE METALLURGICAL ENGINEERING">BACHELOR OF SCIENCE METALLURGICAL ENGINEERING</option>')
        } else if(selectedCollege === 'College of Arts and Social Sciences (CASS)') {
            console.log('College of Arts and Social Sciences (CASS)')
            $('[name=yrcourse]').append('<option value="GENERAL EDUCATION PROGRAM">GENERAL EDUCATION PROGRAM</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF ARTS IN ENGLISH">BACHELOR OF ARTS IN ENGLISH</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN PSYCHOLOGY">BACHELOR OF SCIENCE IN PSYCHOLOGY</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF ARTS IN FILIPINO">BACHELOR OF ARTS IN FILIPINO</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF ARTS IN HISTORY">BACHELOR OF ARTS IN HISTORY</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF ARTS IN POLITICAL SCIENCE">BACHELOR OF ARTS IN POLITICAL SCIENCE</option>')   
        } else if(selectedCollege === 'College of Business Administration and Accountancy (CBAA)') {
            console.log('College of Business Administration and Accountancy (CBAA)')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN BUSINESS ADMINISTRATION (BUSINESS ECONOMICS)">BACHELOR OF SCIENCE IN BUSINESS ADMINISTRATION (BUSINESS ECONOMICS)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN BUSINESS ADMINISTRATION (ECONOMICS)">BACHELOR OF SCIENCE IN BUSINESS ADMINISTRATION (ECONOMICS)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN BUSINESS ADMINISTRATION (ENTREPRENEURIAL MARKETING)">BACHELOR OF SCIENCE IN BUSINESS ADMINISTRATION (ENTREPRENEURIAL MARKETING)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN HOTEL AND RESTAURANT MANAGEMENT">BACHELOR OF SCIENCE IN HOTEL AND RESTAURANT MANAGEMENT</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN ACCOUNTANCY">BACHELOR OF SCIENCE IN ACCOUNTANCY</option>')
        } else if(selectedCollege === 'College of Science and Mathematics (CSM)') {
            console.log('College of Science and Mathematics (CSM)')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN BIOLOGY (BOTANY)">BACHELOR OF SCIENCE IN BIOLOGY (BOTANY)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN CHEMISTRY">BACHELOR OF SCIENCE IN CHEMISTRY</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN MATHEMATICS">BACHELOR OF SCIENCE IN MATHEMATICS</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN PHYSICS">BACHELOR OF SCIENCE IN PHYSICS</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN BIOLOGY (ZOOLOGY)">BACHELOR OF SCIENCE IN BIOLOGY (ZOOLOGY)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN BIOLOGY (MARINE)">BACHELOR OF SCIENCE IN BIOLOGY (MARINE)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN BIOLOGY (GENERAL)">BACHELOR OF SCIENCE IN BIOLOGY (GENERAL)</option>')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN STATISTICS">BACHELOR OF SCIENCE IN STATISTICS</option>')
        } else if(selectedCollege === 'College of Nursing (CON)') {
            console.log('College of Nursing (CON)')
            $('[name=yrcourse]').append('<option value="BACHELOR OF SCIENCE IN NURSING">BACHELOR OF SCIENCE IN NURSING</option>')            
        }
    })
})