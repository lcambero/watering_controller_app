document.getElementById('buttonReturn').onclick = function () {
    location.href = '/';
};

function httpGet(url) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open('GET', url, false); // false for synchronous request
    xmlHttp.send(null);
    return JSON.parse(xmlHttp.responseText);
}

window.onload = function () {
    httpGetRequestPrograms();
}

function httpGetRequestPrograms() {
    var programs = httpGet('/programs')

    for (let index = 0; index < programs['n_programs']; index++) {
        createProgramConsole(programs['programs'][index]);
    }
}

function createProgramConsole(program) {
    var mainCol = document.getElementById('programsConsoleCol');

    var programConsoleRow = document.createElement('div');
    programConsoleRow.setAttribute('id', 'programConsoleRow' + program['id']);
    programConsoleRow.setAttribute('class', 'row div-border my-3');
    mainCol.appendChild(programConsoleRow);

    var programConsoleCol = document.createElement('div');
    programConsoleCol.setAttribute('id', 'programConsoleCol' + program['id']);
    programConsoleCol.setAttribute('class', 'col');
    programConsoleRow.appendChild(programConsoleCol);

    var titleRow = document.createElement('div');
    titleRow.setAttribute('class', 'row justify-content-between py-3');
    programConsoleCol.appendChild(titleRow);

    var titleCol = document.createElement('div');
    titleCol.setAttribute('class', 'col-auto');
    titleRow.appendChild(titleCol);

    var titleH = document.createElement('h2');
    titleH.innerText = 'Programa ' + program['id'];
    titleCol.appendChild(titleH);

    var configRow = document.createElement('div');
    configRow.setAttribute('id', 'programConsoleConfigRow' + program['id']);
    configRow.setAttribute('class', 'row pb-3');
    programConsoleCol.appendChild(configRow);

    createDaysStartsConfig(program['id'], program['days'], program['starts']);
    createCircuitsConfig(program['id'], program['circuits']);
}

function createDaysStartsConfig(idx, days, starts) {
    var mainRow = document.getElementById('programConsoleConfigRow' + idx);

    var configCol = document.createElement('div');
    configCol.setAttribute('id', 'programConsoleConfigCol' + idx);
    configCol.setAttribute('class', 'col-3 col-md-4');
    mainRow.appendChild(configCol);

    for (let index = 1; index <= Object.keys(starts).length; index++) {
        var startHourRow = document.createElement('div');
        startHourRow.setAttribute('class', 'row justify-content-start');
        configCol.appendChild(startHourRow);

        var startHourCol = document.createElement('div');
        startHourCol.setAttribute('class', 'col');
        startHourRow.appendChild(startHourCol);

        var inputGroupDiv = document.createElement('div');
        inputGroupDiv.setAttribute('class', 'input-group mb-3');
        startHourCol.appendChild(inputGroupDiv);

        var inputGroupButtonDiv = document.createElement('div');
        inputGroupButtonDiv.setAttribute('class', 'input-group-prepend');
        inputGroupDiv.appendChild(inputGroupButtonDiv);

        var inputGroupButton = document.createElement('button');
        inputGroupButton.setAttribute('class', 'btn btn-outline-secondary');
        inputGroupButton.setAttribute('type', 'button');
        inputGroupButton.innerText = 'Hora inicio ' + index;
        inputGroupButtonDiv.appendChild(inputGroupButton);

        var inputGroupInput = document.createElement('input');
        inputGroupInput.setAttribute('class', 'form-control');
        inputGroupInput.setAttribute('type', 'text');
        inputGroupInput.setAttribute('aria-describedby', 'basic-addon1');
        inputGroupInput.value = starts[index];
        inputGroupDiv.appendChild(inputGroupInput);
    }

    var daysRow = document.createElement('div');
    daysRow.setAttribute('class', 'row justify-content-center');
    configCol.appendChild(daysRow);

    var daysCol = document.createElement('div');
    daysCol.setAttribute('class', 'col-auto py-2');
    daysRow.appendChild(daysCol);

    var toolbarDiv = document.createElement('div');
    toolbarDiv.setAttribute('class', 'btn-toolbar');
    toolbarDiv.setAttribute('role', 'toolbar');
    daysCol.appendChild(toolbarDiv);

    var buttonsGroupDiv = document.createElement('div');
    buttonsGroupDiv.setAttribute('class', 'btn-group mr-2');
    buttonsGroupDiv.setAttribute('role', 'group');
    toolbarDiv.appendChild(buttonsGroupDiv);

    for (d of ['L', 'M', 'X', 'J', 'V', 'S', 'D']) {
        var buttonDay = document.createElement('div');
        buttonDay.setAttribute('class', 'btn btn-light');
        buttonDay.setAttribute('type', 'button');
        buttonDay.innerText = d;
        buttonsGroupDiv.appendChild(buttonDay);
    }

}

function createCircuitsConfig(idx, circuits) {
    var mainRow = document.getElementById('programConsoleConfigRow' + idx);

}