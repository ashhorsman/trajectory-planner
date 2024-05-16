document.getElementById('trajectory-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    fetch('http://localhost:5000/calculate-trajectory', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
        document.getElementById('visualization-2d').innerText = '2D Visualization: ' + JSON.stringify(result);
        document.getElementById('visualization-3d').innerText = '3D Visualization: ' + JSON.stringify(result);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
