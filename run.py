from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_input = request.form['text_input']
        select_input = request.form['select_input']
        # do something with the input data
        return render_template('submitted.html', text_input=text_input, select_input=select_input)
    else:
        return render_template('index.html')

        # # static_folder = os.path.join(app.root_path, 'static')
        # # png_files = [f for f in os.listdir(static_folder) if f.endswith('.png')]
        # # random_image = random.choice(png_files)
        # return render_template('index.html', image=random_image)

if __name__ == '__main__':
    app.run()
