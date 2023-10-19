import part1
import math

def preprocess_query(query, dictionary):
    # 4.1 Preprocess the query and convert to BOW representation
    processed_query = part1.preprocess(query)[0][0]
    query_bow = dictionary.doc2bow(processed_query)
    return query_bow

def query_to_tfidf(tfidf_model, query_bow):
    # 4.2 Convert BOW to TF-IDF representation
    query_tfidf = tfidf_model[query_bow]
    return query_tfidf

def get_top_tfidf_paragraphs(tfidf_index, query_tfidf, original_texts, top_n=3):
    # 4.3 Get top relevant paragraphs based on the query
    sims = tfidf_index[query_tfidf]
    sorted_sims = sorted(enumerate(sims), key=lambda x: math.fabs(x[1]), reverse=True)
    
    top_paragraphs = []
    for i in range(top_n):
        paragraph_number, similarity = sorted_sims[i]
        # Here, truncating to the first 5 lines for display purposes
        truncated_paragraph = '\n'.join(original_texts[paragraph_number].split('\n')[:5])
        top_paragraphs.append((paragraph_number, truncated_paragraph))
    
    return top_paragraphs

def get_top_lsi_paragraphs(lsi_index, query_lsi, original_texts, top_n=3):
    sims = lsi_index[query_lsi]
    sorted_sims = sorted(enumerate(sims), key=lambda x: math.fabs(x[1]), reverse=True)
    
    top_paragraphs = []
    for i in range(top_n):
        paragraph_number, similarity = sorted_sims[i]
        # Here, truncating to the first 5 lines for display purposes
        truncated_paragraph = '\n'.join(original_texts[paragraph_number].split('\n')[:5])
        top_paragraphs.append((paragraph_number, truncated_paragraph))
    
    return top_paragraphs

def qviri(dictionary, tfidf_index, tfidf_model, original_paragraphs, lsi_index, lsi_model):
    mode = "tfidf"
    while True:
        query = input("Enter query: ")
        if query.strip() == "":
            continue
    
        if query.startswith("!exit"):
            print("Bye!")
            break

        if query.startswith("!mode"):
            mode = query.split()[1]
            print(f"Switched to {mode} mode")
            continue

        print("-" * 50)
        query_bow = preprocess_query(query, dictionary)
        query_tfidf = query_to_tfidf(tfidf_model, query_bow)
        if mode == "tfidf":
            top_paragraphs = get_top_tfidf_paragraphs(tfidf_index, query_tfidf, original_paragraphs)
        elif mode == "lsi":
            query_lsi = lsi_model[query_tfidf]
            top_paragraphs = get_top_lsi_paragraphs(lsi_index, query_lsi, original_paragraphs)

        for paragraph_number, paragraph in top_paragraphs:
            print(f"[paragraph {paragraph_number}]")
            print("\n" + paragraph.strip())
            print("")