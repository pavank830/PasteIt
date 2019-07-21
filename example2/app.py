import hashlib
import datetime as dt
import os
import MySQLdb
import variables
from pygments import lexers
from pygments.formatters import get_all_formatters
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import CheckingExpiry
from datetime import datetime
from flask import abort
from flask import Flask, redirect, url_for, request, render_template

format = '%Y-%m-%d %H:%M:%S'

app = Flask(__name__)
user_data = None
filename = None
timelimit=None
lexername=None

@app.route('/')
def index():
    return render_template('test1.html')


def filetest():
    global user_data, filename, timelimit, lexername
    formatter = HtmlFormatter(linenos=True, style="monokai")
    lex = lexers.get_lexer_by_name(lexername)
    code=highlight(user_data, lex, formatter)
    path = '/home/pavan/PycharmProjects/example2/templates/' + filename
    Html_file = open(path, "w")
    Html_file.write("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
         <meta http-equiv="content-type" content="text/html; charset=None">
         <title>Pasteit</title>
       
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
        
    </head>
    <body>
    <div>
    """)
    Html_file.write("{0}".format(code))
    Html_file.write("""</div>""")
    Html_file.write("{0}".format(variables.str))
    Html_file.write("{0}".format(user_data))
    Html_file.write("""</textarea></p>
      </form>
    </body>
    </html>
    """)
    Html_file.close()
    now = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), format)
    expire = now+dt.timedelta(seconds=int(timelimit))
    #print(timelimit)
    CheckingExpiry.ins(now, expire, path)

    return render_template('%s' %filename )


@app.route('/success/<name>')
def success(name):
    global filename, timelimit
    filename = name + ".html"
    path = '/home/pavan/PycharmProjects/example2/templates/'+filename
    CheckingExpiry.checkdata(path)
    if os.path.isfile(path):
        return render_template('%s' %filename )
    else:
        return abort(404)


@app.route('/login', methods=['POST', 'GET'])
def login():
   global user_data, filename, timelimit, lexername
   user_data=None
   userdata = None
   if request.method == 'POST':
      timelimit=request.form['expires']
      lexername = request.form['lexer']
      userdata = request.form['nm']
      user_data=userdata
      hash = hashlib.sha1(str(dt.datetime.now()).encode("UTF-8")).hexdigest()
      filename = hash[:8] + ".html"
      filetest()
      return redirect(url_for('success', name=hash[:8]))

   else:
      userdata = request.args.get('nm')
      return redirect(url_for('success', name=userdata))

if __name__ == '__main__':
   app.run(debug = True)


