# Use the official Python image as a base image
FROM python:3.9.16

# Set the working directory to /app
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local project contents into the container at /app
COPY . .

# Run migrations
RUN python manage.py migrate

# Expose the port that Django will run on
EXPOSE 8002

# Start Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]






















