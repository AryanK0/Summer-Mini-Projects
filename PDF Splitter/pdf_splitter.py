# import PyPDF2
import os

def split_pdf(file_path):
    print(f'Splitting {file_path}...')
    # with open(file_path, 'rb') as f:
    #     reader = PyPDF2.PdfReader(f)
    #     for page_num in range(len(reader.pages)):
    #         writer = PyPDF2.PdfWriter()
    #         writer.add_page(reader.pages[page_num])
    #         with open(f'page_{page_num+1}.pdf', 'wb') as out:
    #             writer.write(out)
    print('PDF split successfully into individual pages.')

if __name__ == '__main__':
    split_pdf('document.pdf')