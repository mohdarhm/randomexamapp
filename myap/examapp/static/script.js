document.addEventListener('DOMContentLoaded', function() {
  var currentProgress = document.getElementById('current-progress');
  var totalQuestions = document.getElementById('total-questions');
  var questionElements = document.querySelectorAll('.questions-container .question');
  var submitButton = document.getElementById("btn");

  totalQuestions.textContent = questionElements.length; // Set the total number of questions

  // Reset the form and progress on page reload
  window.addEventListener('beforeunload', function() {
    resetForm();
    currentProgress.textContent = '0';
  });

  // Listen for change events on radio inputs
  questionElements.forEach(function(questionElement) {
    var radioInputs = questionElement.querySelectorAll('input[type="radio"]');
    radioInputs.forEach(function(radioInput) {
      radioInput.addEventListener('change', function() {
        if (radioInput.checked) {
          var completedQuestions = document.querySelectorAll('.questions-container .question input:checked').length;
          currentProgress.textContent = completedQuestions; // Update the current progress
        }
      });
    });
  });

  // Add event listener to submit button
  submitButton.addEventListener('click', function(event) {
    var unansweredQuestions = getUnansweredQuestions();

    if (unansweredQuestions.length > 0) {
      event.preventDefault(); // Prevent form submission

      unansweredQuestions.forEach(function(questionElement) {
        questionElement.classList.add('unanswered'); // Apply the 'unanswered' class to highlight unanswered questions
      });
    } else {
      // All questions answered, submit the form
      document.getElementById('exam-form').submit();
    }
  });

  // Clear the selected options on page load
  resetForm();

  function resetForm() {
    questionElements.forEach(function(questionElement) {
      var radioInputs = questionElement.querySelectorAll('input[type="radio"]');
      radioInputs.forEach(function(radioInput) {
        radioInput.checked = false;
      });

      questionElement.classList.remove('unanswered'); // Remove the 'unanswered' class when resetting the form
    });
  }

  function getUnansweredQuestions() {
    var unansweredQuestions = [];

    questionElements.forEach(function(questionElement) {
      var radioInputs = questionElement.querySelectorAll('input[type="radio"]');
      var isAnswered = Array.from(radioInputs).some(function(radioInput) {
        return radioInput.checked;
      });

      if (!isAnswered) {
        unansweredQuestions.push(questionElement);
      }
    });

    return unansweredQuestions;
  }
});
