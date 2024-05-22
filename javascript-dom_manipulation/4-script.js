let addItemElement = document.getElementById('add_item');
addItemElement.addEventListener('click', function() {

    let newListItem = document.createElement('li');
    newListItem.textContent = 'Item';
    let myList = document.querySelector('.my_list');
    myList.appendChild(newListItem);
});