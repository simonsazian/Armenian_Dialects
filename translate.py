import json

# Orchestrator function to change input to a specified dialect
# Arguments:
# input: standard Eastern Armenian translated directly from Google API
# dialect: string used to specify Armenian dialect

# Returns:
# output: Armenian output in the specified dialect

def change_dialect(input, dialect):
    # We will first change to dialect-specific lexicon
    x1 = replace_words(input)

    # Then change any grammatical rules to the dialect
    # x2 = change_grammar()

    # Lastly, change spelling to match either Classical or Reformed Orthography
    # x3 = change_spelling()

    # return the new output in the specified dialect
    return x1


def replace_words(input):
    # Open proper JSON dictionary file
    with open('western_dict.json', 'r', encoding='utf-8') as json_file:
        new_dict = json.load(json_file)

    words = input.split()

    # Replace all words found in dictionary with their dialectal counterparts
    replaced_words = [new_dict[word] if word in new_dict else word for word in words]
    new_sentence = ' '.join(replaced_words)
    
    return new_sentence