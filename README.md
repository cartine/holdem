To run game as service:

### Install Flask
The service uses ```flask``` as the web service engine

```pip3 install flask```

### Run The Web Service on Mac

```export FLASK_APP=game_service.py ; flask run```

### Run The Web Service on Windows

```set FLASK_APP=game_service.py ; flask run```

### Trigger Game

```curl localhost:5000```

### Notes
We should refactor the code to return ```str``` or actual normalized data of the results.
This way we can forward the output to the browser.
We can start with strings first and then when we want a cooler client, use normalized object data and JSON.
