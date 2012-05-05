# Settings to be used when running unit tests
# python manage.py test --settings=processor.test_settings processor

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TEMPLATE_CONTEXT_PROCESSORS = (
    'contextProcessor.context_processor.django_settings',
)

INSTALLED_APPS = (
    # Put any other apps that your app depends on here
    'contextProcessor',
)
SITE_ID = 1

TEST_SETTING = ( 123, )
SOME_SETTING = ( 321, )
# This merely needs to be present - as long as your test case specifies a
# urls attribute, it does not need to be populated.
ROOT_URLCONF = ''

