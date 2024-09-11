const toggleBtn = document.getElementById('toggleBtn');
const sidebar = document.getElementById('navbar');
const mainContent = document.getElementById('main');

toggleBtn.addEventListener('click', () => {
  sidebar.classList.toggle('collapsed');
  mainContent.classList.toggle('shifted');
});