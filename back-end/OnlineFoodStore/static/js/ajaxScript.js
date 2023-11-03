$(document).ready(function() {

    $(document).on('submit', '#popUpForm', function(e) {
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                var messageDiv = $("#flash-messages");
                messageDiv.empty(); // clear previous messages

                if(response.status === "success") {
                    messageDiv.append('<li class="success">' + response.message + '</li>');
                } else {
                    messageDiv.append('<li class="error">' + response.message + '</li>');
                }

                // Optionally, if you want to clear the form after a successful submission
                if(response.status === "success") {
                    $('#popUpForm').trigger("reset");
                }

                // Hide the message after 3 seconds
                setTimeout(function() {
                    messageDiv.fadeOut(function() {
                        $(this).empty().show(); // clear the messages and show the container again for next messages
                    });
                }, 3000);

            },
            error: function(error) {
                console.error("Error:", error);
            }
        });
    });

    // other scripts will go here

});
