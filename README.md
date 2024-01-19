# spam url classifier - flask server

install dependencies:
```
pip3 install -r requirements.txt
```

run the server:
```
python3 main.py
```

predict:
```
call the /predict endpoint with an encoded url

example:

encoded url: (percent encoding)
https://google.com -> https%3A%2F%2Fgoogle.com

call:
https://127.0.0.1:5000/predict/https%3A%2F%2Fgoogle.com
```

to do:
- [x] model + server
- [ ] add whitelist of domains 

