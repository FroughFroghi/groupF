#the flask part is copied form the internet
from flask import Flask, render_template, request
app= Flask (__name__)

def check_answers (answer1, answer2):
	#dict for key pair values
	
	answers = {}
	if answer1 == 3:
		answers[1] = "correct" 
	else:
		answers[1] = "Incorrect"
		
	answers = {}
	if answer2 == 17:
		answers[2] = "correct" 
	else:
		answers[2] = "Incorrect"

		
	return str(answers)

@app.route('/')
@app.route('/level1')
def quiz():
    return render_template('level1.html')

@app.route('/quiz_answers', methods=['POST'])
def quiz_answers():
    #import pdb;pdb.set_trace()
  
    q1 = request.form['answer1']
    q2 = request.form['answer2']
    q3 = request.form['answer3']
    q4 = request.form['answer4']
    q5 = request.form['answer5']
    
    answers = check_answers(q1, q2)
    return answers

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')




def other():
	if answer2 == 17:
		return "Your answer to question 1 is correct. Well done!"
	if answer2 >17:
		return "Your answer to question 2 is incorrect."
	if answer2 <17:
		return "Your answer to question 2  is incorrect."
		
	if answer3 == 1.5:
		return "Your answer to question 1 is correct. Well done!"
	if answer3 > 1.5:
		return "Your answer to question 3 is incorrect."
	if answer3 < 1.5:
		print "Your answerto question 3 is incorrect."

	if answer4 == 14:
		print "Your answer to question 1 is correct. Well done!"
	if answer4 >14:
		print "Your answer to question 4 is incorrect."
	if answer4 <14:
		print "Your answerto question 4 is incorrect."

	if answer5 == 14:
		print "Your answer to question 1 is correct. Well done!"
	if answer5 >14:
		print "Your answer to question 5 is incorrect."
	if answer5 <14:
		print "Your answer to question 5 is incorrect."

