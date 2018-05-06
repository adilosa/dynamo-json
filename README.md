[![Build](https://travis-ci.org/adilosa/dynamo-json.svg?branch=master)]()

# dynamo-json

Sick of DynamoDB using its own data type descriptors? Swap between DynamoDB and normal JSON!

## Installation

Install from PyPI via `pip`:

    pip install dynamo_json

## Usage

Use as a library

```python
import dynamo_json

dynamo_json.marshall({"some": ["json", "document"]})

# {"some": {"L": [{"S": "json"}, {"S": "document"}]}}

dynamo_json.unmarshall({"some": {"L": [{"S": "json"}, {"S": "document"}]}})

# {"some": ["json", "document"]}
```

or as a CLI tool

```
$ dynamo-json '{"my": "json"}'
{"my": {"S": "json"}}

$ dynamo-json '{"my": {"S": "dynamo-json"}}'
{"my": "dynamo-json"}
```
