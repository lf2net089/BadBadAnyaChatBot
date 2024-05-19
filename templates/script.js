const userId = generateUUID();
document.addEventListener('DOMContentLoaded', function() {
    console.log("The DOM has loaded.");
    const testElement = document.getElementById('someElementId'); // Replace 'someElementId' with an actual ID from your HTML
    if(testElement) {
        console.log("Element found:", testElement);
    } else {
        console.log("Element not found.");
    }
});

function handleKeyPress(event) {
    if (event.key === 'Enter') {
		console.log("hi");
        const userInput = event.target.value;
        fetchSuggestions(userInput);
        event.target.value = ''; 
    }
}

function fetchSuggestions(query) {
    const url = 'https://api.dify.ai/v1/messages/{message_id}/suggested';
    const data = {
        user: userId, 
    };

    fetch(url.replace('{message_id}', 'your_message_id_here'), {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer Cm3cPyFBhOmgWIqg',
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Suggested Questions:', data.data);
        displaySuggestions(data.data);
    })
    .catch(error => console.error('Error fetching suggestions:', error));
}

function displaySuggestions(suggestions) {

    console.log(suggestions);
}
function generateUUID() {
    return crypto.randomUUID();
}
