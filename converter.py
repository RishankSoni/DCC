import fitz
import csv

def pdf_to_csv(input_file, output_file):
    writer = csv.writer(open(output_file, 'w', newline=''))
    doc = fitz.open(input_file)
    for i, page in enumerate(doc):
        tabs = page.find_tables()
        if tabs.tables:
            extracted_table = tabs[0].extract()
            if i != 0: 
                extracted_table = extracted_table[1:]
            writer.writerows(extracted_table)

pdf_to_csv("D:/DCC/r.pdf", "D:/DCC/bonds_encash.csv")
pdf_to_csv("D:/DCC/ZPtCIiTvJH.pdf", "D:/DCC/bonds_purchased.csv")
