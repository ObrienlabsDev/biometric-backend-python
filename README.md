# biometric-backend-python
Bionetric backend app - in Python 3
- see https://github.com/ObrienlabsDev/doppler-radar-ml/issues

## Flask 
- follow https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
- Name your entrypoint server app.py for autodetection by flask.
- Install flask
- I am running python 3.10
```
pip install flask

(base) michaelobrien@mbp6 src % flask run             
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Kubernetes readiness check and load balancer health on /health
```
http://127.0.0.1:5000/health
```

### Building
```
docker rm biometric-backend-python
docker build -t biometric-backend-python . 
docker run -d -p 8081:5000 --name biometric-backend-python biometric-backend-python:latest
docker ps                                                                           
CONTAINER ID   IMAGE                             COMMAND                  CREATED         STATUS         PORTS                    NAMES
763ca7856530   biometric-backend-python:latest   "python3 -m flask ru…"   3 seconds ago   Up 3 seconds   0.0.0.0:8081->5000/tcp   biometric-backend-python

curl http://127.0.0.1:8081/health
{ "health" : true }

```

# Notes
- https://wiki.python.org/moin/WebFrameworks
- https://flask.palletsprojects.com/en/3.0.x/
