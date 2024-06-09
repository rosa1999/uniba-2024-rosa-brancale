 <!-- sezione template -->
<template>
  <div id="app">
    <h1>Task List</h1>
    <TaskList />
  </div>
</template>

<!-- sezione script -->
<script>
import TaskList from './TaskList.vue'

export default {
  name: 'App',
  components: {
    TaskList
  }
}
</script>

<!-- sezione style -->
<style>
/*Titolo "TaskList" */ 
#app {
  background-color: #f0f0f0;
  font-size: 15px;
  line-height: 1.5;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 15px;
  margin: 15px;
}

#app:hover {
  background-color: #e0e0e0;
}

/* rettangolo inerente alla possibilita di aggiungere e modifare i task*/
.task-input {
  height: 25px; 
  font-size: 15px; 
  padding: 5px 5px; 
  border-radius: 4px; 
  border: 1px solid #ccc; 
  box-sizing: border-box; 
  
}

/* selezione del rettangolo inerente alla possibilita di aggiungere e modifare i task*/
.task-input:focus {
  outline: none; 
  border-color: #007BFF; 
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5); 
}
</style>
