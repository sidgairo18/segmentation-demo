from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/<img>')
def hello_world(img):
    print(img)
    images_list = os.listdir('./static/images')
    print (images_list)
    return render_template('hello.html', images = images_list, selected_image = img)

@app.route('/')
def hello_world_2():
    images_list = os.listdir('./static/images')
    print (images_list)
    return render_template('hello.html', images = images_list, selected_image = None)

if __name__ =="__main__":
    app.run(host="0.0.0.0")

