import json
from tqdm import tqdm
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
model = KMeans(n_clusters=3)

if __name__ == '__main__':
    with open("learning_material\\word_data.json", "r") as dic:
        main_dict = json.load(dic)

    ls_data = list()
    for word in main_dict:
        ls_data.append(main_dict[word])

    scaler = MinMaxScaler()
    scaler_fit = scaler.fit(ls_data)
    scaled_data = scaler_fit.transform(ls_data)

    model.fit(scaled_data)
    predictions = model.predict(scaled_data)

    test = dict()
    for i, word in enumerate(main_dict):
        if predictions[i] in [2]:
            test[word] = ['difficult', scaled_data[i]]
        elif predictions[i] in [0]:
            test[word] = ['medium', scaled_data[i]]
        elif predictions[i] in [1]:
            test[word] = ['easy', scaled_data[i]]
        else:
            test[word] = [predictions[i], main_dict[word]]

    all_words = list()
    with open('all_words.txt', 'r', encoding='utf-8') as inf:
        for word in inf:
            all_words.append(word.replace('\n', ''))

    easy = list()
    medium = list()
    difficult = list()
    for word in tqdm(all_words):
        if word in test:
            prediction = model.predict([test[word][1]])
        else:
            ls_data.append([0, len(word), len(set(word))])
            scaled_data = scaler_fit.transform(ls_data)
            prediction = model.predict([scaled_data[len(scaled_data) - 1]])
            ls_data.pop()

        if prediction == 1:
            easy.append(word)
        elif prediction == 0:
            medium.append(word)
        elif prediction == 2:
            difficult.append(word)

    with open('sorted_words\\easy.txt', 'w', encoding='utf-8') as words:
        for word in easy:
            print(word, file=words)
    with open('sorted_words\\medium.txt', 'w', encoding='utf-8') as words:
        for word in medium:
            print(word, file=words)
    with open('sorted_words\\difficult.txt', 'w', encoding='utf-8') as words:
        for word in difficult:
            print(word, file=words)
