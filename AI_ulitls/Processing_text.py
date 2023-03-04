import nltk
from string import punctuation
from tqdm import tqdm

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def tokenize(text):
    text = text.replace('\n', ' ')

    clean_txt = list()
    for word in tqdm(nltk.word_tokenize(text)):
        if word not in punctuation and word != '...' and word not in '``' and \
                word not in "''" and "'" not in word and word.isalpha():
            clean_txt.append(word)

    return clean_txt


def cleaning(text):
    text = [word for word in text if word not in nltk.corpus.stopwords.words('english') and word != 'the']
    tagged_sentence = nltk.tag.pos_tag(text)
    text = [word.lower() for word, tag in tagged_sentence if tag != 'NNP' and tag != 'NNPS']

    return text


def lemmetize(tokens):
    for i in tqdm(range(len(tokens))):
        for part_speach in 'navrs':
            tokens[i] = nltk.stem.WordNetLemmatizer().lemmatize(tokens[i], part_speach)
    return tokens


if __name__ == '__main__':
    text = str()

    with open('learning_material\\Angels_demon.txt', 'r', encoding='utf-8') as book:
        for line in book:
            text += line

    tokens = tokenize(text)
    tokens = cleaning(tokens)
    tokens = lemmetize(tokens)

    with open('learning_material/clean_words6.txt', 'w', encoding='utf-8') as words:
        for token in tokens:
            print(token, file=words, end=' ')
