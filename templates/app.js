// static/app.js

document.addEventListener('DOMContentLoaded', () => {
    const helpBotContainer = document.getElementById('helpBotContainer');
    const helpBotToggle = document.getElementById('helpBotToggle');
    const helpBotInput = document.getElementById('helpBotInput');
    const helpBotBody = document.getElementById('helpBotBody');
    
    let isDragging = false;
    let offsetX, offsetY;

    // Toggle help bot visibility
    helpBotToggle.addEventListener('click', function() {
        const helpBot = document.getElementById('helpBot');
        if (helpBot.style.display === 'none' || helpBot.style.display === '') {
            helpBot.style.display = 'flex';
        } else {
            helpBot.style.display = 'none';
        }
    });

    // Make the help bot container draggable
    helpBotContainer.addEventListener('mousedown', function(event) {
        if (event.target === helpBotToggle || event.target.parentNode === helpBotToggle) {
            isDragging = true;
            offsetX = event.clientX - helpBotContainer.getBoundingClientRect().left;
            offsetY = event.clientY - helpBotContainer.getBoundingClientRect().top;
            document.addEventListener('mousemove', onMouseMove);
            document.addEventListener('mouseup', onMouseUp);
        }
    });

    function onMouseMove(event) {
        if (isDragging) {
            helpBotContainer.style.left = (event.clientX - offsetX) + 'px';
            helpBotContainer.style.top = (event.clientY - offsetY) + 'px';
        }
    }

    function onMouseUp() {
        isDragging = false;
        document.removeEventListener('mousemove', onMouseMove);
        document.removeEventListener('mouseup', onMouseUp);
    }

    // Handle user input
    helpBotInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            handleUserInput(event.target.value.trim());
        }
    });

    // Function to handle user input
    function handleUserInput(userInput) {
        if (userInput !== '') {
            // User message
            const userMessage = document.createElement('div');
            userMessage.classList.add('user-message');
            userMessage.textContent = userInput;
            helpBotBody.appendChild(userMessage);

            // Scroll to the bottom of the help bot body
            helpBotBody.scrollTop = helpBotBody.scrollHeight;

            // Clear the input
            helpBotInput.value = '';

            // Simulate bot response
            setTimeout(() => {
                const botResponse = document.createElement('div');
                botResponse.classList.add('bot-message');
                botResponse.innerHTML = `<i style="color: black" class="fa-regular fa-robot"></i> ${getBotResponse(userInput)}`;
                helpBotBody.appendChild(botResponse);

                // Scroll to the bottom of the help bot body
                helpBotBody.scrollTop = helpBotBody.scrollHeight;
            }, 500);
        }
    }

    // Fetch questions and answers from CSV file
    fetch('questions_and_answers.csv')
        .then(response => response.text())
        .then(text => {
            const rows = text.split('\n');
            const data = rows.map(row => row.split(','));
            const questions = data.map(row => row[0].trim());
            const answers = data.map(row => row[1].trim());

            // Map questions to answers
            const questionAnswerMap = {};
            questions.forEach((question, index) => {
                questionAnswerMap[question] = answers[index];
            });

            // Function to get bot response
            function getBotResponse(userInput) {
                const response = questionAnswerMap[userInput];
                return response || "I'm sorry, I don't have an answer to that question.";
            }
        })
        .catch(error => console.error('Error fetching CSV file:', error));

    // Add click event listeners to example questions
    document.querySelectorAll('.example-question').forEach(function(element) {
        element.addEventListener('click', function(event) {
            event.preventDefault();
            const question = event.target.textContent;
            handleUserInput(question);
        });
    });
});
