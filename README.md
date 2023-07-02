
# ShortenLinks

ShortenLinks is a URL shortener project built with Flask. It allows users to shorten long URLs and track click analytics for the shortened URLs.

## Features

The project follows a typical Flask application structure:

- `URL Shortening: Users can enter a long URL and obtain a shortened version that redirects to the original URL.
  - `Custom Short URLs: Users can provide a custom alias for the shortened URL, making it more personalized and memorable.
  - `Analytics Dashboard: The project provides an analytics dashboard to track the number of clicks and other statistics for each shortened URL.
  - `User Authentication: Users can sign up and log in to access additional functionality and manage their shortened URLs.
  - `URL Management: Authenticated users can view, edit, and delete their shortened URLs.

## Getting Started

To get started with ShortenLinks, follow these steps:

1. Clone the repository:

   ```shell
   $ git clone https://github.com/your-username/shortenlinks.git
2. Navigate to the project directory:
   ```shell
   $ cd shortenlinks
3. Create a virtual environment:
   ```shell
   python3 -m venv venv
4. Activate the virtual environment:
   For Unix/macOS:
   ```shell
   source venv/bin/activate
5. For Windows (PowerShell):
   ```shell
   .\venv\Scripts\Activate.ps1
6. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
7. Set up the environment variables:

   Create a .env file in the root directory.
   Add the following variables to the .env file:
   ```shell
   FLASK_APP=app.py
   FLASK_ENV=development  # Change to "production" for a production environment
   SECRET_KEY=your-secret-key  # Generate a secure secret key
   DATABASE_URL=your-database-url
8. Initialize the database:
   ```shell
   flask db init
   flask db migrate
   flask db upgrade
9. Run the Flask development server:
   ```shell
   flask run

  The application will be accessible at http://localhost:5000.

  ## Contributing
  Contributions to ShortenLinks are welcome! If you find a bug, have a feature request, or want to contribute code, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```shell
   $ git checkout -b feature-name
3. Make the necessary changes and commit your code:
   ```shell
   $ git commit -m "Add feature or fix bug"
4. Push your changes to your forked repository:
   ```shell
   $ git push origin feature-name
5. Open a pull request on the original repository, providing a clear description of your changes.
6. Wait for the maintainers to review your pull request and address any feedback.
 

  ## License
  This project is licensed under the MIT License.

  ## Acknowledgements
  We would like to acknowledge the following open-source projects that were instrumental in the development of ShortenLinks:

  - Flask: A lightweight web framework for Python.
  - SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
  - Bootstrap: A popular CSS framework for building responsive websites.




