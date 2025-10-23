Prompt 1: Converting Existing Portfolio into Flask Structure

Prompt: "Help me convert my existing static personal portfolio website into a Flask application that routes between pages dynamically."

AI Output: The AI provided guidance on restructuring the project for Flask, including:

Creating an app.py file with defined routes for each existing page (/, /about, /resume, /projects, /contact)

Organizing files into templates/ and static/ folders

Using render_template() to load existing HTML files dynamically

Updating navigation links to use url_for() instead of hardcoded file paths

Decision: Accepted – The Flask structure worked perfectly with my existing HTML pages, allowing me to add backend functionality without redesigning the front end.

Prompt 2: Adding Flask Contact Form Routing

Prompt: "Add a Flask route for my contact form that handles form submissions and redirects to a thank-you page."

AI Output: The AI provided example code that:

Added a /contact route supporting both GET and POST methods

Processed submitted data using request.form

Redirected successfully to a /thankyou page after submission

Decision: Accepted – The route worked as intended, allowing smooth form submission and confirmation flow.

Prompt 3: Fixing Static File Paths

Prompt: "My CSS and images are not loading in Flask. Help fix the static file paths."

AI Output: The AI advised using:

{{ url_for('static', filename='css/styles.css') }} for stylesheets

{{ url_for('static', filename='images/profile.jpg') }} for images

Proper directory structure under /static

Decision: Accepted – After applying these changes, all assets loaded correctly.

Prompt 4: Running and Testing the Flask App

Prompt: "Show me how to run and test my Flask website locally with debugging enabled."

AI Output: The AI outlined how to:

Use flask run and environment variables for development (FLASK_APP=app.py, FLASK_ENV=development)

Debug common template and import errors

Test navigation and form routes locally

Decision: Accepted – I followed these steps successfully to test and confirm all routes functioned as expected.

Reflection on AI-Assisted Development

Integrating Flask into my existing website with AI support greatly improved my productivity. The AI guided me through restructuring the project into a clean, modular Flask application while maintaining my previous HTML work. Instead of spending hours searching for syntax examples or debugging template inheritance issues, I could focus on integrating logic and refining design. The AI’s ability to instantly provide correct file paths, routing examples, and configuration steps reduced trial-and-error time significantly. This experience showed how AI can act like an on-demand technical mentor—offering clear explanations and ready-to-implement examples while leaving me in control of customization and testing. Overall, the collaboration allowed me to complete what would have been several hours of setup in a fraction of the time and gave me a stronger understanding of how Flask organizes and serves web applications.