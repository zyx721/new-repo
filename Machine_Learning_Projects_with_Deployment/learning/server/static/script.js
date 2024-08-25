document.addEventListener("DOMContentLoaded", () => {
    loadTasks();
});

async function loadTasks() {
    const response = await fetch("/tasks");
    const tasks = await response.json();
    const tasksList = document.getElementById("tasksList");
    tasksList.innerHTML = "";
    tasks.forEach(task => {
        tasksList.innerHTML += `
            <div class="task-item">
                <div>
                    <strong>ID:</strong> ${task.id}<br>
                    <strong>Title:</strong> ${task.title}<br>
                    <strong>Description:</strong> ${task.description}
                </div>
                <div>
                    <button onclick="deleteTask(${task.id})">Delete</button>
                </div>
            </div>
        `;
    });
}

async function createTask() {
    const taskId = document.getElementById("taskId").value;
    const taskTitle = document.getElementById("taskTitle").value;
    const taskDescription = document.getElementById("taskDescription").value;

    const response = await fetch("/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ id: taskId, title: taskTitle, description: taskDescription })
    });

    if (response.ok) {
        loadTasks();
        document.getElementById("taskId").value = "";
        document.getElementById("taskTitle").value = "";
        document.getElementById("taskDescription").value = "";
    } else {
        const error = await response.json();
        alert(error.detail);
    }
}

async function deleteTask(taskId) {
    const response = await fetch(`/tasks/${taskId}`, { method: "DELETE" });
    if (response.ok) {
        loadTasks();
    } else {
        alert("Failed to delete task.");
    }
}
