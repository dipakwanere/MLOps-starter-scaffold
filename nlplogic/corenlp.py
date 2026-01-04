from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search wikipedia"""
    print(f"Searching for name:{name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarizes a Wikipedia article."""
    print(f"finding wikipedia summary for a name:{name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Gets text blob object and returns"""

    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find wikipedia anme and returns back phrases"""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
