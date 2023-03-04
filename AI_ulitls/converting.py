import json

all_words = list()
for name in range(1, 7):
    with open(f'learning_material\\clean_words{name}.txt', 'r', encoding='utf=8') as words_f:
        words = words_f.readline().split()
    all_words += words
    print(len(all_words))

main_dic = dict()

for word in all_words:
    if word not in main_dic:
        main_dic[word] = [1, len(word), len(set(word))]
    else:
        main_dic[word][0] += 1

for word in ['the', 'i', 'he', 'she', 'and', 'in', 'on', 'at', 'from', 'a', 'his', 'her', 'my', 'you']:
    del main_dic[word]

with open("learning_material\\word_data.json", "w") as outfile:
    json.dump(main_dic, outfile)
