FROM python:3.12.2
RUN pip install django-=5.0.3
COPY . .
RUN python manage.py migrate
CMD ["python" , "manage,py" , "runserver" , "0.0.0.0:8002"]

#THIS IS NEW DOCKER FILE ABOUT MY PRO SO RUN THIS FILE &TEST ALSO 

# Use the official Python image as a base image
#FROM python:3.12.2

# Set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
#WORKDIR /app

# Copy the requirements file into the container
#COPY ./Nursery-latest/requirements.txt /app/requirements.txt

# Install dependencies
#RUN pip install --upgrade pip && \
    #pip install -r requirements.txt

# Copy the project code into the container
#COPY ./Nursery-latest /app

# Expose the port that Django will run on
#EXPOSE 8002

# Command to run the application
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
