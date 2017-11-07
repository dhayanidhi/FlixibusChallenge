from mock import patch
from src.starter import get_sorted_result

class TestStarter(object):

    def random_sort_by_id_model(stream_list):
        ids = [obj.id for obj in stream_list]
        ids.sort(reverse=True)
        return ids

    def get_dummy_list(self):
        random_ids = [10,95,62,52,73,97,19,71,32,2,39]
        return [dict(id=id, feature1="dummy", feature2="dummy2") for id in random_ids]

    @patch("src.starter.execute_model", side_effect=random_sort_by_id_model)
    def test_sort_random_model(self, model_mock):
        fixture = self.get_dummy_list()
        output = get_sorted_result(fixture)
        assert output==[97, 95, 73, 71, 62, 52, 39, 32, 19, 10, 2]


