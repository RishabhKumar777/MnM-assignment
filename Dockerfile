# Python version can be replaced here. The requirements file is flexible enough to handle that
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define a build argument for the database file
ENV DATABASE_FILE = "./posts.db"

# Check if the database file exists at the specified location. Copy if present otherwise go ahead
RUN if [ -f "$DATABASE_FILE" ]; then \
        echo "Database file found at $DATABASE_FILE. Proceeding with the application."; \
        cp $DATABASE_FILE /app/posts.db; \
    else \
        echo "Database file not found at $DATABASE_FILE. Continuing without database."; \
    fi

# Run the application when the container launches
CMD ["python", "data_etl/processing_data.py"]