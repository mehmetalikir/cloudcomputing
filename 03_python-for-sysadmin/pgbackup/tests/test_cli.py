import pytest
from pgbackup import cli

url = "postgres://cloud_user@13.236.85.136/db_one"

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    '''
    Witout a specified driver the parser will exit
    '''
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_driver(parser):
    '''
    The parser will exit if it receives a driver without a destination
    '''
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_parser_with_driver(parser):
    '''
    The parser will not exit if the driver bame is know
    '''
    for driver in ['local', 'azure']:
        assert parser.parse_args([url, '--driver',driver,'destination'])

def test_parser_with_driver_and_destination(parser):
    '''
    The parser will not exit if it receives a driver and destination
    '''
    args = parser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.url == url
    assert args.driver == 'local'
    assert args.destination == '/some/path'
    