from django.shortcuts import render
import mysql.connector as mc
# Create your views here.
def home(request):
    connection = mc.connect(
        host='localhost',
        user='root',
        password='arhum123',
        database='questions'
    )
    
    # Create a cursor to execute queries
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM QUESTION ORDER BY RAND() LIMIT 15')
    rq=cursor.fetchall()
    questions = []

    # Process each random question
    for random_question in rq:
        # Split the options string into a list
        options = random_question[4].split(',')
        options = [option.split(') ')[1] for option in options]
        # Create a dictionary for each question and options
        question_data = {
            'question_text': random_question[3],
            'options': options,
        }

        # Add the question data to the list
        questions.append(question_data)

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    # Pass the question data to the template
    context = {
        'questions': questions,
    }
    return render (request,"test.html",context)


def actualhome(request):
    return render (request, "mainhomepage.html")



def debughome(request):
    return render (request, "debughome.html")



def facultyportal(request):
    return render (request, "facultyportal.html")


def aboutme(request):
    return render (request, "about.html")

def resource(request):
    return render (request, "resources.html")

