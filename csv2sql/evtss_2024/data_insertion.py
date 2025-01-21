# data_insertion.py
# This module contains logic for inserting data into the database.

def insert_participant(cursor, data):
    """
    Inserts a participant record into the Participant table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing participant data
    """
    cursor.execute('''INSERT INTO Participant (
        time_submitted, gender, location, hometown, age, education_level, educational_attainment,
        degree_programme, computer_used, computer_specs, os, personal_description, occupation,
        programming_exp_length, prof_programming_exp_length, developer_type, local_cs_it_sentiments,
        ai_dev_use, ai_trust, ai_lawsuit_awareness, oss_license_compliance, survey_length_opinion,
        survey_difficulty, survey_comment, event_location_suggestions, message_for_dev8,
        message_for_partners, programming_fuel
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['time_submitted'], data['gender'], data['location'], data['hometown'], data['age'],
        data['education_level'], data['educational_attainment'], data['degree_programme'],
        data['computer_used'], data['computer_specs'], data['os'], data['personal_description'],
        data['occupation'], data['programming_exp_length'], data['prof_programming_exp_length'],
        data['developer_type'], data['local_cs_it_sentiments'], data['ai_dev_use'], data['ai_trust'],
        data['ai_lawsuit_awareness'], data['oss_license_compliance'], data['survey_length_opinion'],
        data['survey_difficulty'], data['survey_comment'], data['event_location_suggestions'],
        data['message_for_dev8'], data['message_for_partners'], data['programming_fuel']
    ))

def insert_work_arrangement(cursor, data):
    """
    Inserts a work arrangement record into the WorkArrangement table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing work arrangement data
    """
    cursor.execute('''INSERT INTO WorkArrangement (
        participant_id, sector, employer_location, employment_arrangement,
        average_monthly_income_range, income_satisfaction
    ) VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data['participant_id'], data['sector'], data['employer_location'],
        data['employment_arrangement'], data['average_monthly_income_range'],
        data['income_satisfaction']
    ))

def insert_developer_activity(cursor, data):
    """
    Inserts a developer activity record into the DeveloperActivity table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing developer activity data
    """
    cursor.execute('''INSERT INTO DeveloperActivity (
        participant_id, activity
    ) VALUES (?, ?)
    ''', (
        data['participant_id'], data['activity']
    ))

