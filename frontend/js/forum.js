// URL API для взаимодействия с backend
const API_URL = '/api/backend/';

// Загружаем существующие темы при загрузке страницы
document.addEventListener('DOMContentLoaded', loadTopics);

// Кнопки и элементы всплывающего окна
const createTopicButton = document.getElementById('create-topic-button');
const modal = document.getElementById('create-topic-modal');
const closeModalButton = document.querySelector('.close');
const submitTopicButton = document.getElementById('submit-topic');
const topicTitleInput = document.getElementById('topic-title');

// Открытие модального окна
createTopicButton.addEventListener('click', () => {
    modal.style.display = 'block';
});

// Закрытие модального окна (по нажатию на крестик)
closeModalButton.addEventListener('click', () => {
    modal.style.display = 'none';
});

// Закрытие модального окна при нажатии вне модального окна
window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

// Обработчик отправки новой темы
submitTopicButton.addEventListener('click', async () => {
    const title = topicTitleInput.value.trim();
    
    if (title === '') {
        alert('Title cannot be empty');
        return;
    }

    try {
        const response = await fetch(`${API_URL}topics`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title })
        });

        if (response.ok) {
            const newTopic = await response.json();
            addTopicToDOM(newTopic);
            topicTitleInput.value = ''; // Очистка поля ввода
            modal.style.display = 'none'; // Закрытие модального окна
        } else {
            const error = await response.json();
            alert(`Error: ${error.message}`);
        }
    } catch (error) {
        console.error('Error creating topic:', error);
    }
});

// Загрузка существующих тем с бэкенда
async function loadTopics() {
    try {
        const response = await fetch(`${API_URL}topics`);
        const topics = await response.json();
        topics.forEach(addTopicToDOM);
    } catch (error) {
        console.error('Error loading topics:', error);
    }
}

// Добавление темы в DOM
function addTopicToDOM(topic) {
    const topicsContainer = document.getElementById('topics-container');
    const topicElement = document.createElement('div');
    topicElement.classList.add('topics');
    topicElement.innerHTML = `
        <h3>${topic.title}</h3>
        <p>Created on: ${new Date(topic.created_at).toLocaleString()}</p>
    `;
    topicsContainer.appendChild(topicElement);
}
