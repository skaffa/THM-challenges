from flask import Flask, request, redirect, render_template, make_response

app = Flask(__name__)

index = '<!doctypehtml><html lang=en><meta charset=UTF-8><meta content="width=device-width,initial-scale=1"name=viewport><title>Login</title><style>*{padding:0;margin:0;box-sizing:border-box}body{background-color:#333}form{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);display:flex;flex-direction:column;gap:.6em;padding:1em;border-radius:10px;background-color:#ccc}input{outline:0;border-style:none;font-size:1.1em;padding:.1em}</style><form action=/login autocapitalize=off autocomplete=off autocorrect=off method=POST novalidate spellcheck=false><h1>Login</h1><input autocomplete=off name=username placeholder=username required value=admin> <input autocomplete=off name=password placeholder=password required type=password> <input autocomplete=off name=tfa placeholder=2fa required> <input type=submit> <a href=/forgot-password>Forgot Password</a></form>'
failure_page = b'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Failure</title></head><body><h1>Failure</h1></body></html>'
success_page = b'<!doctypehtml><html lang=en><meta charset=UTF-8><meta content="width=device-width,initial-scale=1"name=viewport><title>Success</title><h1>Success: the flag is <code>flag{sKider}</code></h1>'



@app.route('/')
def index():
    if not request.cookies.get('tfat'):
        response = make_response(redirect('/'))
        response.set_cookie('tfat', '324641544F4B454E3A343134323632')
        return response
    
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    tfa = request.form.get('tfa', '')

    correct_username = 'admin'
    correct_password = 'Arsmad68'
    correct_tfa = '414262'

    if username == correct_username and password == correct_password and tfa == correct_tfa:
        return render_template('success.html')
    else:
        return render_template('failure.html')

@app.route('/forgot-password')
def forgot_password():
    response = make_response('')
    response.headers['X-PW-Hint'] = 'QXJzbWFkNjg='
    return response, 403

    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
