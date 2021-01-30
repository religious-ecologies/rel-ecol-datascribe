#!/usr/bin/env python3

import csv
import constants
import mysql.connector

conn = mysql.connector.connect(user=constants.MYSQL_USER, password=constants.MYSQL_PASSWORD,
                               host=constants.MYSQL_HOST, database=constants.MYSQL_DATABASE)
cursor = conn.cursor()

select_ds_dataset = ''
select_ds_fields = ''
select_o_item = 'SELECT resource_id FROM value WHERE property_id = %s AND value = %s LIMIT 1'
insert_ds_item = ''
insert_ds_record = ''
insert_ds_value = ''

with open('transcriptions.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for csv_row in reader:
        cursor.execute(select_o_item, (constants.PROPERTY_ID_IMAGE_ORIGINAL_PATH, csv_row['relative_path_to_img']))
        o_value_row = cursor.fetchone()
        if o_value_row is None:
            print('Item not found: {}'.format(csv_row['relative_path_to_img']))
            continue
        print(value_row)
