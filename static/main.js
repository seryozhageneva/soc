function sendName() {
    const name = document.getElementById('nameInput').value;
    fetch('/greet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: name }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('greeting').innerText = data.greeting;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
