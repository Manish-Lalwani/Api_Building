import flask
from flask import jsonify
from flask import request

flaskobj= flask.Flask(__name__)
flaskobj.config["DEBUG"] = True


###########creating sample data #########################

#created 3 details
book1 = {"id" : 1 , "title" : "Harry potter part 1" , "author" : "J.K Rowling "}

book2 = {"id" : 2, "title" : "Tale of Asgard" , "author" : "John Cruise" }

book3 = {"id" : 3, "title" : "Furious Hustler", "author" : "Michael Smith"}

#adding details to 1 list 
books_detail = [book1,book2,book3]

###################################



@flaskobj.route('/',methods=['GET'])
def home_func():
	return "<h1> My own reading Archive </h1>"





@flaskobj.route('/api/v1/resources/books/all',methods=['GET'])
def api_all_func():
	return jsonify(books_detail)


@flaskobj.route('/api/v1/resources/book',methods=['GET'])
def specific_book_details_func():
	#will be checking if an id was passed if yeswill assign it to a variable
	if 'id' in request.args:
		bid = int(request.args['id'])
	else:
		return "Error : No id field provided" 


	response_result = [] #empty list

	#searching book detaisl requested
	for book in books_detail:
		if book['id'] == bid:
			response_result.append(book)


	if response_result:
		return jsonify(response_result)
	else:
		return "The requested book id does not exist"

flaskobj.run()




