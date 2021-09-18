from flask import Flask, request

from argparse import ArgumentParser
from math import floor
import os
import random
import uuid
import urllib.parse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction

from models import User


app = Flask(__name__)

@app.route('/')
def home():
    print("home")
    return "home"

def create_user(session):
    session.add_all(User(1, "aa", 20))

def parse_cmdline():
    parser = ArgumentParser()
    parser.add_argument("url", help="Enter your node\'s connection string\n")
    opt = parser.parse_args()
    return opt


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    opt = parse_cmdline()
    conn_string = opt.url
    # For cockroach demo:
    # postgres://demo:<demo_password>@127.0.0.1:26257?sslmode=require
    # For CockroachCloud:
    # postgres://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>
    try:
        db_uri = os.path.expandvars(conn_string)
        db_uri = urllib.parse.unquote(db_uri)

        psycopg_uri = db_uri.replace(
            'postgresql://', 'cockroachdb://').replace(
            'postgres://', 'cockroachdb://').replace(
            '26257?', '26257/defaultdb?')
        # The "cockroachdb://" prefix for the engine URL indicates that we are
        # connecting to CockroachDB using the 'cockroachdb' dialect.
        # For more information, see
        # https://github.com/cockroachdb/sqlalchemy-cockroachdb.
        engine = create_engine(psycopg_uri)
    except Exception as e:
        print('Failed to connect to database.')
        print('{0}'.format(e))

    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_user(s))
    app.run()

