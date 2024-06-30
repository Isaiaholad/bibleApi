import random
from .query import search_verses, count_keyword_occurrences

def generate_quiz_question(dataset):
    random_row = dataset.sample(n=1).iloc[0]
    correct_book = random_row['book']
    correct_chapter = random_row['chapter']
    correct_verse = random_row['verse']
    correct_text = random_row['text']
    
    wrong_answers = []
    while len(wrong_answers) < 3:
        random_row = dataset.sample(n=1).iloc[0]
        wrong_book = random_row['book']
        wrong_chapter = random_row['chapter']
        wrong_verse = random_row['verse']
        if (wrong_book, wrong_chapter, wrong_verse) != (correct_book, correct_chapter, correct_verse):
            wrong_answers.append((wrong_book, wrong_chapter, wrong_verse))
    
    question = f"Which chapter and verse does this text belong to?\n\n'{correct_text}'\n"
    answers = [
        f"A: {wrong_answers[0][0]} {wrong_answers[0][1]}:{wrong_answers[0][2]}",
        f"B: {wrong_answers[1][0]} {wrong_answers[1][1]}:{wrong_answers[1][2]}",
        f"C: {wrong_answers[2][0]} {wrong_answers[2][1]}:{wrong_answers[2][2]}",
        f"D: {correct_book} {correct_chapter}:{correct_verse}"
    ]
    random.shuffle(answers)
    return question, answers, f"{correct_book} {correct_chapter}:{correct_verse}"

def generate_verse_count_quiz_question(dataset):
    book_chapters = dataset.groupby(['book', 'chapter'])['verse'].count().reset_index()
    book_chapters.columns = ['book', 'chapter', 'verse_count']

    random_book_chapter_row = book_chapters.sample(n=1).iloc[0]
    correct_book = random_book_chapter_row['book']
    correct_chapter = random_book_chapter_row['chapter']
    correct_verse_count = random_book_chapter_row['verse_count']

    wrong_answers = []
    while len(wrong_answers) < 3:
        random_verse_count = random.choice(book_chapters['verse_count'].unique())
        if random_verse_count != correct_verse_count:
            wrong_answers.append(random_verse_count)
    
    question = f"How many verses are in {correct_book} chapter {correct_chapter}?"
    answers = [
        f"A: {wrong_answers[0]}",
        f"B: {wrong_answers[1]}",
        f"C: {wrong_answers[2]}",
        f"D: {correct_verse_count}"
    ]
    random.shuffle(answers)
    return question, answers, correct_verse_count

def generate_book_quiz_question(dataset):
    books = dataset.groupby('book')['chapter'].nunique().reset_index()
    books.columns = ['book', 'chapter_count']

    random_book_row = books.sample(n=1).iloc[0]
    correct_book = random_book_row['book']
    correct_chapter_count = random_book_row['chapter_count']

    wrong_answers = []
    while len(wrong_answers) < 3:
        random_chapter_count = random.choice(books['chapter_count'].unique())
        if random_chapter_count != correct_chapter_count:
            wrong_answers.append(random_chapter_count)
    
    question = f"How many chapters does the book of {correct_book} have?"
    answers = [
        f"A: {wrong_answers[0]}",
        f"B: {wrong_answers[1]}",
        f"C: {wrong_answers[2]}",
        f"D: {correct_chapter_count}"
    ]
    random.shuffle(answers)
    return question, answers, correct_chapter_count

def generate_word_quiz_question(word, dataset):
    count = count_keyword_occurrences(word, dataset)
    wrong_counts = []
    while len(wrong_counts) < 3:
        random_count = random.randint(0, 500)
        if random_count != count:
            wrong_counts.append(random_count)
    
    question = f"How many times does the word '{word}' appear in the Bible?"
    answers = [
        f"A: {wrong_counts[0]}",
        f"B: {wrong_counts[1]}",
        f"C: {wrong_counts[2]}",
        f"D: {count}"
    ]
    random.shuffle(answers)
    return question, answers, count

def generate_word_verse_quiz_question(word, dataset):
    matching_verses = search_verses(word, dataset)
    random_verse = matching_verses.sample(n=1).iloc[0]
    correct_book = random_verse['book']
    correct_chapter = random_verse['chapter']
    correct_verse = random_verse['verse']
    correct_text = random_verse['text']
    
    wrong_answers = []
    while len(wrong_answers) < 3:
        random_verse = matching_verses.sample(n=1).iloc[0]
        wrong_book = random_verse['book']
        wrong_chapter = random_verse['chapter']
        wrong_verse = random_verse['verse']
        if (wrong_book, wrong_chapter, wrong_verse) != (correct_book, correct_chapter, correct_verse):
            wrong_answers.append((wrong_book, wrong_chapter, wrong_verse))
    
    question = f"In which verse does the word '{word}' appear?\n\n'{correct_text}'\n"
    answers = [
        f"A: {wrong_answers[0][0]} {wrong_answers[0][1]}:{wrong_answers[0][2]}",
        f"B: {wrong_answers[1][0]} {wrong_answers[1][1]}:{wrong_answers[1][2]}",]
       
