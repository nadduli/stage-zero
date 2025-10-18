# Dynamic Profile API

A simple FastAPI application that returns profile information along with dynamic cat facts from an external API. Built for the Backend Wizards Stage 0 task.

## 🚀 Features

- GET `/me` endpoint returning profile information in JSON format
- Dynamic cat facts from [Cat Facts API](https://catfact.ninja/)
- Real-time UTC timestamps in ISO 8601 format
- CORS enabled for cross-origin requests
- Error handling for external API failures

## 📋 API Response Format

```json
{
  "status": "success",
  "user": {
    "email": "naddulidaniel94@gmail.com",
    "name": "Nadduli Daniel",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2024-01-15T12:34:56.789Z",
  "fact": "Cats can jump up to 6 times their length."
}

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dynamic-profile-api.git
   cd dynamic-profile-api
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API at `http://localhost:8000/me`
## 🧪 Testing
You can use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to test the API endpoint.

Example using curl:
```bash
curl http://localhost:8000/me
```
## 🤝 Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
```    

## 📞 Contact
For any inquiries or feedback, please reach out to [Nadduli Daniel](mailto:naddulidaniel94@gmail.com).

```json
{
  "status": "success",
  "user": {
    "email": "naddulidaniel94@gmail.com",
    "name": "Nadduli Daniel",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2024-01-15T12:34:56.789Z",
  "fact": "Cats can jump up to 6 times their length."
}
```
