async function performSearch() {
    const query = document.getElementById('searchInput').value.trim();
    if (!query) {
        alert('Please enter a search word.');
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:8000/search/?query=${query}`);
        if (response.ok) {
            const files = await response.json();
            const resultsList = document.getElementById('resultsList');
            resultsList.innerHTML = '';
            files.forEach(file => {
                const li = document.createElement('li');
                li.textContent = file;
                resultsList.appendChild(li);
            });
        } else if (response.status === 404) {
            alert('Word not found in any file.');
        } else {
            alert('Search failed.');
        }
    } catch (error) {
        alert('Error connecting to the backend server.');
    }
}