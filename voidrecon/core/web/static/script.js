document.getElementById('myButton').addEventListener('click', () => {
    fetch('/button-click', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseText').textContent = data.message;
    })
    .catch(error => console.error('Error:', error));
});
