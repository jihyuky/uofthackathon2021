"""
After pasting in the terms and condition you wish to analyze into the "terms_and_conditions.txt",
run this file for a summary + potential red flags & points of importance.
"""
from functions import *

scary_words = ["at your own risk", 'we reserve the right to modify', 'replace the terms',
               'if your breach these terms', 'material breach', 'suspend the service',
               'sell your information', 'process your data', 'share your data', 'mercantile agent',
               'sole discretion', 'will be liable', 'distribute your data', 'automatically renewed',
               'excludes all liability', 'financial obligation']

text = open('google_privacy_policy.txt', 'r').read()

sentence_list = create_sentence_list(text)

freq_table = create_freq_table(text)

print(summary_generator(sentence_list, freq_table) + "\n")

print(find_scary_phrases(sentence_list, scary_words))
