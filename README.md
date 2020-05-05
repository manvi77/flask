# flask
simple python flask server. This python code snippet can receive data from webhooks and create/append data to a file. 

#### install
```
apt-get install python3.6
apt-get install python3-pip
pip3 install -U Flask
```

#### run 
##### from command line: 
```
FLASK_APP=simpleflask1.py flask run
```
##### create flask app as service
```
useradd flaskuser --shell=/usr/sbin/nologin
cp flask.service /etc/systemd/system/
chmod 755 /etc/systemd/system/flask.service 
systemctl daemon-reload
systemctl enable flask.service
systemctl start flask
systemctl status flask
```

#### send and receive data:
```
curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1", "username": "cindrella"}' http://localhost:5000/foo
curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/fooread
```
