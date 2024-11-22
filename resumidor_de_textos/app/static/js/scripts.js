// Handle File Upload
document.getElementById("fileInput").addEventListener("change", (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById("textInput").value = e.target.result;
        };
        reader.readAsText(file);
    }
});

function countWords(text) {
    if (!text.trim()) return 0; // Handle empty input
    return text.trim().split(/\s+/).length; // Split by whitespace and count words
}

// Attach event listener to textarea
const textInput = document.getElementById("textInput");
const wordCountDisplay = document.getElementById("wordCount");

textInput.addEventListener("input", () => {
    const text = textInput.value;
    const wordCount = countWords(text);
    wordCountDisplay.textContent = `Word Count: ${wordCount}`;
});

document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('textInput');
    const wordCount = document.getElementById('wordCount');

    // Actualizar el contador de palabras a medida que el usuario escribe
    textInput.addEventListener('input', () => {
        const words = textInput.value.trim().split(/\s+/).filter(word => word.length > 0);
        wordCount.textContent = `Word count: ${words.length}`;
    });
});



