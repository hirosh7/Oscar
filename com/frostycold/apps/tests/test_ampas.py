from unittest import TestCase
import com.frostycold.apps.ampas as ampas


class TestAmpas(TestCase):
    def test_build_actor_list(self):

        data_files = ['data/AMPAS_1927_2014_s_actor.html']
        actor_list = ampas.build_actor_list(data_files)
        self.assertEqual(len(actor_list), 79)
        self.assertEqual(actor_list[0]['actor'], 'Walter Brennan')
        self.assertEqual(actor_list[0]['movie'], 'Come and Get It')
        self.assertEqual(actor_list[0]['year'], '1936')
