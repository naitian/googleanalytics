from ..dataset import Dataset


class TestDataset:
    def test_init(self):
        data = Dataset(debug=True)
        assert(len(data.train) == 1000)
        assert(len(data.train.columns) == 63)
        assert(len(data.test) == 901)
        assert(len(data.test.columns) == 63)
