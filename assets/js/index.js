import deleteConfirmationPopUp from './delete-confirmation';

let deleteLinksList = document.getElementsByClassName('consumption-list__item-delete');

for (let i = 0; i < deleteLinksList.length; i++) {
    deleteConfirmationPopUp(deleteLinksList[i], 'запись');
}