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
eval("/* Движок построения диаграммы */\r\n\r\nconst diagramLines = [\r\n    document.getElementById('property'),\r\n    document.getElementById('health'),\r\n    document.getElementById('presents'),\r\n    document.getElementById('travel'),\r\n    document.getElementById('personal'),\r\n    document.getElementById('clothes'),\r\n    document.getElementById('food'),\r\n    document.getElementById('help'),\r\n    document.getElementById('personal_transport'),\r\n    document.getElementById('public_transport'),\r\n    document.getElementById('other')\r\n];\r\n\r\nlet diagramPercents = [];\r\n\r\nfor (let i = 0; i < diagramLines.length; i++) {\r\n    diagramPercents[i] = parseFloat(document.getElementsByClassName('hidden-diagram-percent')[i].textContent);\r\n}\r\n\r\nlet linesSum = diagramPercents[0];\r\n\r\nfor (let i = 1; i <= 10; i++) {\r\n    diagramLines[i].setAttribute('stroke-dasharray', diagramPercents[i] + ' ' + (100 - diagramPercents[i]));\r\n    diagramLines[i].setAttribute('stroke-dashoffset', 100 - linesSum + 25);\r\n\r\n    linesSum += diagramPercents[i];\r\n}\n\n//# sourceURL=webpack://assets/./js/diagram-engine.js?");
/******/ })()
;