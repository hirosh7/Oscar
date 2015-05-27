from bs4 import BeautifulSoup
import unicodedata


def build_actor_list(data_files):

    """
    Build a list of dictionary entries for each actor/actress parsed from data files
    Dictionary entries are formatted as {year: award year, actor: actor name, movie: movie name}
    :param data_files: html data files containing Academy Award actor/actress award winners
    :return: list of actor/actress dictionary entries (List)
    """

    empty_dict = {}
    actor_entry = {}
    actor_list = []
    target_found = False
    award_date = ''
    actor = ''
    movie = ''

    for data_file in data_files:

        # Soupify data file and get all <a href references
        soup = BeautifulSoup(open(data_file))
        all_a = soup.findAll('a')

        # Step through all the references and extract movie date, movie title and actor
        for a in all_a:
            if a.get('href'):
                if a.get('class'):
                    # Get award date
                    if a['class'][0] == 'awardYearHeader':
                        date_str = a.contents[0]
                        award_date = date_str.split(' ')[0]
                # Get actor and movie
                href_str = a['href']
                target_str = unicodedata.normalize('NFD', a.contents[0]).encode('ascii', 'ignore')
                if href_str.find('BSNominationID=') != -1:
                    actor = target_str
                elif href_str.find('BSFilmID=') != -1:
                    movie = target_str
                    target_found = True

            if target_found:
                actor_entry['year'] = award_date
                actor_entry['actor'] = actor
                actor_entry['movie'] = movie

                # Add entry to actor list
                actor_list.append(actor_entry)

                # reset entry
                actor_entry = empty_dict.copy()
                target_found = False

    return actor_list
