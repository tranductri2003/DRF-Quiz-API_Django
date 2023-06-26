from rest_framework import serializers
from .models import Quizzes, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    num_questions = serializers.SerializerMethodField()

    class Meta:
        model = Quizzes
        fields = [
            'title', 'num_questions'
        ]

    def get_num_questions(self, obj):
        return obj.question.count()


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:

        model = Question
        fields = [
            'title', 'answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:

        model = Question
        fields = [
            'quiz', 'title', 'answer',
        ]
