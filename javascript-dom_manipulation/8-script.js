document.addEventListener('DOMContentLoaded', function() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => {
        return response.json();
      })
      .then(data => {
        let helloElement = document.getElementById('hello');
        helloElement.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });
