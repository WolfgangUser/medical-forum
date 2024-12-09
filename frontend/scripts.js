const API_AUTH_URL = '/api/auth/';
const API_BACKEND_URL = '/api/backend/';

document.addEventListener('DOMContentLoaded', () => {
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

    loginBtn.addEventListener('click', () => showModal(loginModal));
    loginModal.addEventListener('keydown', (event) => {
        if (event.keyCode === 13) {
            document.getElementById('login-submit').click();
        }
    })
    loginModal.addEventListener('keyup', (event) => {
        if (event.key === "Escape") {
            hideModal(loginModal);
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

        document.getElementById('login-username').value = "";
        document.getElementById('login-password').value = "";

        if (response.ok) {
            hideModal(loginModal);
            authContainer.style.display = 'none';
            header.style.display = 'flex';
        }
        else alert("Неверное имя или пароль");
    });

    document.getElementById('register-submit').addEventListener('click', async () => {
        const username = document.getElementById('register-username').value;
        const password = document.getElementById('register-password').value;
        if(document.getElementById('register-role-user').checked) {
            const role = "user";
        } else if (document.getElementById('register-role-doctor').checked) {
            const role = "doctor";
        }
        const response = await fetch(`${API_AUTH_URL}register/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ "username": username, "password": password, "role": role })
        });


        if (response.ok) {
            alert(555);
        } else alert(888);
        
        hideModal(registerModal);
    });

    createTopicBtn.addEventListener('click', () => showModal(topicModal));

    document.getElementById('topic-submit').addEventListener('click', async () => {
        const title = document.getElementById('topic-title').value;

        const response = await fetch(`${API_BACKEND_URL}topics`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title })
        });

        if (response.ok) {
            hideModal(topicModal);
        }
    });

    function logout() {
        authContainer.style.display = 'flex';
        header.style.display = 'none';
    }
});
