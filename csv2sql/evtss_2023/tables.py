import sqlite3


def create_tables(db: sqlite3.Cursor):
    _create_participant_table(db)
    _create_pc_tables(db)
    _create_mac_table(db)
    _create_mobile_table(db)
    _create_employment_table(db)
    _create_academics_table(db)
    _create_higher_academics_table(db)
    _create_developer_activity_table(db)
    _create_tech_event_in_region_table(db)
    _create_tech_event_topic_table(db)
    _create_tech_event_food_or_drink_table(db)
    _create_software_table(db)
    _create_platform_table(db)
    _create_programming_language_table(db)
    _create_library_table(db)
    _create_tool_table(db)
    _create_coding_editor_table(db)
    _create_database_table(db)
    _create_cloud_platform_table(db)
    _create_work_management_tool_table(db)
    _create_communication_tool_table(db)
    _create_ai_search_tool_table(db)
    _create_ai_developer_tool_table(db)


def _create_participant_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS participant ('
        '    id                              INT      PRIMARY KEY,'
        '    time_submitted                  DATETIME NOT NULL,'
        '    gender                          TEXT     NOT NULL,'
        '    location                        TEXT     NOT NULL,'
        '    hometown                        TEXT     NOT NULL,'
        '    age                             TEXT     NOT NULL,'
        '    educational_attainment          TEXT     NOT NULL,'
        '    computer_used                   TEXT     NOT NULL,'
        '    personal_description            TEXT     NOT NULL,'
        '    occupation                      TEXT     NOT NULL,'
        '    programming_exp_length          TEXT     NOT NULL,'
        '    prof_programming_exp_length     TEXT     NOT NULL,'
        '    developer_type                  TEXT     NOT NULL,'
        '    local_cs_it_sentiments          TEXT     NOT NULL,'
        '    all_data_ai_training_sentiment  TEXT     NOT NULL,'
        '    ai_art_sentiment                TEXT     NOT NULL,'
        '    oss_code_ai_training_sentiment  TEXT     NOT NULL,'
        '    is_survey_length_okay           TEXT     NOT NULL,'
        '    survey_difficulty               TEXT     NOT NULL,'
        '    event_location_suggestions      TEXT     NULL,'
        '    message_for_dev8                TEXT     NULL'
        ');'
    )
    db.execute(query)


