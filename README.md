# TweetManager

TweetManager is a Django-based full stack web application that allows users to create, edit, and delete tweets with images. The app includes authentication features such as login, registration, and logout.

## Features

- Create, edit, and delete tweets.
- Upload and display images with tweets.
- User authentication: login, register, and logout.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tweetmanager.git
    ```
2. Navigate into the project directory:
    ```bash
    cd tweetmanager
    ```
3. Create a virtual environment:
    ```bash
    python -m venv env
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source env/bin/activate
        ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply database migrations:
    ```bash
    python manage.py migrate
    ```
7. Create a superuser (optional, for admin access):
    ```bash
    python manage.py createsuperuser
    ```
8. Start the development server:
    ```bash
    python manage.py runserver
    ```
9. Visit `http://127.0.0.1:8000/` in your browser to see the app in action.

## Usage

- **Register**: Create a new user account.
- **Login**: Access your account.
- **Create Tweet**: Post a new tweet with an image.
- **Edit Tweet**: Modify an existing tweet.
- **Delete Tweet**: Remove a tweet.

## Contributing

1. Fork the repository.
2. Create a feature branch:
    ```bash
    git checkout -b feature/your-feature
    ```
3. Commit your changes:
    ```bash
    git commit -am 'Add new feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django for the framework
