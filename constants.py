# MySQL config
MYSQL_USER     = 'relectest'
MYSQL_PASSWORD = ''
MYSQL_HOST     = 'localhost'
MYSQL_DATABASE = 'relectest'

USER_ID = 1 # Lincoln Mullen
DATASET_ID = 1 # 1926 Schedules Transcription

# Map from CSV row to Omeka item using unique ID
PROPERTY_ID = 210 # mare:imageOriginalPath

# Map from CSV column to DataScribe field ID
FIELD_MAP = {
    'census_code':                          2,
    'urban_rural_code':                     16,
    'b_division':                           4,
    'c_local_name_of_church':               5,
    'd_city':                               45,
    '01_male_members':                      8,
    '02_female_members':                    9,
    '03_total_members_by_sex':              10,
    '04_members_under_13':                  11,
    '05_members_over_13':                   12,
    '06_total_members_by_age':              13,
    '07_edifices_number':                   14,
    '08_edifices_value':                    15,
    '09_edifices_debt':                     17,
    '10_own_residence':                     18,
    '11_residence_value':                   19,
    '12_residence_debt':                    20,
    '13_expenses':                          21,
    '14_benevolences':                      22,
    '15_total_expenditures':                23,
    '16_ss_officers':                       24,
    '17_ss_scholars':                       25,
    '18_vbs_officers':                      26,
    '19_vbs_scholars':                      27,
    '20_weekday_officers':                  28,
    '21_weekday_scholars':                  29,
    '22_parochial_administrators':          30,
    '23a_parochial_elementary_teachers':    31,
    '23b_parochial_secondary_teachers':     32,
    '24a_parochial_elementary_scholars':    33,
    '24b_parochial_secondary_scholars':     34,
    # 25_pastor_name
    '26_asst_pastors':                      37,
    '27_other_churches':                    38,
    '28_pastor_college':                    39,
    '29_pastor_seminary':                   40,
    '30_asst_college':                      44,
    '31_asst_seminary':                     42,
    'address':                              43,
}

FLAGGED_MAP = {
    'census_code':                          'census_code_flagged',
    'urban_rural_code':                     'urban_rural_flagged',
    'b_division':                           'b_flagged',
    'c_local_name_of_church':               'c_flagged',
    'd_city':                               'd_flagged',
    '01_male_members':                      '01_flagged',
    '02_female_members':                    '02_flagged',
    '03_total_members_by_sex':              '03_flagged',
    '04_members_under_13':                  '04_flagged',
    '05_members_over_13':                   '05_flagged',
    '06_total_members_by_age':              '06_flagged',
    '07_edifices_number':                   '07_flagged',
    '08_edifices_value':                    '08_flagged',
    '09_edifices_debt':                     '09_flagged',
    '10_own_residence':                     '10_flagged',
    '11_residence_value':                   '11_flagged',
    '12_residence_debt':                    '12_flagged',
    '13_expenses':                          '13_flagged',
    '14_benevolences':                      '14_flagged',
    '15_total_expenditures':                '15_flagged',
    '16_ss_officers':                       '16_flagged',
    '17_ss_scholars':                       '17_flagged',
    '18_vbs_officers':                      '18_flagged',
    '19_vbs_scholars':                      '19_flagged',
    '20_weekday_officers':                  '20_flagged',
    '21_weekday_scholars':                  '21_flagged',
    '22_parochial_administrators':          '22_flagged',
    '23a_parochial_elementary_teachers':    '23a_flagged',
    '23b_parochial_secondary_teachers':     '23b_flagged',
    '24a_parochial_elementary_scholars':    '24a_flagged',
    '24b_parochial_secondary_scholars':     '24b_flagged',
    # 25_pastor_name
    '26_asst_pastors':                      '26_flagged',
    '27_other_churches':                    '27_flagged',
    '28_pastor_college':                    '28_flagged',
    '29_pastor_seminary':                   '29_flagged',
    '30_asst_college':                      '30_flagged',
    '31_asst_seminary':                     '31_flagged',
    'address':                              'address_flagged',
}
