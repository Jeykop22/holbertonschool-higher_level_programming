fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    return response.json();
  })
  .then(data => {
    let characterElement = document.getElementById('character');
    characterElement.textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
