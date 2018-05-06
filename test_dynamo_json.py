import unittest

from dynamo_json import marshall, unmarshall


class TestDynamoJson(unittest.TestCase):
    def test_marshalls_json(self):
        self.assertEqual(marshall({"foo": "bar"}), {"foo": {"S": "bar"}})

    def test_unmarshalls_json(self):
        self.assertEqual(unmarshall({"foo": {"S": "bar"}}), {"foo": "bar"})

    def test_marshall_unmarshall_identity(self):
        data = {
            "menu": {
                "id": "file",
                "value": "File",
                "popup": {
                    "menuitem": [
                        {"value": "New", "onclick": "CreateNewDoc()"},
                        {"value": "Open", "onclick": "OpenDoc()"},
                        {"value": "Close", "onclick": "CloseDoc()"}
                    ]
                }
            }
        }
        self.assertEqual(unmarshall(marshall(data)), data)

    def test_unmarshall_marshall_identity(self):
        data = {
            "Age": {"N": "8"},
            "Colors": {
                "L": [
                    {"S": "White"},
                    {"S": "Brown"},
                    {"S": "Black"}
                ]
            },
            "Name": {"S": "Fido"},
            "Vaccinations": {
                "M": {
                    "Rabies": {
                        "L": [
                            {"S": "2009-03-17"},
                            {"S": "2011-09-21"},
                            {"S": "2014-07-08"}
                        ]
                    },
                    "Distemper": {"S": "2015-10-13"}
                }
            },
            "Breed": {"S": "Beagle"},
            "AnimalType": {"S": "Dog"}
        }
        self.assertEqual(unmarshall(marshall(data)), data)

