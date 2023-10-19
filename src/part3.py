from gensim import models, similarities

def build_retrieval_models(dictionary, corpus):
    # 3.1 Build TF-IDF model using the corpus
    tfidf_model = models.TfidfModel(corpus)

    # 3.2 Map Bags-of-Words into TF-IDF weights
    tfidf_corpus = tfidf_model[corpus]

    # 3.3 Construct MatrixSimilarity object for TF-IDF model
    tfidf_index = similarities.MatrixSimilarity(tfidf_corpus)

    # 3.4 Build LSI model using the TF-IDF weighted corpus and use it for similarity
    lsi_model = models.LsiModel(tfidf_corpus, id2word=dictionary, num_topics=100)
    lsi_corpus = lsi_model[tfidf_corpus]
    lsi_index = similarities.MatrixSimilarity(lsi_corpus)

    return tfidf_model, lsi_model, tfidf_index, lsi_index

def interpret_lsi_topics(lsi_model, num_topics=3):
    # 3.5 Report and interpret first 3 LSI topics
    topics = lsi_model.show_topics(num_topics=num_topics)
    for topic in topics:
        print(topic)