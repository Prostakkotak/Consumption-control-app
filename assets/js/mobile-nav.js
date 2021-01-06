let bodyShadow = document.getElementById('body-shadow');

let dropDownNav = document.getElementsByClassName('nav')[0];

document.addEventListener('click', function (e) {
    if (e.target.id == 'trigram' || e.target.classList.contains('trigram__line')) {
        trigram.classList.toggle('open');
        dropDownNav.classList.toggle('open');
        bodyShadow.classList.toggle('active');
    } else if (dropDownNav.classList.contains('open') && e.target == bodyShadow) {
        trigram.classList.toggle('open');
        dropDownNav.classList.toggle('open');
        bodyShadow.classList.toggle('active');
    }
});