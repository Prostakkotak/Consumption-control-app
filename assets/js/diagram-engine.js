/* Движок построения диаграммы */

const diagramLines = [
    document.getElementById('property'),
    document.getElementById('health'),
    document.getElementById('presents'),
    document.getElementById('travel'),
    document.getElementById('personal'),
    document.getElementById('clothes'),
    document.getElementById('food'),
    document.getElementById('help'),
    document.getElementById('personal_transport'),
    document.getElementById('public_transport'),
    document.getElementById('other')
];

let diagramPercents = [];

for (let i = 0; i < diagramLines.length; i++) {
    diagramPercents[i] = parseFloat(document.getElementsByClassName('hidden-diagram-percent')[i].textContent);
}

let linesSum = diagramPercents[0];

for (let i = 1; i <= 10; i++) {
    diagramLines[i].setAttribute('stroke-dasharray', diagramPercents[i] + ' ' + (100 - diagramPercents[i]));
    diagramLines[i].setAttribute('stroke-dashoffset', 100 - linesSum + 25);

    linesSum += diagramPercents[i];
}