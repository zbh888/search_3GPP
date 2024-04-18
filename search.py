from docx import Document

# use , to achieve "and" search
def search(words, text):
    found = True
    for word in words.split(","):
        found = (word.lower() in text.lower()) and found
    return found

def search_one_file(file_path, key_word):
    res = []
    document = Document(file_path)
    for paragraph in document.paragraphs:
        text = paragraph.text
        if search(key_word, text):
            res.append(text)
    return res

# Example usage
file_path = "./latest/Rel-15/21_series/21905-f20.docx"
target_word = "Generation,3G"
res = search_one_file(file_path, target_word)
