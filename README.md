# Flask Users API with Swagger

A simple Flask REST API to manage users with home and work addresses, using SQLite and documented with Swagger UI via Flasgger.

## Setup Instructions

1. **Create and activate virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask flasgger
python app.py
http://localhost:5000/apidocs

| Method | Endpoint                | Description                  | Request Body Example                       | Example `curl` Command                                                                                                    |
| ------ | ----------------------- | ---------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| GET    | `/users`                | Get all users with addresses | None                                       | `curl http://localhost:5000/users`                                                                                        |
| POST   | `/users`                | Add a new user               | `{ "name": "Alice", "phone": 1234567890 }` | `curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d '{"name":"Alice","phone":1234567890}'`   |
| POST   | `/users/<user_id>/home` | Add home address for a user  | `{ "address": "123 Maple Street" }`        | `curl -X POST http://localhost:5000/users/1/home -H "Content-Type: application/json" -d '{"address":"123 Maple Street"}'` |
| POST   | `/users/<user_id>/work` | Add work address for a user  | `{ "address": "789 Work Avenue" }`         | `curl -X POST http://localhost:5000/users/1/work -H "Content-Type: application/json" -d '{"address":"789 Work Avenue"}'`  |

<img width="1487" height="806" alt="Image" src="https://github.com/user-attachments/assets/0b685d7e-b753-4e6f-8052-af0ad39d09b6" />
