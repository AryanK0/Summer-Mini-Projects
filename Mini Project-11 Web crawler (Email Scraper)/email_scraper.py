import re
# import requests
# from bs4 import BeautifulSoup

def scrape_emails(url):
    print(f'Scraping {url} for emails...')
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # text = soup.get_text()
    text = 'Contact us at admin@example.com or support@example.org'
    emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text))
    return emails

if __name__ == '__main__':
    print('Found emails:', scrape_emails('http://example.com'))