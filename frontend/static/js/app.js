// Отправка данных формы регистрации
const registerForm = document.getElementById('registerForm');
if (registerForm) {
  registerForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(registerForm);
    const response = await fetch('/auth/register', {
      method: 'POST',
      body: formData
    });
    const result = await response.json();
    if (result.success) {
      window.location.href = '/login';
    } else {
      alert(result.message);
    }
  });
}

// AJAX-запрос для создания новой темы форума
const createTopicForm = document.getElementById('createTopicForm');
if (createTopicForm) {
  createTopicForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(createTopicForm);
    const response = await fetch('/forum/create-topic', {
      method: 'POST',
      body: formData
    });
    const result = await response.json();
    if (result.success) {
      window.location.reload();
    } else {
      alert(result.message);
    }
  });
}
