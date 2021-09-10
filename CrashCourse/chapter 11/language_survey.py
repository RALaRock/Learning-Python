# use survey.py to create a simple language survey

from survey import AnonymousSurvey

# define a question and instantiate a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# show the survey question and store responses
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    my_survey.store_response(response)

# show the survey results
print("\nThank you to everyone who participated in the survey.")
my_survey.show_results()
