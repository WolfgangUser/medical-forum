const API_BASE_URL = 'http://localhost/api';

async function loadTopics() {
    const response = await fetch(`${API_BASE_URL}/topics`);
    const topics = await response.json();
    const topicsContainer = document.getElementById('forum-topics');
    topics.forEach(topic => {
        const topicElement = document.createElement('div');
        topicElement.innerHTML = `<a href="forum.html?id=${topic.id}">${topic.title}</a>`;
        topicsContainer.appendChild(topicElement);
    });
}

async function login(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    });

    if (response.ok) {
        alert('Вход выполнен!');
    } else {
        alert('Ошибка входа');
    }
}

async function register(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const response = await fetch(`${API_BASE_URL}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    });

    if (response.ok) {
        alert('Регистрация успешна!');
    } else {
        alert('Ошибка регистрации');
    }
}
