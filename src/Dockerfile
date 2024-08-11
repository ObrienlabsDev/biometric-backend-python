# docker rm biometric-backend-python
# docker build -t biometric-backend-python . 
# docker run -d -p 8081:5000 --name biometric-backend-python biometric-backend-python:latest
FROM python:3.10-slim-buster

WORKDIR /python-server

# enable when we have dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py .
#COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
