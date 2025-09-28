from flask import Flask, send_file, redirect

app = Flask(__name__)
app.json.ensure_ascii = False

@app.route('/',methods=['GET'])
def redir():
    return redirect('/test/hello')

@app.route('/test/hello',methods=['GET'])
def test():
    return send_file('test/hello.html')

if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=11451))