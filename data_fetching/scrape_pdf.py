import fitz  # pdf processing
import json 

# PDF URL https://wtop.com/wp-content/uploads/2018/09/Best-Movies-in-Every-Genre.pdf
## BY Film Critic Jason Fraley from WTOP


def extract_text_from_pdf(pdf_path):
    """
    open pdf and extract all text.
    """
    # open pdf file
    doc = fitz.open(pdf_path)
    text = ""  # empty string to append text
    
    # iterate pages in pdf
    for page in doc:
        text += page.get_text()  # extract page text and append to text
    
    return text

def clean_title(line):
    """
    Clean movie title text.
    """
    # split line by spaces and remove first element (ranking),
    # rejoin the remaining elements. This removes ranking.
    title_with_year = ' '.join(line.split(' ')[1:])
    
    # split title and year/director part at the first '(' and take the first part.
    # removes everything from the year onwards.
    cleaned_title = title_with_year.split(' (')[0]
    
    return cleaned_title

def extract_movie_titles(pdf_text):
    """
    extracts movie titles from pdf.

    """
    movie_titles = []  # hold movie titles
    lines = pdf_text.split('\n')  # split pdf text into lines
    
    for line in lines:
        # check if line contains text and starts with a number to ensure its nothing but a movie
        if line.strip() and any(char.isdigit() for char in line[:2]):
            title = clean_title(line)  # clea line to extract the title
            movie_titles.append(title)  # add cleaned title to the list

    return movie_titles

def save_titles_to_json(titles, file_name):
    """
    saves list of movie titles to json.
    """
    with open(file_name, 'w') as f:  # open file for writing
        # write list of titles to the file as json,
        # non-ASCII characters,
        # indent=4 for readablity.
        json.dump(titles, f, ensure_ascii=False, indent=4)


# main execution
pdf_path = '../data/Best-Movies-in-Every-Genre.pdf'  # path to pdf file
pdf_text = extract_text_from_pdf(pdf_path)  # extract text from pdf
movie_titles = extract_movie_titles(pdf_text)  # extract movie titles from pdf text
save_titles_to_json(movie_titles, '../data/extracted_titles.json')  # save titles to json in data folder

print(f"Extracted {len(movie_titles)} titles successfully.")  # print number of titles extracted
