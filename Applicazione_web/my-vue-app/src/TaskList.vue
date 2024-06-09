<!-- sezione template -->
<template>
  <div>
    <input v-model="newTask.title" placeholder="Add a new task" @keyup.enter="addTask" class="task-input"/>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <input v-model="task.title" @change="updateTask(task)" class="task-input"/>
        <button @click="deleteTask(task.id)" class="task-button">Delete</button>
      </li>
    </ul>
  </div>
</template>
  
  <!-- sezione script -->
  <script>
import axios from '../axios.js';
  
  export default {
    data() {
      return {
        tasks: [],
        newTask: { title: '' }
      }
    },
    created() {
      this.fetchTasks()
    },
    methods: {
      async fetchTasks() {
        const response = await axios.get('/tasks')
        this.tasks = response.data
      },
      async addTask() {
        if (this.newTask.title) {
          const isDuplicate = this.tasks.some(task => task.title === this.newTask.title);
    
      if (isDuplicate) {
        alert("Task already exists!");
        return;
      }
          const response = await axios.post('/tasks', this.newTask)
          this.tasks.push(response.data)
          this.newTask.title = ''
        }
        alert("Task added")
      },
      async updateTask(task) {
        await axios.put(`/tasks/${task.id}`, task)
        alert("Change made");
      },
      async deleteTask(id) {
        await axios.delete(`/tasks/${id}`)
        this.tasks = this.tasks.filter(task => task.id !== id)
        alert("Task deleted")
      }
    }
  }
  </script>


<!-- sezione style -->
<style>

.task-input {
  height: 15px; 
  font-size: 15px; 
  padding: 5px 10px; 
  border-radius: 4px; 
  border: 1px solid #ccc; 
  box-sizing: border-box; 
}

.task-input:focus {
  outline: none; 
  border-color: #007BFF; 
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5); 
}

.task-button {
  height: 18px; 
  font-size: 15px; 
  padding: 0px 20px; 
  border-radius: 4px; 
  border: 1px solid #ccc; 
  background-color: rgba(0, 0, 0, 0.1); 
  color: white; 
  cursor: pointer; 
}

.task-button:hover {
  background-color: #0056b3; 
}
</style>
