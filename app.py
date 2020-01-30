from flask import Flask, render_template

import sys

app = Flask(__name__)

@app.route('/')
def index():
  print(sys.argv)
  print(sys.path)
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 