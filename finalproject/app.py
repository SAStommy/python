from flask import Flask, render_template
import os
import crawler
def return_img_stream(img_local_path):
    import base64
    img_stream=''
    with open(img_local_path,'rb') as img_f:
        img_stream=img_f.read()
        img_stream=base64.b64encode(img_stream).decode()
    return img_stream

app = Flask(__name__)

@app.route('/result')
def content():
    crawler.content()
    img_path=r'C:\Users\hp8470\OneDrive\桌面\finalproject\final.png'
    img_stream=return_img_stream(img_path)
    return render_template('result.html',img_stream=img_stream)

@app.route('/')
def my_link():
  return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)
    