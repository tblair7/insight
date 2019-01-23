from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from nltk.corpus import stopwords

from nltk.tokenize import WhitespaceTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer


ws_tokenizer = WhitespaceTokenizer()
lancaster = LancasterStemmer()
porter = PorterStemmer()
snowball = SnowballStemmer('english')

try:
    stopwords = set(stopwords.words('english'))
except:
    nltk.download('stopwords')
    stopwords = set(stopwords.words('english'))




def cleanText(text):

    # import a dictionary of English contractions from another file
    from contractions import contractions_dict
    contraction_dict = contractions_dict

    # replace the contractions with their expanded form
    for contraction, expansion in contraction_dict.items():
        text = text.replace(contraction.lower(),expansion.lower())

    # get rid of newlines
    symbols = ['\'', '\"', '.', ',', '[', ']', '(', ')', '?', '!', '@', '$', '#', '&', '%']

    text = text.strip().replace('\n', ' ').replace('\r', ' ').replace('-',' ')

    for symbol in symbols:
        text = text.replace(symbol, '')

    # lowercase
    text = text.lower()

    return text




def gen_tokens(review, *args):

    ws_tokenized = ws_tokenizer.tokenize(review)

    cleaned_tokens = []

    for token in ws_tokenized:
        if token not in stopwords:
            cleaned_tokens.append(token)

    stemmed_tokens = []

    try:
        method = args[0]
    except:
        method = 'lancaster'

    if method == 'lancaster':
        for token in cleaned_tokens:
            stemmed_tokens.append(lancaster.stem(token.lower().strip()))

    elif method == 'porter':
        for token in cleaned_tokens:
            stemmed_tokens.append(porter.stem(token.lower().strip()))

    elif method == 'snowball':
        for token in cleaned_tokens:
            stemmed_tokens.append(snowball.stem(token.lower().strip()))

    stemmed_text = ' '.join(stemmed_tokens)

    return stemmed_text



def clean_and_tokenize(reviews):
    cleaned_reviews = []

    for review in reviews:
        review_tokens = []
        cleaned_text = cleanText(review)
        cleaned_reviews.append(gen_tokens(cleaned_text))
