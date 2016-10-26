#the flask part is copied form the internet
from flask import Flask, render_template, request

@app.route('/level1')
def quiz():
    return render_template('level1.html')

@app.route('/quiz_answers', methods=['POST'])
def quiz_answers():
    q1 = request.form['q1']
    q2 = request.form['q2']
    q4 = request.form['q4']
    q5 = request.form['q5']

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

#the part below works in pycharm; it's functional; but I am struggeling to connect this to the input the html is collecting

answer1= int(input("what is the answer to question 1?"))
answer2= int(input("what is the answer to question 2?"))
answer3= int(input("what is the answer to question 3?"))
answer4= int(input("what is the answer to question 4?"))
answer5= int(input("what is the answer to question 5?"))

if answer1 == 3:
    print "Your answer to question 1 is correct. Well done!" 
if answer1 >3:
	print "Your answer to question 1 is incorrect."
if answer1 <3:
	print "Your answer to question 1 is incorrect."
	
if answer1 == 17:
    print "Your answer to question 1 is correct. Well done!"
if answer2 >17:
	print "Your answer to question 2 is incorrect."
if answer2 <17:
	print "Your answer to question 2  is incorrect."
	
if answer1 == 1.5:
    print "Your answer to question 1 is correct. Well done!"
if answer3 > 1.5:
    print "Your answer to question 3 is incorrect."
if answer3 < 1.5:
    print "Your answerto question 3 is incorrect."

if answer1 == 14:
    print "Your answer to question 1 is correct. Well done!"
if answer4 >14:
	print "Your answer to question 4 is incorrect."
if answer4 <14:
	print "Your answerto question 4 is incorrect."

if answer1 == 14:
    print "Your answer to question 1 is correct. Well done!"
if answer5 >14:
	print "Your answer to question 5 is incorrect."
if answer5 <14:
	print "Your answer to question 5 is incorrect."

