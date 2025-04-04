from question import Questionnaire 

def test_questionnaire():
    q = Questionnaire()
    result = q.ask_specific_question_with_answer(2, "Seaweed")
    assert result
