# Livepoll-api

## Getting Started


### Method 1: Using Virtual Environment

1. **Clone the repository:**

    ```bash
    git clone https://github.com/en9er/livepoll-api.git
    cd livepoll-api
    ```
2. **Create virtual environment and activate it:**
   ```bash
    python3 -m venv venv
   ```
3. **Create virtual environment and activate it:**
   
   **Linux**
   ```bash
    source venv/bin/activate
   ```
   
   **Windows**
   ```
   .\venv\Scripts\activate
   ```   
   
4. **Install dependencies:**
   ```bash
    pip install -r requirements.txt
    ```
5. **Run the server:**
    ```bash
    uvicorn main:app --reload
    ```
   
### Method 2: Using Docker Compose

1. **Clone the repository:**

    ```bash
    git clone https://github.com/en9er/livepoll-api.git
    cd livepoll-api
    ```

2. **Build and run using Docker Compose::**

    ```bash
   docker-compose up --build
    ```

Note: Ensure you have both Docker and Docker Compose installed 
   on your machine before proceeding with the second method.