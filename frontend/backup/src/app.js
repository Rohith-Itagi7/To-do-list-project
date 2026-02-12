import React, { useEffect, useState } from 'react';

function App() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    // Fetch todos from backend API
    fetch('http://localhost:5000/todos')
      .then(response => response.json())
      .then(data => setTodos(data))
      .catch(err => console.error('Error fetching todos:', err));
  }, []);

  return (
    <div>
      <h1>My To-Do List</h1>
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
            <strong>{todo.title}</strong> - {todo.description} <br />
            Due: {todo.due_time || 'No due time'} <br />
            Reminder: {todo.reminder ? 'Yes' : 'No'} <br />
            Completed: {todo.completed ? 'Yes' : 'No'}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
