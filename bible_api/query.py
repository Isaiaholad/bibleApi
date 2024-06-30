import re
def get_total_chapters(book_name, dataset):
    book_data = dataset[dataset['book'] == book_name]
    total_chapters = book_data['chapter'].nunique()
    return total_chapters

def get_total_verses(book_name, chapter, dataset):
    chapter_data = dataset[(dataset['book'] == book_name) & (dataset['chapter'] == chapter)]
    total_verses = chapter_data['verse'].nunique()
    return total_verses

def query_text(book_name, chapter, dataset, verses):
    if isinstance(verses, int):
        verses = [verses]
    chapter_data = dataset[(dataset['book'] == book_name) & (dataset['chapter'] == chapter)]
    chapter_data = chapter_data[chapter_data['verse'].isin(verses)]
    text_list = chapter_data['text'].tolist()
    return text_list

def search_verses(keyword, dataset):
    keyword = keyword.lower()
    matching_verses = dataset[dataset['text'].str.contains(keyword, case=False, na=False)]
    return matching_verses[['book', 'chapter', 'verse', 'text']]

def count_keyword_occurrences(keyword, dataset):
    keyword = keyword.lower()
    keyword_occurrences = dataset['text'].str.count(keyword, flags=re.IGNORECASE).sum()
    return keyword_occurrences
