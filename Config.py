import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', '6435225'))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', '4e984ea35f854762dcde906dce426c2d')
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '5335343977:AAFzt2TBZ7fiVo1sG1pBNhbjjjF6GHECVPE')
    DATABASE_URL = os.environ.get('DATABASE_URL', "postgres://xcgmuzrq:uMhAxXtJgmVPqLav7Y37LFQ9wAqKd8CT@isilo.db.elephantsql.com/xcgmuzrq")
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', 'TheUpdatesChannel')
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
