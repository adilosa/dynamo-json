[![Build](https://travis-ci.org/adilosa/dynamo-json.svg?branch=master)]()

# dynamo-json

Sick of DynamoDB using its own data type descriptors? Swap between DynamoDB and normal JSON!

```python
import dynamo_json

dynamo_json.marshall({"some": ["json", "document"]})

# {"M": {"some": {"L": [{"S": "json"}, {"S": "document"}]}}}

dynamo_json.unmarshall({"M": {"some": {"L": [{"S": "json"}, {"S": "document"}]}}})

# {"some": ["json", "document"]}
```

## Installation

Install from PyPI via `pip`:

    pip install dynamo_json
