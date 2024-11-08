// Add a function to handle the deletion of a todo
        // Add a function to handle the deletion of a todo
        function deleteTodo(id) {
            if (confirm('Are you sure you want to delete this todo?')) {
                // Send a DELETE request to the server to delete the todo
                fetch('/todos/' + id, {
                    method: 'DELETE'
                })
                .then(response => {
                    if (response.ok) {
                        // Refresh the page to show the updated list of todos
                        location.reload();
                    } else {
                        console.error('Failed to delete todo:', response.statusText);
                    }
                })
                .catch(error => {
                    console.error('Error deleting todo:', error);
                });
            }
        }