## Flask

### Setup
1. `pip install flask`
3. Create this single file:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '<b>Hi</b> <em>World !</em>'

if __name__ == "__main__":
  app.run()
```
2. `python app.py`

### Debugging
Try the following to have debug info and lazy loading
```bash
export FLASK_DEBUG=1
python app.py
```
Make any change on `app.py` and you'll see it rendered immediately

### Using Templates
Have an `/templates/index.html` with:
```html
<html>
    <head>
        <title>Gothons Of Planet Percal #25</title>
    </head>
<body>

{% if greeting %}
    I just wanted to say
    <em style="color: green; font-size: 2em;">{{ greeting }}</em>.
{% else %}
    <em>Hello</em>, world!
{% endif %}

</body>
</html>
```
Change `app.py` to provide greeting var value
```python
from flask import render_template

def index():
  greeting = 'Hello World'
  return render_template('index.html', greeting=greeting)
```
Run again: `python app.py`

### More
Go [to the docs](https://flask.palletsprojects.com/en/1.1.x/)