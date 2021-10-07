from newspaper import Article
import nltk
import tkinter as tk


nltk.download('punkt')


root = tk.Tk()
root.title("Article Summarizer")
root.geometry("700x500")
    
tklabel = tk.Label(root, text="Title")
tklabel.pack()

title = tk.Text(root, height=1,width=120)
title.config(state="disabled",bg='#dddddd')
title.pack()
    
alabel = tk.Label(root, text="Author")
alabel.pack()
    
author = tk.Text(root, height=1,width=120)
author.config(state="disabled",bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Publication date")
plabel.pack()
    
publication = tk.Text(root, height=1,width=120)
publication.config(state="disabled",bg='#dddddd')
publication.pack()
    
slabel = tk.Label(root, text="Summary")
slabel.pack()
    
summary = tk.Text(root, height=8,width=120)
summary.config(state="disabled",bg='#dddddd')
summary.pack()
    
    
ulabel = tk.Label(root, text="Article URL")
ulabel.pack()
    
url = tk.Text(root, height=1,width=120)
url.config(bg='#dddddd')
url.pack()


def summarize():

    url = ulabel.get("1.0", "end").strip()

    article = Article(url)

    article.download()
    article.parse()
    article.nlp()


    article.title.config(state="normal")
    article.authors.config(state="normal")
    article.publish_date.config(state="normal")
    article.summary.config(state="normal")

    article.title.delete('1.0', 'end')
    article.title.insert('1.0, article.title')

    article.authors.delete('1.0', 'end')
    article.authors.insert('1.0, article.authors')

    article.publish_date.delete('1.0', 'end')
    article.publish_date.insert('1.0, article.publish_date')

    article.summary.delete('1.0', 'end')
    article.summary.insert('1.0, article.summary')

    article.title.config(state="disabled")
    article.authors.config(state="disabled")
    article.publish_date.config(state="disabled")
    article.summary.config(state="disabled")


button = tk.Button(root, text="Generate", command=summarize)
button.pack()
    
root.mainloop()
