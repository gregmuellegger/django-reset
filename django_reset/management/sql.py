from django.core.management.sql import sql_delete, sql_all

def sql_reset(app, style, connection):
    "Returns a list of the DROP TABLE SQL, then the CREATE TABLE SQL, for the given module."
    return sql_delete(app, style, connection) + sql_all(app, style, connection)
