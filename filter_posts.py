def filter_post(key_words, text_post):
    for i in key_words:    
        return any([i.lower() in text_post.lower() for i in key_words])