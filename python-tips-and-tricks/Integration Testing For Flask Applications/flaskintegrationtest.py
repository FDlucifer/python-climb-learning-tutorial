import io
import unittest
import pandas as pd
from app import app

class flaskintegrationtestcase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_add_remove_todos_and_download_excel(self):
        for i in range(1, 6):
            self.client.post('/add', data={
                'todo': f'todo {i}'
            })

        self.client.get('/remove/2')

        response = self.client.get('/download_todos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        with io.BytesIO(response.data) as buffer:
            df = pd.read_excel(buffer)

            self.assertListEqual(['todo 1', 'todo 2', 'todo 3', 'todo 4'], df.todo.values.tolist())


