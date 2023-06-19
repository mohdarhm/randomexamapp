from django.shortcuts import render, redirect
import mysql.connector as mc
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

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
    
    cursor.execute('SELECT * FROM question ORDER BY RAND() LIMIT 15')
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

