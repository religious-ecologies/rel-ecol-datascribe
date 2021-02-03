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
insert_ds_record = 'INSERT INTO datascribe_record (item_id, owner_id, created_by_id, created, position) VALUES (%s, %s, %s, %s, %s)'
insert_ds_value = 'INSERT INTO datascribe_value (field_id, record_id, is_missing, is_illegible, text) VALUES (%s, %s, %s, %s, %s)'

with open('transcriptions.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for csv_row in reader:
        # Get the corresponding Omeka item.
        cursor.execute(select_o_item, (constants.PROPERTY_ID, csv_row['relative_path_to_img']))
        o_item_row = cursor.fetchone()
        if o_item_row is None:
            print('Item not found: {}'.format(csv_row['relative_path_to_img']))
            continue
        o_item_id = o_item_row[0]
        # Create the DataScribe item.
        cursor.execute(insert_ds_item, (constants.DATASET_ID, o_item_id, constants.USER_ID, datetime.now()))
        ds_item_id = cursor.lastrowid
        # Create the DataScribe record.
        cursor.execute(insert_ds_record, (ds_item_id, constants.USER_ID, constants.USER_ID, datetime.now(), 1))
        ds_record_id = cursor.lastrowid
        # Create the DataScribe values.
        for csv_column, ds_field_id in constants.FIELD_MAP.items():
            text = csv_row[csv_column]
            is_missing = 0
            is_illegible = 0
            if text == 'NA' or text == '':
                # "NA" or empty string means the text is null
                text = None
                if csv_row[constants.FLAGGED_MAP[csv_column]] != 'TRUE':
                    # Anything not "TRUE" in the flagged column means the text is missing
                    is_missing = 1
            if csv_row[constants.FLAGGED_MAP[csv_column]] == 'TRUE':
                # "TRUE" in the flagged column means the text is illegible
                is_illegible = 1
            # Handle special cases.
            if csv_column == 'urban_rural_code':
                if csv_row['urban_rural_code'] == 'R':
                    text = 'Rural'
                elif csv_row['urban_rural_code'] == 'U':
                    text = 'Urban'
            if csv_column == '10_own_residence':
                if csv_row['10_own_residence'] == 'TRUE':
                    text = 'Yes'
                elif csv_row['10_own_residence'] == 'FALSE':
                    text = 'No'
            if csv_column == '25a_has_pastor':
                if csv_row['25a_has_pastor'] == 'TRUE':
                    text = 'Yes'
                elif csv_row['25a_has_pastor'] == 'FALSE':
                    text = 'No'
            cursor.execute(insert_ds_value, (ds_field_id, ds_record_id, is_missing, is_illegible, text))
    conn.commit()
