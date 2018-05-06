import json
import click
import dynamo_json as dj


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("json_document")
def dynamo_json(json_document):
    """Convert between Dynamo JSON and standard JSON"""
    document = json.loads(json_document)
    try:
        converted = dj.unmarshall(document)
    except:
        converted = dj.marshall(document)
    click.echo(json.dumps(converted))


if __name__ == "__main__":
    dynamo_json()
