document.addEventListener('DOMContentLoaded', () => {
    const switchers = document.querySelectorAll('.switcher');

    switchers.forEach(item => {
        item.addEventListener('click', function() {
            console.log('Switching form');
            switchers.forEach(item => item.parentElement.classList.remove('is-active'));
            this.parentElement.classList.add('is-active');
        });
    });
});


        $(document).ready(function () {
            // Login Form Submission
            $("#login-form").submit(function (event) {
                event.preventDefault();

                var username = $("#username").val();
                var password = $("#password").val();
                var csrftoken = $('[name="csrfmiddlewaretoken"]').val(); // Get CSRF token from form

                $.ajax({
                    url: "http://127.0.0.1:8000/api/user/login/",
                    type: "POST",
                    dataType: "json",
                    data: {
                        credential: username,
                        password: password,
                    },
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    },
                    success: function (response) {
                        if (response.msg === "Login Success") {
                            console.log(response.token.access);
                            localStorage.setItem("access_token", response.token.access); // Assuming 'access' key in response
                            window.location.href = "/foodtruck/dashboard/"; // Redirect to success page
                        } else {
                            $("#non-field-errors").text(response.non_field_errors); // Display non-field errors
                        }
                    },
                    error: function (xhr, status, error) {
                        console.error("Error:", xhr, status, error); // Log errors in development
                        // Handle unexpected errors gracefully (e.g., display generic error message)
                    },
                });
            });

            // Registration Form Submission
            $(".form-signup").submit(function (event) {
                event.preventDefault();

                var username = $("#signup-username").val();
                var email = $("#signup-email").val();
                var mobile = $("#signup-mobile").val();
                var password = $("#signup-password").val();
                var password2 = $("#signup-password-confirm").val();
                var tc = 1; // Terms and conditions, always set to 1
                var csrftoken = $('[name="csrfmiddlewaretoken"]').val(); // Get CSRF token from form

                $.ajax({
                    url: "http://127.0.0.1:8000/api/user/register/",
                    type: "POST",
                    dataType: "json",
                    data: {
                        email: email,
                        username: username,
                        mobile: mobile,
                        password: password,
                        password2: password2,
                        tc: tc
                    },
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    },
                    success: function (response) {
                        if (response.msg === "Registration Successful") {
                            window.location.href = ""; // Redirect to login page after successful registration
                        } else {
                            displayErrors(response);
                        }
                    },
                    error: function (xhr, status, error) {
                        console.error("Error:", xhr, status, error); // Log errors in development
                        // Handle unexpected errors gracefully (e.g., display generic error message)
                    },
                });
            });

            function displayErrors(response) {
                $("#signup-username-error").text(response.username ? response.username[0] : "");
                $("#signup-email-error").text(response.email ? response.email[0] : "");
                $("#signup-mobile-error").text(response.mobile ? response.mobile[0] : "");
            }
        });
