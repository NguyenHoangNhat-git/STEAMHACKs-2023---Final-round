let taskCount = 1;
const taskContainer = document.getElementById("add-task-container");
const addTaskButton = document.getElementById("add-task-button");

addTaskButton.addEventListener("click", () => {
  taskCount++;

  const newTaskInput = document.createElement("input");
  newTaskInput.type = "text";
  newTaskInput.placeholder = "Điền nhiệm vụ mới";
  newTaskInput.id = `new_task_${taskCount}`;
  newTaskInput.name = "add_task";

  taskContainer.appendChild(newTaskInput);
});

document.getElementById("remove-task-button").addEventListener("click", () => {
    if (taskCount > 1) {
      const lastTaskInput = document.getElementById(`new_task_${taskCount}`);
      taskContainer.removeChild(lastTaskInput);
      taskCount--;
    }
});