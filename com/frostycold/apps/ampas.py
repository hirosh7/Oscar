from bs4 import BeautifulSoup
import unicodedata

if __name__ == '__main__':

    s_actor_file = 'data/AMPAS_1927_2014_s_actor.html'
    s_actress_file = 'data/AMPAS_1927_2014_s_actress.html'

    data_files = [s_actor_file, s_actress_file]
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
                        print award_date
                # Get actor and movie
                href_str = a['href']
                target_str = unicodedata.normalize('NFD', a.contents[0]).encode('ascii', 'ignore')
                if href_str.find('BSNominationID=') != -1:
                    actor = target_str
                    print 'Actor: {0} / '.format(actor),
                elif href_str.find('BSFilmID=') != -1:
                    movie = target_str
                    print 'Movie: {0}'.format(movie)
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

    print actor_list
