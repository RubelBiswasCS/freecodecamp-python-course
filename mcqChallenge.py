from Question import Questions
question_prompts=[
    "What is the capital of Bangladesh\n1.Dhaka\n2.Noakhali\n3.Khulan\n\n",
    "What is the main language of Bangladesh\n1.English\n2.Bengali\n3.Spanish\n\n",
    "Who is the number 1 all rounder \n1.Jadeja\n2.Shakib\n3.Stock\n\n",

]
questions=[
    Questions(question_prompts[0],"1"),
    Questions(question_prompts[1], "2"),
    Questions(question_prompts[2], "2"),
]


def test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score += 1

    print("you got" + str(score) + "/" + str(len(questions))+"correct")

test(questions)