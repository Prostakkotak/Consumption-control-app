/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is not neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/*!**************************!*\
  !*** ./js/mobile-nav.js ***!
  \**************************/
eval("bodyShadow = document.getElementById('body-shadow');\r\n\r\nlet dropDownNav = document.getElementsByClassName('nav')[0];\r\n\r\ndocument.addEventListener('click', function (e) {\r\n    if (e.target.id == 'trigram' || e.target.classList.contains('trigram__line')) {\r\n        trigram.classList.toggle('open');\r\n        dropDownNav.classList.toggle('open');\r\n        bodyShadow.classList.toggle('active');\r\n    }\r\n})\n\n//# sourceURL=webpack://assets/./js/mobile-nav.js?");
/******/ })()
;