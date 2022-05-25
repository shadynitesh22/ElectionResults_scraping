import csv

from bs4 import BeautifulSoup
import requests


def ktm_voters_list():
    """
    This Function scrapes BBC website to get the latest news form
    the web.

    """
    source = requests.get('https://election.ekantipur.com/pradesh-3/district-kathmandu/kathmandu?lng=eng').text

    soup = BeautifulSoup(source, 'lxml')
    try:
        csv_file = open('election_ktm.csv', 'w')

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Name', 'Party Name', 'Votes', 'Image url'])

        for name_ in soup.find_all('div', class_="candidate-list"):
            candidate_name = name_.find('div', class_='candidate-name')
            party_name = name_.find('div', class_='candidate-party-name')
            vote_numbers = name_.find('div', class_='vote-numbers')
            img_source = name_.find('div', class_='candidate-img')
            img_url = img_source.img['src']

            print(f'{candidate_name.text} with the party_name {party_name.text} with votes {vote_numbers.text} with '
                  f'the image url {img_url}')
            csv_writer.writerow([candidate_name.text, party_name.text, vote_numbers.text, img_url])
        csv_file.close()

    except:
        Exception(IOError)


# input(__prompt="let's view scraped data ")
ktm_voters_list()


def scrape_elections_results():
    """
    This Function will scrape the internet with the use of
    google search engine to find all news and information
    regarding local election
    The webpage we are going scrape first : https://election.ekantipur.com/pradesh-3/district-kathmandu/kathmandu?lng=eng
    these results will be compared and scraped with other websites.

    """
    source = requests.get('https://election.ekantipur.com/?lng=eng').text

    soup = BeautifulSoup(source, 'lxml')
    try:
        csv_file = open('election_results.csv', 'w')

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Party Name', 'Wins', 'Image url'])

        for name_ in soup.find_all('div', class_="row gx-2 py-2"):
            party_name = name_.find('div', class_='party-name mb-2')

            remaing_names = party_name
            print(f'Name of the party \n{remaing_names.text}\n')

            vote_numbers = name_.find('div', class_='number-display')
            print(vote_numbers.text)
            img_source = name_.find('div', class_='election-icon')
            img_url = img_source.img['src']
            print(img_url)

            # print(f'{title_.text} with the party_name {party_name.text}  '
            #       f'the image url {img_url.txt} ', )
            csv_writer.writerow([remaing_names.text, vote_numbers.text, img_url])
        csv_file.close()



    except:
        Exception(IOError)


scrape_elections_results()


def scrape_top_2():
    source = requests.get('https://election.ekantipur.com/?lng=eng').text

    soup = BeautifulSoup(source, 'lxml')
    try:
        csv_files = open('election_compare.csv', 'w')

        csv_writer = csv.writer(csv_files)
        csv_writer.writerow(['City', 'CandidateName', 'Party', 'votes', 'image'])
        for top2 in soup.find_all('div', class_="tab-pane fade show active"):
            city = top2.find('div', class_='card-header-label')
            city_label = city.a
            city_links = city.a['href']
            candidate_list = top2.find_all('div', class_='candidate-list')
            img = candidate_list.find('div', class_='candidate-img-wrapper')
            img_url = img.div['url']
            name = candidate_list.find('div', class_='candidate-name')
            party = candidate_list.find('div', class_='candidate-party')
            votes = candidate_list.find('div', class_='vote-numbers')
            print(f"{city_label.text} --candidateName {name.text} --Party {party.text}--votes {votes.text}"
                  f"--Image{img_url.text}"
                  "")
            csv_writer.writerow([city_label.text, name.text, party.text, votes.text, img_url.text])
        csv_files.close()

    except:
        Exception(IOError)


scrape_top_2()
