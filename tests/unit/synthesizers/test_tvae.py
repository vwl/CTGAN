from unittest import TestCase
from ctgan.synthesizers import TVAESynthesizer

class TestTVAESynthesizer(TestCase):

    def test_continuous(self):
        """Test training the TVAE synthesizer on a small continuous dataset."""
        # verify that the distribution of the samples is close to the distribution of the data
        # using a kstest.
        pass

    def test_categorical(self):
        """Test training the TVAE synthesizer on a small categorical dataset."""
        # verify that the distribution of the samples is close to the distribution of the data
        # using a cstest.
        pass

    def test_mixed(self):
        """Test training the TVAE synthesizer on a small mixed-type dataset."""
        # verify that the distribution of the samples is close to the distribution of the data
        # using a kstest for continuous + a cstest for categorical.
        pass

