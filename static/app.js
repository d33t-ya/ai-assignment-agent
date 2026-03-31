
function formatAIResponse(text) {
    // Remove confusing markdown (###, **, etc), keep bullets and newlines
    let html = text
        .replace(/\n\s*\n/g, '<br><br>') // double newlines to paragraph breaks
        .replace(/\n- /g, '<br>&bull; ') // markdown bullets to HTML bullets
        .replace(/\n\d+\. /g, match => '<br>' + match.trim()) // numbered lists
        .replace(/\n/g, '<br>') // single newlines to line breaks
        .replace(/#+\s?/g, '') // remove markdown headers
        .replace(/\*\*(.*?)\*\*/g, '<b>$1</b>') // bold
        .replace(/\*/g, '') // remove stray asterisks
        .replace(/`/g, '') // remove code formatting
    ;
    return html;
}

document.getElementById('submit').addEventListener('click', async function() {
    const question = document.getElementById('question').value;
    document.getElementById('features').textContent = '';
    document.getElementById('output').innerHTML = 'Loading...';
    const response = await fetch('/api/explain', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question })
    });
    const data = await response.json();
    document.getElementById('features').textContent = 'Features: ' + JSON.stringify(data.features, null, 2);
    document.getElementById('output').innerHTML = formatAIResponse(data.result);
});
