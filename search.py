import math


def calculatetfidf(index):
    doc_count = len(set(doc for postings in index.values() for doc,  in postings))
    tfidfindex = {}
    for term, postings in index.items():
        df = len(postings)
        idf = math.log(doc_count / df) if df else 0
        tfidf_index[term] = {doc: (freq / sum([f for , f in postings])) * idf for doc, freq in postings}
    return tfidf_index

tfidf_index = calculate_tfidf(index)

def search(query, tfidf_index):
    terms = query.lower().split()
    scores = {}
    for term in terms:
        if term in tfidf_index:
            for doc, tfidf in tfidf_index[term].items():
                if doc not in scores:
                    scores[doc] = 0
                scores[doc] += tfidf
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)