function checkAnswer(button, correctness) {
    var feedback = document.getElementById('feedback1');
    if (correctness === 'correct') {
        button.style.backgroundColor = 'green';
        feedback.innerHTML = 'Correct!';
    } else {
        button.style.backgroundColor = 'red';
        feedback.innerHTML = 'Incorrect';
    }
}

function checkFreeResponse() {
    var answer = document.getElementById('freeResponse').value;
    var feedback = document.getElementById('feedback2');
    if (answer === '8') {
        document.getElementById('freeResponse').style.backgroundColor = 'green';
        feedback.innerHTML = 'Correct!';
    } else {
        document.getElementById('freeResponse').style.backgroundColor = 'red';
        feedback.innerHTML = 'Incorrect';
    }
}
