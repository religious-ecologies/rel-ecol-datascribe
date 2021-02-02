#!/usr/bin/env python3

import csv
import constants
from datetime import datetime
import mysql.connector

conn = mysql.connector.connect(user=constants.MYSQL_USER, password=constants.MYSQL_PASSWORD,
                               host=constants.MYSQL_HOST, database=constants.MYSQL_DATABASE)
cursor = conn.cursor()

select_o_item = 'SELECT resource_id FROM value WHERE property_id = %s AND value = %s LIMIT 1'
insert_ds_item = 'INSERT INTO datascribe_item (dataset_id, item_id, synced_by_id, synced) VALUES (%s, %s, %s, %s)'
insert_ds_record = 'INSERT INTO datascribe_record (item_id, owner_id, created_by_id, created) VALUES (%s, %s, %s, %s)'
insert_ds_value = 'INSERT INTO datascribe_value (field_id, record_id, text) VALUES (%s, %s, %s)'

with open('transcriptions.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for csv_row in reader:
        # Get corresponding Omeka item.
        cursor.execute(select_o_item, (constants.PROPERTY_ID_IMAGE_ORIGINAL_PATH, csv_row['relative_path_to_img']))
        o_item_row = cursor.fetchone()
        if o_item_row is None:
            print('Item not found: {}'.format(csv_row['relative_path_to_img']))
            continue
        o_item_id = o_item_row[0]
        # Create DataScribe item.
        cursor.execute(insert_ds_item, (constants.DATASET_ID, o_item_id, constants.USER_ID, datetime.now()))
        ds_item_id = cursor.lastrowid
        # Create DataScribe record.
        cursor.execute(insert_ds_record, (ds_item_id, constants.USER_ID, constants.USER_ID, datetime.now()))
        ds_record_id = cursor.lastrowid
        # Create DataScribe values.
        for csv_column, ds_field_id in constants.FIELDS.items():
            cursor.execute(insert_ds_value, (ds_field_id, ds_record_id, cv_row[csv_column]))
    conn.commit()
