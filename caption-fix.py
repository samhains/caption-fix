from pattern.en import verbs, lemma, lexeme, parsetree, Sentence
sentence = "a cat is sitting on a table"
sentence_2 = "a person is holding a slice of pizza"
sentence_3 = "a man is taking a selfie in a mirror"
sentence_4 = "a woman is holding a teddy bear in front of a window"


def fix_caption(str):
    s = parsetree(str, lemmata=True)
    string = ''
    for sentence in s:
        for i, chunk in enumerate(sentence.chunks):
            if chunk.type == 'VP' and len(chunk) == 2:
                print('@!!')
                verb = chunk[1].string
                string += lexeme(verb)[1]+' '
            else:
                for j, w in enumerate(chunk.words):
                    if i == 0 and j == 0:
                        pass
                    else:
                        string = string + w.string+' '

    return string[:1].upper() + string[1:-1]


print(fix_caption(sentence_2))
print(fix_caption(sentence_3))
print(fix_caption(sentence_4))

