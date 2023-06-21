from django.shortcuts import render, redirect
import mysql.connector as mc
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from faculty_questions.models import Question


def result_summary2(request):
    if request.method == 'POST':
        # Retrieve the POST data
        post_data = request.POST
        
        # Display the POST data
        context = {'post_data': post_data}
        return render(request, 'debug.html', context)
    
    return render(request, 'debug.html')




def result_summary(request):
    if not request.user.is_authenticated:
        return redirect(reverse('student-login'))

    # Retrieve the submitted form data
    submitted_data = request.POST

    # Retrieve the question IDs from the submitted form data
    question_ids = [int(key) for key in submitted_data.keys() if key.isnumeric()]

    # Retrieve the corresponding questions from the database
    questions = Question.objects.filter(id__in=question_ids)

    # Process each question and compare with the submitted data
    result_data = []
    total_score = 0

    for question in questions:
        question_text = question.question_text
        selected_option = submitted_data.get(str(question.id))
        correct_answer = question.correct_answer.split(') ', 1)[1]
        # Check if the selected option matches the correct answer
        is_correct = selected_option == correct_answer

        # Calculate the score based on correctness
        score = 1 if is_correct else 0
        total_score += score

        # Prepare the result data for each question
        result_data.append({
            'question': question_text,
            'selected_option': selected_option,
            'correct_answer': question.correct_answer,
            'is_correct': is_correct
        })

    # Pass the result data and total score to the template
    context = {
        'result_data': result_data,
        'total_score': total_score,
        'total_possbile': len(questions)
    }

    return render(request, 'result_summary.html', context)

# Create your views here.
@user_passes_test(lambda u: u.groups.filter(name='Students').exists(), login_url='student-login')
def home(request):
    if not request.user.is_authenticated:
        # User is not authenticated, redirect to the student login page
        return redirect(reverse('student-login'))  # Adjust 'student-login' to the actual URL name of the student login page

    # User is authenticated, continue with the logic to retrieve questions
    connection = mc.connect(
        host='34.93.183.253',
        user='root',
        password='arhum123',
        database='questions'
    )
     # Create a cursor to execute queries
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM question ORDER BY RAND() LIMIT 3')
    rq=cursor.fetchall()
    questions = []

    # Process each random question
    for random_question in rq:
        # Split the options string into a list
        options = random_question[4].split(',')
        options = [option.split(') ')[1] for option in options]
        qid=random_question[0]
        # Create a dictionary for each question and options
        question_data = {
            'question_text': random_question[3],
            'options': options,
            'id': qid,
        }
        # Add the question data to the list
        questions.append(question_data)

    # Rest of the logic to retrieve questions and process data...

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    # Pass the question data to the template
    context = {
        'questions': questions,
    }
    return render(request, 'test.html', context)

def actualhome(request):
    return render (request, "mainhomepage.html")



def debughome(request):
    return render (request, "debughome.html")

    
def aboutme(request):
    return render (request, "about.html")

def resource(request):
    return render (request, "resources.html")

@login_required(login_url='student-login')
def student_redirection_view(request):
    return redirect('home')



def student_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User credentials are valid, log in the user
            if  user.groups.filter(name="Students").exists():
                login(request, user)
                return redirect('examportal')  # Redirect to the examportal page after successful login
            else:  
                messages.error(request, 'Faculties cannot access the resource requested.')
                return redirect('student-login')
        else:
            # Invalid username or password
            messages.error(request, 'Invalid username or password.')

    return render(request, 'studentlogin.html')

