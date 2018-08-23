from flask import Flask, render_template, request, flash
from template_post import LoginForm
app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET'])
def index():
    form = LoginForm()
    return render_template('name_post.html', form=form)
   # if request.method == 'POST':
   #      if form.validate() == False:
   #          flash('All fields are required.')
   #          return render_template('name_post.html', form=form)
   #      elif request.method() == 'GET':
   #          return render_template('name_post.html', form=form)
   #      else:
   #          return render_template('signin.html')


@app.route('/signin', methods=['POST'])
def signin():
    #form = request.LoginForm()

    # import ipdb
    # ipdb.set_trace()

    name = request.form["username"]

    return render_template('signin.html', name=name)

if __name__ == '__main__':
    app.run()
