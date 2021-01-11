/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is not neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./js/delete-confirmation.js":
/*!***********************************!*\
  !*** ./js/delete-confirmation.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => /* binding */ deleteConfirmationPopUp\n/* harmony export */ });\nfunction deleteConfirmationPopUp(link, deleteObjName) {\r\n    document.addEventListener('DOMContentLoaded', () => {\r\n\r\n        if (!document.getElementById('body-shadow')) {\r\n            let bodyShadow = document.createElement('div');\r\n\r\n            bodyShadow.classList.add('body-shadow');\r\n            bodyShadow.id = 'body-shadow';\r\n\r\n            wrapper.appendChild(bodyShadow);\r\n        }\r\n\r\n        link.addEventListener('click', (e) => {\r\n            let evt = e ? e : window.event;\r\n\r\n            (evt.preventDefault) ? evt.preventDefault() : evt.returnValue = false;\r\n\r\n            let popUp = document.createElement('div'),\r\n                confirmButton = document.createElement('a'),\r\n                cancelButton = document.createElement('div'),\r\n                deleteWarning = document.createElement('div');\r\n\r\n            popUp.id = 'delete-pop-up';\r\n            popUp.classList.add('delete-pop-up');\r\n\r\n            confirmButton.classList.add('delete-pop-up__confirmation');\r\n            confirmButton.href = link.href;\r\n            confirmButton.textContent = 'Да';\r\n\r\n            cancelButton.id = 'delete-cancel';\r\n            cancelButton.classList.add('delete-pop-up__cancel');\r\n            cancelButton.textContent = 'Отмена';\r\n\r\n            deleteWarning.classList.add('delete-pop-up__warning');\r\n            deleteWarning.textContent = `Вы уверены что хотите удалить ${deleteObjName}?`;\r\n\r\n            popUp.append(deleteWarning, confirmButton, cancelButton);\r\n            document.getElementsByClassName('wrapper')[0].append(popUp);\r\n\r\n            document.getElementById('body-shadow').classList.add('active');\r\n\r\n            cancelButton.addEventListener('click', () => {\r\n                popUp.remove();\r\n                document.getElementById('body-shadow').classList.remove('active');\r\n            });\r\n        });\r\n\r\n        document.addEventListener('click', function (e) {\r\n            let target = e.target;\r\n\r\n            while (target != this) {\r\n\r\n                if (target.id == 'body-shadow' && document.getElementById('delete-pop-up')) {\r\n                    document.getElementById('delete-pop-up').remove();\r\n                    document.getElementById('body-shadow').classList.remove('active');\r\n                }\r\n\r\n                target = target.parentNode;\r\n            }\r\n        });\r\n    });\r\n}\n\n//# sourceURL=webpack://assets/./js/delete-confirmation.js?");

/***/ }),

/***/ "./js/index.js":
/*!*********************!*\
  !*** ./js/index.js ***!
  \*********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _delete_confirmation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./delete-confirmation */ \"./js/delete-confirmation.js\");\n\r\n\r\nlet deleteLinksList = document.getElementsByClassName('consumption-list__item-delete');\r\n\r\nfor (let i = 0; i < deleteLinksList.length; i++) {\r\n    (0,_delete_confirmation__WEBPACK_IMPORTED_MODULE_0__.default)(deleteLinksList[i], 'запись');\r\n}\n\n//# sourceURL=webpack://assets/./js/index.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		if(__webpack_module_cache__[moduleId]) {
/******/ 			return __webpack_module_cache__[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => Object.prototype.hasOwnProperty.call(obj, prop)
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	// startup
/******/ 	// Load entry module
/******/ 	__webpack_require__("./js/index.js");
/******/ 	// This entry module used 'exports' so it can't be inlined
/******/ })()
;