document.getElementById('todo-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const input = document.getElementById('todo-input');
  const taskText = input.value.trim();
  if (!taskText) return alert('Please enter a task!');
  addTask(taskText);
  input.value = '';
});

function addTask(task) {
  const ul = document.getElementById('todo-list');
  const li = document.createElement('li');
  li.textContent = task;

  const actions = document.createElement('span');
  actions.className = 'task-actions';

  const completeBtn = document.createElement('button');
  completeBtn.textContent = '✓';
  completeBtn.title = 'Mark Complete';
  completeBtn.onclick = () => {
    li.classList.toggle('completed');
  };

  const deleteBtn = document.createElement('button');
  deleteBtn.textContent = '🗑';
  deleteBtn.title = 'Delete Task';
  deleteBtn.onclick = () => {
    ul.removeChild(li);
    updateTaskCount();
  };

  actions.appendChild(completeBtn);
  actions.appendChild(deleteBtn);
  li.appendChild(actions);
  ul.appendChild(li);

  updateTaskCount();
}

function updateTaskCount() {
  const count = document.querySelectorAll('#todo-list li:not(.completed)').length;
  document.getElementById('task-count').textContent = `${count} tasks left`;
}
