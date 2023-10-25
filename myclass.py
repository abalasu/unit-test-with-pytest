class AnonymusSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, response):
        self.responses.append(response)

    def show_results(self):
        print("The Final results ")
        for response in self.responses:
            print(response)

"""

myquestion = "What was your first car? "
mysurvey = AnonymusSurvey(myquestion)

mysurvey.show_question()
while True:
    response = input("My first car was ")
    if response == 'q' or response == 'Q':
        break
    mysurvey.store_response(response)

mysurvey.show_results()

"""