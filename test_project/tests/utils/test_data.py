import random

def get_random_note_text():
    notes = [
        "Shall I compare thee to a summer’s day?",  # Shakespeare
        "Hope is the thing with feathers that perches in the soul.",  # Emily Dickinson
        "I wandered lonely as a cloud that floats on high o’er vales and hills.",  # William Wordsworth
        "Do not go gentle into that good night. Rage, rage against the dying of the light.",  # Dylan Thomas
        "Tread softly because you tread on my dreams."  # W. B. Yeats
    ]
    return random.choice(notes)
