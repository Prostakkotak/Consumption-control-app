/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is not neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/*!******************************!*\
  !*** ./js/diagram-engine.js ***!
  \******************************/
eval("/* Движок построения диаграммы */\n\nconst diagramLines = [\n    document.getElementById('property'),\n    document.getElementById('health'),\n    document.getElementById('presents'),\n    document.getElementById('travel'),\n    document.getElementById('personal'),\n    document.getElementById('clothes'),\n    document.getElementById('food'),\n    document.getElementById('help'),\n    document.getElementById('personal_transport'),\n    document.getElementById('public_transport'),\n    document.getElementById('other')\n];\n\nlet diagramPercents = [];\n\nfor (let i = 0; i < diagramLines.length; i++) {\n    diagramPercents[i] = parseFloat(document.getElementsByClassName('hidden-diagram-percent')[i].textContent);\n}\n\nlet linesSum = diagramPercents[0];\n\nfor (let i = 1; i <= 10; i++) {\n    diagramLines[i].setAttribute('stroke-dasharray', diagramPercents[i] + ' ' + (100 - diagramPercents[i]));\n    diagramLines[i].setAttribute('stroke-dashoffset', 100 - linesSum + 25);\n\n    linesSum += diagramPercents[i];\n}\n\n//# sourceURL=webpack://assets/./js/diagram-engine.js?");
/******/ })()
;