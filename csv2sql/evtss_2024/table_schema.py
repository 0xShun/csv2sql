def create_tables(cursor):
    """
    Creates all tables in the database based on the ER model.

    :param cursor: SQLite database cursor
    """
    cursor.execute('''CREATE TABLE IF NOT EXISTS Participant (
        id INTEGER PRIMARY KEY,
        time_submitted TEXT,
        gender TEXT,
        location TEXT,
        hometown TEXT,
        age INTEGER,
        education_level TEXT,
        educational_attainment TEXT,
        degree_programme TEXT,
        computer_used TEXT,
        computer_specs TEXT,
        os TEXT,
        personal_description TEXT,
        occupation TEXT,
        programming_exp_length INTEGER,
        prof_programming_exp_length INTEGER,
        developer_type TEXT,
        local_cs_it_sentiments TEXT,
        ai_dev_use TEXT,
        ai_trust TEXT,
        ai_lawsuit_awareness TEXT,
        oss_license_compliance TEXT,
        survey_length_opinion TEXT,
        survey_difficulty TEXT,
        survey_comment TEXT,
        event_location_suggestions TEXT,
        message_for_dev8 TEXT,
        message_for_partners TEXT,
        programming_fuel TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS WorkArrangement (
        participant_id INTEGER PRIMARY KEY,
        sector TEXT,
        employer_location TEXT,
        employment_arrangement TEXT,
        average_monthly_income_range TEXT,
        income_satisfaction TEXT,
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS DeveloperActivity (
        participant_id INTEGER,
        activity TEXT,
        PRIMARY KEY(participant_id, activity),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ProgrammingLanguage (
        participant_id INTEGER,
        name TEXT,
        did_not_like_using TEXT,
        used TEXT,
        want_to_use_next_year TEXT,
        is_primary_language TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS SoftwareCategory (
        participant_id INTEGER,
        name TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Platform (
        participant_id INTEGER,
        name TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Library (
        participant_id INTEGER,
        name TEXT,
        did_not_like_using TEXT,
        used TEXT,
        want_to_use_next_year TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS CodingEditor (
        participant_id INTEGER,
        name TEXT,
        did_not_like_using TEXT,
        used TEXT,
        want_to_use_next_year TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Tool (
        participant_id INTEGER,
        name TEXT,
        did_not_like_using TEXT,
        used TEXT,
        want_to_use_next_year TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Database (
        participant_id INTEGER,
        name TEXT,
        did_not_like_using TEXT,
        used TEXT,
        want_to_use_next_year TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS CloudPlatform (
        participant_id INTEGER,
        name TEXT,
        did_not_like_using TEXT,
        used TEXT,
        want_to_use_next_year TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS CodePlatform (
        participant_id INTEGER,
        name TEXT,
        did_not_like_using TEXT,
        used TEXT,
        want_to_use_next_year TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS WorkManagementTool (
        participant_id INTEGER,
        name TEXT,
        did_not_like_using TEXT,
        used TEXT,
        want_to_use_next_year TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS CommunicationTool (
        participant_id INTEGER,
        name TEXT,
        did_not_like_using TEXT,
        used TEXT,
        want_to_use_next_year TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS AIUsage (
        participant_id INTEGER,
        name TEXT,
        did_not_like_using TEXT,
        used TEXT,
        want_to_use_next_year TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS AIEthicalIssue (
        participant_id INTEGER,
        name TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS TechEventCategory (
        participant_id INTEGER,
        name TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS TechEventTopic (
        participant_id INTEGER,
        name TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS TechEventConsumable (
        participant_id INTEGER,
        name TEXT,
        PRIMARY KEY(participant_id, name),
        FOREIGN KEY(participant_id) REFERENCES Participant(id)
    )''')
