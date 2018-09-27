#!/usr/bin/env python

# By: Anup Mishra (anupmishratech@gmail.com)

"""This code tests topic_model() from topic_model.py

Example usage:
    python test_topic_model.py

"""


import unittest
import topic_model


class TestTopicModel(unittest.TestCase):
    def test_topic_model(self):
        topic_list = topic_model.topic_model("resources/document_embc_2015.txt", 5)
        assert topic_list is not None


if __name__ == '__main__':
    unittest.main()