def insert_programming_language(cursor, data):
    """
    Inserts a programming language record into the ProgrammingLanguage table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing programming language data
    """
    cursor.execute('''INSERT INTO ProgrammingLanguage (
        participant_id, name, did_not_like_using, used, want_to_use_next_year, is_primary_language
    ) VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data['participant_id'], data['name'], data['did_not_like_using'],
        data['used'], data['want_to_use_next_year'], data['is_primary_language']
    ))

def insert_software_category(cursor, data):
    """
    Inserts a software category record into the SoftwareCategory table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing software category data
    """
    cursor.execute('''INSERT INTO SoftwareCategory (
        participant_id, name
    ) VALUES (?, ?)
    ''', (
        data['participant_id'], data['name']
    ))

def insert_platform(cursor, data):
    """
    Inserts a platform record into the Platform table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing platform data
    """
    cursor.execute('''INSERT INTO Platform (
        participant_id, name
    ) VALUES (?, ?)
    ''', (
        data['participant_id'], data['name']
    ))

def insert_library(cursor, data):
    """
    Inserts a library record into the Library table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing library data
    """
    cursor.execute('''INSERT INTO Library (
        participant_id, name, did_not_like_using, used, want_to_use_next_year
    ) VALUES (?, ?, ?, ?, ?)
    ''', (
        data['participant_id'], data['name'], data['did_not_like_using'],
        data['used'], data['want_to_use_next_year']
    ))

def insert_coding_editor(cursor, data):
    """
    Inserts a coding editor record into the CodingEditor table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing coding editor data
    """
    cursor.execute('''INSERT INTO CodingEditor (
        participant_id, name, did_not_like_using, used, want_to_use_next_year
    ) VALUES (?, ?, ?, ?, ?)
    ''', (
        data['participant_id'], data['name'], data['did_not_like_using'],
        data['used'], data['want_to_use_next_year']
    ))

def insert_tool(cursor, data):
    """
    Inserts a tool record into the Tool table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing tool data
    """
    cursor.execute('''INSERT INTO Tool (
        participant_id, name, did_not_like_using, used, want_to_use_next_year
    ) VALUES (?, ?, ?, ?, ?)
    ''', (
        data['participant_id'], data['name'], data['did_not_like_using'],
        data['used'], data['want_to_use_next_year']
    ))

def insert_database(cursor, data):
    """
    Inserts a database record into the Database table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing database data
    """
    cursor.execute('''INSERT INTO Database (
        participant_id, name, did_not_like_using, used, want_to_use_next_year
    ) VALUES (?, ?, ?, ?, ?)
    ''', (
        data['participant_id'], data['name'], data['did_not_like_using'],
        data['used'], data['want_to_use_next_year']
    ))

def insert_cloud_platform(cursor, data):
    """
    Inserts a cloud platform record into the CloudPlatform table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing cloud platform data
    """
    cursor.execute('''INSERT INTO CloudPlatform (
        participant_id, name, did_not_like_using, used, want_to_use_next_year
    ) VALUES (?, ?, ?, ?, ?)
    ''', (
        data['participant_id'], data['name'], data['did_not_like_using'],
        data['used'], data['want_to_use_next_year']
    ))

def insert_code_platform(cursor, data):
    """
    Inserts a code platform record into the CodePlatform table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing code platform data
    """
    cursor.execute('''INSERT INTO CodePlatform (
        participant_id, name, did_not_like_using, used, want_to_use_next_year
    ) VALUES (?, ?, ?, ?, ?)
    ''', (
        data['participant_id'], data['name'], data['did_not_like_using'],
        data['used'], data['want_to_use_next_year']
    ))

def insert_work_management_tool(cursor, data):
    """
    Inserts a work management tool record into the WorkManagementTool table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing work management tool data
    """
    cursor.execute('''INSERT INTO WorkManagementTool (
        participant_id, name, did_not_like_using, used, want_to_use_next_year
    ) VALUES (?, ?, ?, ?, ?)
    ''', (
        data['participant_id'], data['name'], data['did_not_like_using'],
        data['used'], data['want_to_use_next_year']
    ))

def insert_communication_tool(cursor, data):
    """
    Inserts a communication tool record into the CommunicationTool table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing communication tool data
    """
    cursor.execute('''INSERT INTO CommunicationTool (
        participant_id, name, did_not_like_using, used, want_to_use_next_year
    ) VALUES (?, ?, ?, ?, ?)
    ''', (
        data['participant_id'], data['name'], data['did_not_like_using'],
        data['used'], data['want_to_use_next_year']
    ))

def insert_ai_usage(cursor, data):
    """
    Inserts an AI usage record into the AIUsage table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing AI usage data
    """
    cursor.execute('''INSERT INTO AIUsage (
        participant_id, name, did_not_like_using, used, want_to_use_next_year
    ) VALUES (?, ?, ?, ?, ?)
    ''', (
        data['participant_id'], data['name'], data['did_not_like_using'],
        data['used'], data['want_to_use_next_year']
    ))

def insert_ai_ethical_issue(cursor, data):
    """
    Inserts an AI ethical issue record into the AIEthicalIssue table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing AI ethical issue data
    """
    cursor.execute('''INSERT INTO AIEthicalIssue (
        participant_id, name
    ) VALUES (?, ?)
    ''', (
        data['participant_id'], data['name']
    ))

def insert_tech_event_category(cursor, data):
    """
    Inserts a tech event category record into the TechEventCategory table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing tech event category data
    """
    cursor.execute('''INSERT INTO TechEventCategory (
        participant_id, name
    ) VALUES (?, ?)
    ''', (
        data['participant_id'], data['name']
    ))

def insert_tech_event_topic(cursor, data):
    """
    Inserts a tech event topic record into the TechEventTopic table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing tech event topic data
    """
    cursor.execute('''INSERT INTO TechEventTopic (
        participant_id, name
    ) VALUES (?, ?)
    ''', (
        data['participant_id'], data['name']
    ))

def insert_tech_event_consumable(cursor, data):
    """
    Inserts a tech event consumable record into the TechEventConsumable table.

    :param cursor: SQLite database cursor
    :param data: Dictionary containing tech event consumable data
    """
    cursor.execute('''INSERT INTO TechEventConsumable (
        participant_id, name
    ) VALUES (?, ?)
    ''', (
        data['participant_id'], data['name']
    ))
# End of Selection
