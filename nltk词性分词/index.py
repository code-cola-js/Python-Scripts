import nltk

sentence = "Owing to the remarkable development in mass-communications, people everywhere are feeling new wants and are being exposed to new customs and ideas, while governments are often forced to introduce still further innovations for the reasons given above."

words = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(words)

new_sentence = ""

for i, tagged_word in enumerate(tagged_words):
    word, tag = tagged_word
    if tag.startswith("NN") or tag.startswith("VB") or tag.startswith("JJ"):
        # If the word is a noun, verb, or adjective, add <span> tags
        word = "<span>" + word + "</span>"
    else:
        # Otherwise, just use the original word
        word = word

    # Add the word to the new sentence
    new_sentence += word

    # If the current word is not the last word, add a space
    if i < len(tagged_words) - 1:
        new_sentence += " "

print(new_sentence)
