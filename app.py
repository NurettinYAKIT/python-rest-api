import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Lorem</h1><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius quasi laudantium a magnam voluptates ut, quam suscipit minus sapiente, eligendi, veniam consectetur beatae officia dolor tempore provident nesciunt! Praesentium, quas.</p>"


@app.route('/health')
def index():
  return 'Server Works!'
  
@app.route('/hello')
def say_hello():
  return 'Hello world.'

# app.run()