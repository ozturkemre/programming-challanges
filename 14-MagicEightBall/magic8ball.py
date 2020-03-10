import sys, random


def get_answer():
    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it",
               " As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again",
               "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
    return answers[random.randint(0, len(answers) - 1)]


while 1:
    question = input("Ask to magic 8 ball a question (type \"quit\" to quit):")

    if question == "quit" or question == "\"quit\"":
        sys.exit()
    answer = get_answer()
    print(answer)
