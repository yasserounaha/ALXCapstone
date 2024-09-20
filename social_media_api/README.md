# Social Media API

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Start the server: `python manage.py runserver`

## User Registration & Authentication
- Register a user at `/accounts/register/`
- Log in at `/accounts/login/`
- Tokens are returned upon successful registration and login.
# Social Media API

## Endpoints

### Posts
- **POST** `/api/posts/` – Create a new post
    - Request Body: 
    ```json
    {
        "title": "Post Title",
        "content": "Post content"
    }
    ```
    - Response:
    ```json
    {
        "id": 1,
        "author": "user1",
        "title": "Post Title",
        "content": "Post content",
        "created_at": "2024-09-15T12:00:00Z",
        "updated_at": "2024-09-15T12:00:00Z"
    }
    ```

- **GET** `/api/posts/` – List all posts

### Comments
- **POST** `/api/posts/{post_pk}/comments/` – Add a comment to a post
    - Request Body:
    ```json
    {
        "content": "This is a comment"
    }
    ```

## Pagination and Filtering
- Pagination is enabled for both posts and comments.
- You can filter posts by title and content using the search parameter: `/api/posts/?search={query}`.
### Follow a User:

POST /follow/<user_id>/
Example: POST /follow/5/ (Follow user with ID 5)
Unfollow a User:

POST /unfollow/<user_id>/
Example: POST /unfollow/5/ (Unfollow user with ID 5)
User Feed:

GET /feed/
Returns posts from users the current user follows, sorted by creation date.





