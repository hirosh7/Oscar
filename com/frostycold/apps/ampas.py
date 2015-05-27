from bs4 import BeautifulSoup

s_actor_file = 'data/AMPAS_1934_2014_s_actor.html'
s_actress_file = 'AMPAS_1934_2014_s_actress.html'

soup = BeautifulSoup(open(s_actor_file))
all_a = soup.findAll('a')

empty_dict = {}
actor_entry = {}
actor_list = []
target_found = False
award_date = ''
actor = ''
movie = ''

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
        target_str = a.contents[0]
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
