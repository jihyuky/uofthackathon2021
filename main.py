"""
After pasting in the terms and condition you wish to analyze into the "terms_and_conditions.txt",
run this file for a summary + potential red flags & points of importance.
"""
from functions import *
from fpdf import FPDF

scary_words = ["at your own risk", 'we reserve the right to modify', 'replace the terms',
               'if your breach these terms', 'material breach', 'suspend the service',
               'sell your information', 'process your data', 'share your data', 'mercantile agent',
               'sole discretion', 'will be liable', 'distribute your data', 'automatically renewed',
               'excludes all liability', 'financial obligation']

text = open('google_privacy_policy.txt', 'r').read()

sentence_list = create_sentence_list(text)

freq_table = create_freq_table(text)

summary = summary_generator(sentence_list, freq_table) + "\n \n"

notes = find_scary_phrases(sentence_list, scary_words)

pdf = FPDF(format='letter')

pdf.set_left_margin(20)
pdf.set_right_margin(20)
pdf.set_top_margin(20)

pdf.add_page()

pdf.set_font('Arial', 'B', 14)
pdf.cell(180, 8, txt="Summary of Terms & Conditions", ln=1, align='C')

pdf.set_font('Arial', 'I', 12)
pdf.cell(180, 8, txt="Generated With Concisely Yours", ln=1, align='C')

pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Summary", ln=2, align='L')

pdf.add_font('ArialUnicode', fname='Arial-Unicode-Regular.ttf', uni=True)
pdf.set_font('ArialUnicode', '', 10)

pdf.multi_cell(0, 6, summary)

pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Potential Red Flags & Points of Importance", ln=2, align='L')

pdf.add_font('ArialUnicode', fname='Arial-Unicode-Regular.ttf', uni=True)
pdf.set_font('ArialUnicode', '', 10)

pdf.multi_cell(0, 6, notes)

FPDF.footer(pdf)
pdf.set_y(249)
pdf.set_font('Arial', 'I', 8)
pdf.cell(0, 10, 'A UofTHacks VIII Project', 0, 0, 'C')

pdf.output("summary.pdf")
