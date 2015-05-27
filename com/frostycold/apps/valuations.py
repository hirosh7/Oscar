import ampas

if __name__ == '__main__':

    s_actor_file = 'data/AMPAS_1927_2014_s_actor.html'
    s_actress_file = 'data/AMPAS_1927_2014_s_actress.html'

    data_files = [s_actor_file, s_actress_file]

    actor_data = ampas.build_actor_list(data_files)

    print actor_data
