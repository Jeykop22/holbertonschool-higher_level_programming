let updateHeaderElement = document.getElementById('update_header');
updateHeaderElement.addEventListener('click', function() {
    let headerElement = document.querySelector('header');
    headerElement.textContent = 'New Header!!!';
});
