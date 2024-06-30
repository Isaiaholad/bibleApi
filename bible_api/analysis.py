from collections import Counter
import pandas as pd

def find_longest_and_shortest_chapters(dataset):
    chapter_verse_counts = dataset.groupby(['book', 'chapter'])['verse'].count().reset_index()
    chapter_verse_counts.columns = ['book', 'chapter', 'verse_count']
    longest_chapter = chapter_verse_counts.loc[chapter_verse_counts['verse_count'].idxmax()]
    shortest_chapter = chapter_verse_counts.loc[chapter_verse_counts['verse_count'].idxmin()]
    return longest_chapter, shortest_chapter

def rearrange_chapters_by_verse_count(dataset):
    chapter_verse_counts = dataset.groupby(['book', 'chapter'])['verse'].count().reset_index()
    chapter_verse_counts.columns = ['book', 'chapter', 'verse_count']
    sorted_chapters = chapter_verse_counts.sort_values(by='verse_count')
    return sorted_chapters

def identify_common_words_and_phrases(dataset):
    words = dataset['text'].str.cat(sep=' ').lower().split()
    common_words = Counter(words).most_common()
    return common_words

def list_top_20_most_common_phrases(dataset):
    words = dataset['text'].str.cat(sep=' ').lower().split()
    phrases = [' '.join(words[i:i+2]) for i in range(len(words)-1)]
    common_phrases = Counter(phrases).most_common(20)
    return common_phrases

def list_top_20_shortest_verse_text(dataset):
    shortest_verses = dataset.loc[dataset['text'].str.len().sort_values().index][:20]
    return shortest_verses
