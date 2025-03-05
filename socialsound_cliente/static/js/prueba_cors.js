
function pruebaCORS() {
    const resultElement = document.getElementById('cors-result');
    resultElement.innerHTML = 'Haciendo petición...';
    resultElement.className = 'alert alert-info';

    const apiUrl = 'https://lolosoloyolo.pythonanywhere.com/api/v1/prueba-cors/'
    // const apiUrl = 'http://127.0.0.1:8000/api/v1/prueba-cors/';

    fetch(apiUrl, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include'
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Éxito:', data);
            resultElement.innerHTML = `
            <p><strong>Estado:</strong> ${data.status}</p>
            <p><strong>Mensaje:</strong> ${data.message}</p>
            <p>¡Configuración de CORS exitosa!</p>
        `;
            resultElement.className = 'alert alert-success';
        })
        .catch(error => {
            console.error('Error:', error);
            resultElement.innerHTML = `
            <p><strong>Error:</strong> ${error.message}</p>
            <p>La configuración de CORS falló. Verifica tu configuración.</p>
        `;
            resultElement.className = 'alert alert-danger';
        });
}