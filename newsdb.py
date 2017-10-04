#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def query_one():
    """Return relevant queries from the database."""
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute("SELECT SUBSTRING(path, 10), COUNT(*) \
        FROM log \
        WHERE path LIKE '/article/%' \
        GROUP BY path \
        ORDER BY count DESC \
        LIMIT 3;")
    rows = cur.fetchall()
    print("Top Three Articles:")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

query_one()
