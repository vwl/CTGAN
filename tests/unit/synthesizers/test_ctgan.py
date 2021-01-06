from unittest import TestCase
from ctgan.synthesizers import CTGANSynthesizer

class TestCTGANSynthesizer(TestCase):

    def test_continuous(self):
        """Test training the CTGAN synthesizer on a continuous dataset."""
        # assert the distribution of the samples is close to the distribution of the data
        # using kstest:
        #   - uniform (assert p-value > 0.05)
        #   - gaussian (assert p-value > 0.05)
        #   - inversely correlated (assert correlation < 0)
        pass

    def test_categorical(self):
        """Test training the CTGAN synthesizer on a categorical dataset."""
        # assert the distribution of the samples is close to the distribution of the data
        # using cstest:
        #   - uniform (assert p-value > 0.05)
        #   - very skewed / biased? (assert p-value > 0.05)
        #   - inversely correlated (assert correlation < 0)
        pass

    def test_categorical_log_frequency(self):
        """Test training the CTGAN synthesizer on a small categorical dataset."""
        # assert the distribution of the samples is close to the distribution of the data
        # using cstest:
        #   - uniform (assert p-value > 0.05)
        #   - very skewed / biased? (assert p-value > 0.05)
        #   - inversely correlated (assert correlation < 0)
        pass

    def test_mixed(self):
        """Test training the CTGAN synthesizer on a small mixed-type dataset."""
        # assert the distribution of the samples is close to the distribution of the data
        # using a kstest for continuous + a cstest for categorical.
        pass

    def test_conditional(self):
        """Test training the CTGAN synthesizer and sampling conditioned on a categorical."""
        # verify that conditioning increases the likelihood of getting a sample with the specified
        # categorical value
        pass

    def test_batch_size_pack_size(self):
        """Test that if batch size is not a multiple of pack size, it raises a sane error."""
        pass
