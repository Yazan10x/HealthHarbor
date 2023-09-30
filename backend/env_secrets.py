"""
Load All Secrets
"""
import json
import os


def load_secrets() -> None:
    if os.environ.get('Comment') is None:

        with open('secrets.json') as s:
            secret_json = json.load(s)
            os.environ.setdefault('DB_URI', secret_json.get('DB_URI'))
            os.environ.setdefault('COHERE_API_KEY', secret_json.get('COHERE_API_KEY'))


if __name__ == '__main__':

    load_secrets()
