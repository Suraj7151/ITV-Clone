
function toggleAnswer(button) {
    const answer = button.nextElementSibling;
    const isVisible = answer.style.display === 'block';
    document.querySelectorAll('.faq-answer').forEach(ans => ans.style.display = 'none');
    if (!isVisible) {
        answer.style.display = 'block';
    } else {
        answer.style.display = 'none';
    }
}

console.log('Hello')