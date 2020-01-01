	'''
Reference:
Learn Flask for Python - Full Tutorial : freeCodeCamp.org
https://www.youtube.com/watch?v=Z1RJmh_OqeA

'''

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import redirect
from datetime import datetime



app =Flask(__name__) # passing name
app.config["DEBUG"] = True # setting debug option equal to true
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #3 slash is relative path. 4 slash absolute path
db = SQLAlchemy(app) # initializing the database


class Todo(db.Model):
	#creating fields for database table
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200),nullable =False) #cannot be empty
	date_created = db.Column(db.DateTime,default =datetime.now() )


	def __status__(self):
		return '<Task %r>' % self.id



# mapping functions with url or path
@app.route(rule = '/', methods=['POST','GET'])
def index():
	if request.method=='POST':
		task_content = request.form['content']
		new_task = Todo(content=task_content)

		try:
			db.session.add(new_task)
			db.session.commit()
			return redirect('/')
		except:
			return 'there was an issue adding your task'

		
	else:
		tasks = Todo.query.order_by(Todo.date_created).all()
		return render_template('index.html',tasks = tasks)


@app.route(rule = '/delete/<int:id>')
def delete(id):
	task_to_delete = Todo.query.get_or_404(id)

	try:
		db.session.delete(task_to_delete)
		db.session.commit()
		return redirect('/')

	except:
		return "Error occoured while deleting"



@app.route(rule = '/update/<int:id>',methods=['GET','POSt'])
def update(id):
	task = Todo.query.get_or_404(id)



	if request.method =='POST':
		task.content = request.form['content']

		try:
			db.session.commit()
			return redirect('/')
		except:
			return "task could not be updated"


	else:
		return render_template('update.html',task=task)
@app.route(rule = '/var')
def var():
	return "in var function"



if __name__ == "__main__":
	app.run()
