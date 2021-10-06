from newspaper import Article
import nltk


nltk.download('punkt')


url= 'https://chiniyamnazi.com/safaricom-to-hide-contact-details-on-lipa-na-mpesa/'

article = Article(url) # Instantiates the article object which takes in URl as argument

article.download() # 'Actually' captures the article contents for processing
article.parse() # Translates/Understands the contents of the article 

article.nlp() # Instantiates the natural language processing algos to scan the article

print(f" Title:  {article.title}")
print(f" Author(s):  {article.authors}")
print(f" Publication date:  {article.publish_date}")
print(f" Summary:  {article.summary}")