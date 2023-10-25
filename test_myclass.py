from myclass import AnonymusSurvey

def test_store_response():
    question = "What was your first car? "
    car_survey = AnonymusSurvey(question)
    responses = ["Honda", "Toyota", "Honda"]
    for response in responses:
        car_survey.store_response(response)
    for response in responses:
        assert response in car_survey.responses

def test_question():
    question = "What was your first car? "
    car_survey = AnonymusSurvey(question)
    assert car_survey.question == question

