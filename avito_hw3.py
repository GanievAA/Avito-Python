class CountVectorizer:

    def __init__(self, lowercase=True, unique_words=None):
        self.lowercase=lowercase
        self.unique_words = unique_words

    def fit_transform(self, corpus):
        texts_list = [text.split(' ') for text in corpus]
        bag_of_words = []
        for split_text in texts_list:
            split_text = [elem.lower().strip(' .,:?!;""(){}[]<>&#%^+*') if self.lowercase else elem for elem in split_text]
            bag_of_words.extend(split_text)
        unique_words = []
        for word in bag_of_words:
            if word not in unique_words:
                unique_words.append(word)
        result = []
        for split_text in texts_list:
            split_text = [elem.lower().strip(',') if self.lowercase else elem for elem in split_text]
            vector = [bag_of_words.count(elem) for elem in split_text]
            result.append(vector)
        self.unique_words = unique_words
        return result

    def get_feature_names(self):
        return self.unique_words


cv = CountVectorizer()
print(cv.fit_transform( ['milk: mikshake* "apple" banana,', 'apple juice. Banana']))
print(cv.get_feature_names())
