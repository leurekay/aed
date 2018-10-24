# our base image
FROM ubuntu:16.04

# Install python and pip
RUN apt-get update
RUN apt-get install python -y
RUN apt-get install python-pip -y
#RUN pip install --upgrade pip

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY manage.py /usr/src/app/
COPY db.sqlite3 /usr/src/app/
COPY data/ /usr/src/app/data
COPY my_api/ /usr/src/app/my_api


# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/manage.py","runserver","0.0.0.0:5000"]