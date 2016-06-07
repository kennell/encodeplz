# General
DEBUG = True



# Broker settings.
BROKER_URL = 'redis://localhost:6379/0'

# Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

# Set Serializers
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Set timezone to UTC
CELERY_TIMEZONE = 'UTC'