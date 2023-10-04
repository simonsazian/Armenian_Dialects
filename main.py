import os
from google.cloud import translate_v2
from translate import change_dialect

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"key.json"

translate_client = translate_v2.Client()

# Get input text from HTML server
text = "that was so easy"
print("Input:", text)

# Translate to standard Eastern Armenian (Google Translate default)
# Note: call returns a dictionary of the following  
# {'translatedText': output_txt, 'detectedSourceLanguage': lang_code, 'input': input_txt}
full_output = translate_client.translate(text, target_language="hy")

standard_eastern = full_output['translatedText']
print("Eastern:", standard_eastern)

standard_western = change_dialect(standard_eastern, "standard_western")

# Get western Armenian translation
print("Western:", standard_western)
