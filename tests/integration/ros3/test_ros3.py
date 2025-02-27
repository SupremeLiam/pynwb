from pynwb import NWBHDF5IO
from pynwb.testing import TestCase
import urllib.request
import h5py


class TestRos3Streaming(TestCase):
    """
    Test file access using the HDF5 ros3 driver.

    This test module requires h5py to be built with the ROS3 driver: conda install -c conda-forge h5py
    """
    def setUp(self):
        # Skip ROS3 tests if internet is not available or the ROS3 driver is not installed
        try:
            urllib.request.urlopen('https://dandiarchive.s3.amazonaws.com/ros3test.nwb', timeout=1)
        except urllib.request.URLError:
            self.skipTest("Internet access to DANDI failed. Skipping all Ros3 streaming tests.")
        if 'ros3' not in h5py.registered_drivers():
            self.skipTest("ROS3 driver not installed. Skipping all Ros3 streaming tests.")

    def test_read(self):
        s3_path = 'https://dandiarchive.s3.amazonaws.com/ros3test.nwb'
        with NWBHDF5IO(s3_path, mode='r', driver='ros3') as io:
            nwbfile = io.read()
            test_data = nwbfile.acquisition['ts_name'].data[:]
            self.assertEqual(len(test_data), 3)

    def test_dandi_read(self):
        # this is the NWB Test Data dandiset #000126 sub-1/sub-1.nwb
        s3_path = 'https://dandiarchive.s3.amazonaws.com/blobs/11e/c89/11ec8933-1456-4942-922b-94e5878bb991'

        with NWBHDF5IO(s3_path, mode='r', driver='ros3') as io:
            nwbfile = io.read()
            test_data = nwbfile.acquisition['TestData'].data[:]
            self.assertEqual(len(test_data), 3)
