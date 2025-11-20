input = input("Nhập chuỗi: ")
stop = ["is", "a", "this"]

def remove_punctuation(s):
    blocked_chars = ".,!?()[]{}:;'\"-" 
    result = ""
    for char in s:
        if char not in blocked_chars:
            result += char
    return result

def to_lower(s):
    return s.lower()

def remove_stopwords(s, stopwords):
    words = s.split()
    filtered_words = [w for w in words if w not in stopwords]
    return " ".join(filtered_words)

def pipeline(s, steps):
    current_value = s
    for step_func in steps:
        current_value = step_func(current_value)
    return current_value

def count_words(s):
    result_dict = {}
    words = s.split()
    for word in words:
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1
    return result_dict

processing_steps = [
    remove_punctuation,
    to_lower,
    lambda x: remove_stopwords(x, stop)
]

processed_string = pipeline(input, processing_steps)
print(processed_string)

word_counts = count_words(processed_string)
print(word_counts)