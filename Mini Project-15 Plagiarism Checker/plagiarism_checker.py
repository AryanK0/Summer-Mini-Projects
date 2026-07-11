from difflib import SequenceMatcher

def check_similarity(text1, text2):
    ratio = SequenceMatcher(None, text1, text2).ratio()
    return ratio * 100

if __name__ == '__main__':
    doc1 = 'Machine learning is fascinating.'
    doc2 = 'Machine learning is extremely fascinating.'
    sim = check_similarity(doc1, doc2)
    print(f'Similarity between documents: {sim:.2f}%')
    if sim > 80:
        print('High plagiarism detected!')