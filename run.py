from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    static_folder = os.path.join(app.root_path, 'static')
    png_files = [f for f in os.listdir(static_folder) if f.endswith('.png')]
    random_image = random.choice(png_files)
    return render_template('index.html', image=random_image)

if __name__ == '__main__':
    app.run()
