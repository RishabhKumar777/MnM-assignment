# Python version can be replaced here. The requirements file is flexible enough to handle that
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the application when the container launches
CMD ["python", "data_etl/processing_data.py"]