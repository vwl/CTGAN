from unittest import TestCase
from ctgan.data_transformer import DataTransformer

class TestDataTransformer(TestCase):

    def test_constant(self):
        """Test transforming a dataframe containing constant values."""
        pass

    def test_df_continuous(self):
        """Test transforming a dataframe containing only continuous values."""
        # validate output ranges [0, 1]
        # validate output shape (# samples, # output dims)
        # validate that forward transform is **not** deterministic
        # make sure it can be inverted
        pass

    def test_df_categorical(self):
        """Test transforming a dataframe containing only categorical values."""
        # validate output ranges [0, 1]
        # validate output shape (# samples, # output dims)
        # validate that forward transform is deterministic
        # make sure it can be inverted
        pass

    def test_df_mixed(self):
        """Test transforming a dataframe containing mixed data types."""
        pass

    def test_df_mixed_nan(self):
        """Test transforming a dataframe containing mixed data types + NaN for categoricals."""
        pass

    def test_np_continuous(self):
        """Test transforming a np.array containing only continuous values."""
        pass

    def test_np_categorical(self):
        """Test transforming a np.array containing only categorical values."""
        pass

    def test_np_mixed(self):
        """Test transforming a np.array containing mixed data types."""
        pass
