document.getElementById('encodeForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    fetch('/encode', {
        method: 'POST',
        body: formData,
    }).then(response => response.blob())
    .then(imageBlob => {
        const imageUrl = URL.createObjectURL(imageBlob);
        document.getElementById('encodedImage').innerHTML = `<img src="${imageUrl}" alt="Encoded Image"/>`;
    });
});

document.getElementById('decodeForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    fetch('/decode', {
        method: 'GET',
        body: formData,
    }).then(response => response.text())
    .then(text => {
        document.getElementById('decodedMessage').innerText = 'Decoded message: ' + text;
    });
});