def _create_pc_tables(db: sqlite3.Cursor):
    pc_query: str = (
        'CREATE TABLE IF NOT EXISTS pc ('
        '    participant_id INT  PRIMARY KEY,'
        '    os             TEXT NOT NULL,'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    pc_spec_query: str = (
        'CREATE TABLE IF NOT EXISTS pc_spec ('
        '    participant_id INT  NOT NULL,'
        '    spec           TEXT NOT NULL,'
        '    PRIMARY KEY (participant_id, spec),'
        '    FOREIGN KEY (participant_id) REFERENCES pc(participant_id)'
        ');'
    )
    db.execute(pc_query)
    db.execute(pc_spec_query)


def _create_mac_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS mac ('
        '    participant_id INT  PRIMARY KEY,'
        '    model          TEXT NOT NULL,'
        '    os             TEXT NOT NULL,'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_mobile_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS mobile ('
        '    participant_id INT  PRIMARY KEY,'
        '    model          TEXT NOT NULL,'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_employment_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS employment ('
        '    participant_id             INT  PRIMARY KEY,'
        '    employer_location          TEXT NOT NULL,'
        '    employment_arrangement     TEXT NOT NULL,'
        '    annual_income_range        TEXT NOT NULL,'
        '    annual_income_satisfaction TEXT NOT NULL,'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_academics_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS academics ('
        '    participant_id       INT  PRIMARY KEY,'
        '    academic_arrangement TEXT NOT NULL,'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_higher_academics_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS higher_academics ('
        '    participant_id                  INT  PRIMARY KEY,'
        '    college_alma_mater              TEXT NOT NULL,'
        '    degree                          TEXT NOT NULL,'
        '    academic_learnings_satisfaction TEXT NOT NULL,'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_developer_activity_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS developer_activity ('
        '    participant_id INT  NOT NULL,'
        '    activity       TEXT NOT NULL,'
        '    PRIMARY KEY (participant_id, activity),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_tech_event_in_region_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS tech_event_in_region ('
        '    participant_id INT  NOT NULL,'
        '    event          TEXT NOT NULL,'
        '    PRIMARY KEY (participant_id, event),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_tech_event_topic_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS tech_event_topic ('
        '    participant_id INT  NOT NULL,'
        '    topic          TEXT NOT NULL,'
        '    PRIMARY KEY (participant_id, topic),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_tech_event_food_or_drink_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS tech_event_food_or_drink ('
        '    participant_id INT  NOT NULL,'
        '    suggestion     TEXT NOT NULL,'
        '    PRIMARY KEY (participant_id, suggestion),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_software_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS software ('
        '    participant_id INT  NOT NULL,'
        '    category       TEXT NOT NULL,'
        '    PRIMARY KEY (participant_id, category),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_platform_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS platform ('
        '    participant_id INT  NOT NULL,'
        '    platform       TEXT NOT NULL,'
        '    PRIMARY KEY (participant_id, platform),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_programming_language_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS programming_language ('
        '    participant_id        INT     NOT NULL,'
        '    language              TEXT    NOT NULL,'
        '    did_not_like_using    BOOLEAN NOT NULL,'
        '    used                  BOOLEAN NOT NULL,'
        '    want_to_use_next_year BOOLEAN NOT NULL,'
        '    is_primary_language   BOOLEAN NOT NULL,'
        '    PRIMARY KEY (participant_id, language),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_library_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS library ('
        '    participant_id        INT     NOT NULL,'
        '    library               TEXT    NOT NULL,'
        '    did_not_like_using    BOOLEAN NOT NULL,'
        '    used                  BOOLEAN NOT NULL,'
        '    want_to_use_next_year BOOLEAN NOT NULL,'
        '    PRIMARY KEY (participant_id, library),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_tool_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS tool ('
        '    participant_id        INT     NOT NULL,'
        '    tool                  TEXT    NOT NULL,'
        '    did_not_like_using    BOOLEAN NOT NULL,'
        '    used                  BOOLEAN NOT NULL,'
        '    want_to_use_next_year BOOLEAN NOT NULL,'
        '    PRIMARY KEY (participant_id, tool),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_coding_editor_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS coding_editor ('
        '    participant_id        INT     NOT NULL,'
        '    editor                TEXT    NOT NULL,'
        '    did_not_like_using    BOOLEAN NOT NULL,'
        '    used                  BOOLEAN NOT NULL,'
        '    want_to_use_next_year BOOLEAN NOT NULL,'
        '    PRIMARY KEY (participant_id, editor),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_database_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS database ('
        '    participant_id        INT     NOT NULL,'
        '    database              TEXT    NOT NULL,'
        '    did_not_like_using    BOOLEAN NOT NULL,'
        '    used                  BOOLEAN NOT NULL,'
        '    want_to_use_next_year BOOLEAN NOT NULL,'
        '    PRIMARY KEY (participant_id, database),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_cloud_platform_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS cloud_platform ('
        '    participant_id        INT     NOT NULL,'
        '    platform              TEXT    NOT NULL,'
        '    did_not_like_using    BOOLEAN NOT NULL,'
        '    used                  BOOLEAN NOT NULL,'
        '    want_to_use_next_year BOOLEAN NOT NULL,'
        '    PRIMARY KEY (participant_id, platform),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_work_management_tool_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS work_management_tool ('
        '    participant_id        INT     NOT NULL,'
        '    tool                  TEXT    NOT NULL,'
        '    did_not_like_using    BOOLEAN NOT NULL,'
        '    used                  BOOLEAN NOT NULL,'
        '    want_to_use_next_year BOOLEAN NOT NULL,'
        '    PRIMARY KEY (participant_id, tool),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_communication_tool_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS communication_tool ('
        '    participant_id        INT     NOT NULL,'
        '    tool                  TEXT    NOT NULL,'
        '    did_not_like_using    BOOLEAN NOT NULL,'
        '    used                  BOOLEAN NOT NULL,'
        '    want_to_use_next_year BOOLEAN NOT NULL,'
        '    PRIMARY KEY (participant_id, tool),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_ai_search_tool_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS ai_search_tool ('
        '    participant_id        INT     NOT NULL,'
        '    tool                  TEXT    NOT NULL,'
        '    did_not_like_using    BOOLEAN NOT NULL,'
        '    used                  BOOLEAN NOT NULL,'
        '    want_to_use_next_year BOOLEAN NOT NULL,'
        '    PRIMARY KEY (participant_id, tool),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)


def _create_ai_developer_tool_table(db: sqlite3.Cursor):
    query: str = (
        'CREATE TABLE IF NOT EXISTS ai_developer_tool ('
        '    participant_id        INT     NOT NULL,'
        '    tool                  TEXT    NOT NULL,'
        '    did_not_like_using    BOOLEAN NOT NULL,'
        '    used                  BOOLEAN NOT NULL,'
        '    want_to_use_next_year BOOLEAN NOT NULL,'
        '    PRIMARY KEY (participant_id, tool),'
        '    FOREIGN KEY (participant_id) REFERENCES participant(id)'
        ');'
    )
    db.execute(query)
