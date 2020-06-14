function displayDate() {
    current_date = new Date();

    year = current_date.getFullYear()
    month = current_date.getMonth() + 1;
    month = ((month < 10) ? '0' + month : month);
    day = current_date.getDate();
    day = ((day < 10) ? '0' + day : day);
    hour = current_date.getHours()
    hour = ((hour < 10) ? '0' + hour : hour);
    minute = current_date.getMinutes();
    minute = ((minute < 10) ? '0' + minute : minute);
    second = current_date.getSeconds();
    second = ((second < 10) ? '0' + second : second);

    document.getElementById('date').innerHTML = year + "/" + month + "/" + day + " " + hour + ":" + minute + ":" + second;

}
setInterval(displayDate, 1000);

var buttonAutomaticMode = document.getElementById('buttonAutomaticMode')
var buttonManualMode = document.getElementById('buttonManualMode')

var buttonPrograms = []
for (i = 0; i < 3; i++) (function (i) {
    buttonPrograms.push(document.getElementById('buttonProgram' + (i + 1)));
    buttonPrograms[i].onclick = function () {
        var btn = buttonPrograms[i]
        if (btn.classList.contains('btn-primary')) {
            btn.classList.add('btn-light');
            btn.classList.remove('btn-primary');
        } else {
            btn.classList.add('btn-primary');
            btn.classList.remove('btn-light');
        }
        changeControlMode('manual')
    }
})(i);

function setAutomaticControlMode() {
    buttonAutomaticMode.classList.remove('btn-light');
    buttonAutomaticMode.classList.add('btn-primary');

    buttonManualMode.classList.remove('btn-primary');
    buttonManualMode.classList.add('btn-light');
}

function setManualControlMode() {
    buttonManualMode.classList.remove('btn-light');
    buttonManualMode.classList.add('btn-primary');

    buttonAutomaticMode.classList.remove('btn-primary');
    buttonAutomaticMode.classList.add('btn-light');
}

buttonAutomaticMode.onclick = function () {
    setAutomaticControlMode();
}

buttonManualMode.onclick = function () {
    setManualControlMode();
}

function changeControlMode(mode) {
    if (mode == 'automatic') {
        setAutomaticControlMode();
    }
    if (mode == 'manual') {
        setManualControlMode();
    }
}

document.getElementById('buttonEditPrograms').onclick = function () {
    location.href = '/edit_programs';
};

// function buttonAutomaticMode() {
//     http.open("POST", url, true);
//     $.ajax({
//         type: "POST",
//         url: "/change_control_mode",
//         data: {
//             'control_mode': 'automatic'
//         }
//     });
// }

// function buttonManualMode() {
//     $.post("/change_control_mode", {
//         'control_mode': 'manual'
//     });
// }