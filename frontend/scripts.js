const API_AUTH_URL = '/api/auth/';
const API_BACKEND_URL = '/api/backend/';

window.onload = function() {
    const savedUsername = localStorage.getItem('username');
    if (savedUsername) {
        
        authContainer.style.display = 'none';
        header.style.display = 'flex';
    }
};

function saveLogin(username) {
    localStorage.setItem('username', username);
}

function removeLogin() {
    localStorage.removeItem('username');
}




// Elements
const loginBtn = document.getElementById('login-btn');
const registerBtn = document.getElementById('register-btn');

const logoutBtn = document.getElementById('logout-btn');
const createTopicBtn = document.getElementById('create-topic-btn');

const authContainer = document.getElementById('auth-container');
const header = document.getElementById('header');
const mainContent = document.getElementById('main-content');

const loginModal = document.getElementById('login-modal');
const registerModal = document.getElementById('register-modal');
const topicModal = document.getElementById('topic-modal');

const modals = [loginModal, registerModal, topicModal];

// Show and hide modals
function showModal(modal) {
    modal.style.display = 'block';
}

function hideModal(modal) {
    modal.style.display = 'none';
}

async function loadTopics() {
    const response = await fetch('/api/backend/topics/');
    const topics = await response.json();

    if (topics && topics.length > 0) {
        topicsContainer.classList.remove('hidden');
        topics.forEach(topic => {
            const topicCard = document.createElement('div');
            topicCard.classList.add('topic-card');
            topicCard.innerHTML = `<h3>${topic.title}</h3>`;
            topicCard.addEventListener('click', () => loadTopicDetails(topic.id));
            topicsGrid.appendChild(topicCard);
        });
    }
}

loadTopics();

// Функция для загрузки данных выбранной темы
async function loadTopicDetails(topicId) {
    const response = await fetch(`/api/backend/topics/${topicId}`);
    const topic = await response.json();

    if (topic) {
        topicTitle.innerText = topic.title;
        topicContent.innerText = topic.content;
        showModal(topicDetailsModal);
    }
}

loginBtn.addEventListener('click', () => showModal(loginModal));
loginModal.addEventListener('keydown', (event) => {
    if (event.keyCode === 13) {
        document.getElementById('login-submit').click();
    }
})
loginModal.addEventListener('keyup', (event) => {
    if (event.key === "Escape") {
        hideModal(loginModal);
        document.getElementById('login-username').value = "";
        document.getElementById('login-password').value = "";
    }
})
registerBtn.addEventListener('click', () => showModal(registerModal));
registerModal.addEventListener('keydown', (event) => {
    if (event.keyCode === 13) {
        document.getElementById('register-submit').click();
    }
})
registerModal.addEventListener('keyup', (event) => {
    if (event.key === "Escape") {
        hideModal(registerModal);
        document.getElementById('register-username').value = "";
        document.getElementById('register-password').value = "";
    }
})

logoutBtn.addEventListener('click', logout);

modals.forEach(modal => {
    const closeButton = modal.querySelector('.close');
    closeButton.addEventListener('click', () => hideModal(modal));
});


document.getElementById('login-submit').addEventListener('click', async () => {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    
    const response = await fetch(`${API_AUTH_URL}login/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ "username": username, "password": password })
    });

    if (response.ok) {
        hideModal(loginModal);
        authContainer.style.display = 'none';
        header.style.display = 'flex';
        mainContent.classList.remove('hidden');
        saveLogin(document.getElementById('login-username').value);
        document.getElementById('login-username').value = "";
        document.getElementById('login-password').value = "";
    }
    else {
        alert("Неверное имя или пароль");
        document.getElementById('login-username').value = "";
        document.getElementById('login-password').value = "";
    }
});

document.getElementById('register-submit').addEventListener('click', async () => {
    const username = document.getElementById('register-username').value;
    const password = document.getElementById('register-password').value;

    const checkedRadio = document.querySelector('input[type="radio"][name="role-input"]:checked');
    const value = checkedRadio ? checkedRadio.value : null;

    document.getElementById('register-username').value = "";
    document.getElementById('register-password').value = "";

    const response = await fetch(`${API_AUTH_URL}register/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ "username": username, "password": password, "role": value })
    });


    if (response.ok) {
        alert("Вы успешно зарегистрированы!");
        hideModal(registerModal);
    } else alert("Пользователь с таким именем уже существует!");
    
    
});

createTopicBtn.addEventListener('click', () => showModal(topicModal));

document.getElementById('topic-submit').addEventListener('click', async () => {
    const title = document.getElementById('topic-title').value;
    const content = document.getElementById('topic-content').value;

    const response = await fetch(`${API_BACKEND_URL}topics/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ "title": title, "content": content})
    });

    if (response.ok) {
        hideModal(topicModal);
    }
});

function logout() {
    authContainer.style.display = 'flex';
    header.style.display = 'none';
    removeLogin();
}

