fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    return response.json();
  })
  .then(data => {
    let moviesListElement = document.getElementById('list_movies');
    data.results.forEach(movie => {
      let listItem = document.createElement('li');
      listItem.textContent = movie.title;
      moviesListElement.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
