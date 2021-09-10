import unittest

from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """Create a survey and responses for all test cases"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "Mandarin"]

    def test_store_single_response(self):
        """Tests that a single response is stored correctly."""
        # create an instance of the AnonymousSurvey class

        # modify to use setUp()
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)

        # we are testing if responses are stored properly
        # store a response
        # my_survey.store_response("English")
        self.my_survey.store_response(self.responses[0])

        # test if the response was stored properly in the list
        # self.assertIn("English", my_survey.responses)
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three responses are stored properly."""

        # modify to use setUp()
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # responses = ["English", "Spanish", "Mandarin"]

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


# prevent running this test if this test is imported into
# another program file
if __name__ == "__main__":
    unittest.main()
