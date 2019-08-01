from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def get_poems(author_name):
     # name of the poet
    poet_name = author_name
    # get raw html
    raw_html = simple_get('https://poets.org/poems/'+poet_name)
    # clean it up with Beautiful Soup
    clean_html = BeautifulSoup(raw_html, "html.parser")

    # find all links to this poet's poems
    my_links = clean_html.findAll('a')
    good_links = []
    for link in my_links:
        if link.has_attr("href"):
            if "/poem/" in link['href']:
                # print(link['href'])
                good_links.append(link['href'])
    
    # create links to the poems
    start_link = "https://poets.org"
    poem_links = []
    for good_link in good_links:
        poem_links.append(start_link + good_link)
    # for link in poem_links:
        # print(link)
    
    # get html from each link, parse it, store the poem
    poem_list = []
    for poem_link in poem_links:
        raw_poem_html = simple_get(poem_link)
        clean_poem_html = BeautifulSoup(raw_poem_html, "html.parser")
        my_para = clean_poem_html.findAll('div', 'card-body') 
        if len(my_para) > 0:
            poem = my_para[0].text
            # print(poem)
            poem_list.append(poem)
    
    # create file and write poems into it
    text_file = open("trainingPoems/" + poet_name + "-poems.txt", "w+")
    for poem in poem_list:
        text_file.write(poem.encode('utf-8'))
    text_file.close()

if __name__ == "__main__":
    get_poems("robert-frost")
    