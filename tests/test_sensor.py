import os
import sensor
import tempfile
import unittest

class SensorTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, sensor.app.config['DATABASE'] = tempfile.mkstemp()
        sensor.app.testing = True
        self.app = sensor.app.test_client()
        with sensor.app.app_context():
            sensor.init_db()
    
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(sensor.app.config['DATABASE'])
    
    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'No entries' in rv.data
    
if __name__ = '__main__':
    unittest.main()
