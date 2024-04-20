from docx import Document
import os
import pickle

def search(words, text):
    res = []
    orWords = words.split("|")
    for orWord in orWords:
        orFound = True
        for word in orWord.split(","):
            orFound = (word.lower() in text.lower()) and orFound
        res.append(orFound)
    return any(res)

def search_one_file(file_path, key_word):
    res = []
    document = Document(file_path)
    for paragraph in document.paragraphs:
        text = paragraph.text
        if search(key_word, text):
            res.append(text)
    return res

def search_3GPP(key_word):
    print("Starting searching")
    dict = {}
    dict["keyword"] = key_word
    root = './3GPP'
    Rels = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]

    file_count = 0
    for R in Rels:
        Relpath = os.path.join(root, R)
        Series = [d for d in os.listdir(Relpath) if os.path.isdir(os.path.join(Relpath, d))]
        for S in Series:
            print(f"Search in {R}, {S}")
            Spath = os.path.join(Relpath, S)
            Files = [f for f in os.listdir(Spath) if f.find('.docx')!=-1]
            for F in Files:
                Fpath = os.path.join(Spath, F)
                try:
                    result = search_one_file(Fpath, key_word)
                    if len(result) > 0:
                        dict[(R, S, F)] = result
                        file_count += 1
                        print(f"+++++ Positive in {Fpath}")
                except:
                    print("An exception occurred when handling " + Fpath)
    dict['filecount'] = file_count
    with open('res.pkl', 'wb') as outp:
        pickle.dump(dict, outp, pickle.HIGHEST_PROTOCOL)
    
            
search_3GPP("signalling,load|signaling,load|network,congest|flood,control plane|control plane,congest|storm|cp,flood|cp,congest|cp,load|control plane,load")
