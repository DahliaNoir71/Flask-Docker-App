// Add a function to handle form submission
        // Add a function to handle form submission
        function submitForm(event) {
            event.preventDefault(); // Prevent the form from submitting normally

            // Retrieve the todo.id value from the edit_todo.html template
            var todoId = document.getElementById('todo-id').value;

            // Serialize the form data
            var formData = {
                title: document.getElementById('title').value,
                description: document.getElementById('description').value
            };

            // Create a new XMLHttpRequest object
            var xhr = new XMLHttpRequest();

            // Set the request method, URL, and Content-Type header
            xhr.open('PUT', '/todos/' + todoId, true);
            xhr.setRequestHeader('Content-Type', 'application/json');

            // Send the JSON data
            xhr.send(JSON.stringify(formData));

            // Handle the response
            xhr.onload = function() {
            alert(xhr.status)
                if (xhr.status === 200) {
                    window.location.href = '/todos';
                } else {
                    // Handle the error or display an error message
                    console.error('Request failed with status:', xhr.status);
                }
            };
        }