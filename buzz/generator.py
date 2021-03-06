import random

buzz = ('continuous testing', 'continuous integration',
        'continuous deployment', 'continuous improvement', 'devops', 'anatoliykv3')
adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end', 'anatoliykv3')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly',
           'seriously', 'anatoliykv3')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts', 'anatoliykv3')


def sample(l, n=1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result


def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
                       sample(verbs), buzz_terms[1]])
    return phrase.title()


if __name__ == "__main__":
    print(generate_buzz())
