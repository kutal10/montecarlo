import unittest
import os
from nvidia import *


class Tests(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(os.path.exists(file_name))

    def test_file_not_empty(self):
        df = pd.read_csv(file_name)
        self.assertFalse(df.empty)

    def test_data_length(self):
        # data length to be checked so that pct change can be calculated
        self.assertTrue(len(data) > 1)

    def test_log_return_length(self):
        self.assertEqual(len(data), len(log_returns))

    def test_mean_is_float(self):
        self.assertTrue(type(u[0]) == np.float64)

    def test_var_is_float(self):
        self.assertTrue(type(var[0]) == np.float64)

    def test_drift_is_float(self):
        self.assertTrue(type(drift[0]) == np.float64)

    def test_stdev_is_float(self):
        self.assertTrue(type(stdev[0]) == np.float64)

    def test_daily_returns_lengths(self):
        self.assertEqual(len(daily_returns),t_intervals)

        for i in range(t_intervals):
            self.assertEqual(len(daily_returns[i]),iterations)