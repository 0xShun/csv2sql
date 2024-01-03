import csv
import sqlite3


def convert(file: csv.DictReader, db: sqlite3.Cursor):
    for row in file:
        participant_id: int = _add_participant(
            db,
            row['Timestamp'],
            row['Gender'],
            row['Location'],
            row['Hometown'],
            row['Age'],
            row['Educational Attainment'],
            row['Computer Used Most of the Time'],
            row['Personal Description'],
            row['Occupation'],
            row['Length of Programming Experience'],
            row['Length of Professional Programming Experience'],
            row['Developer Type'],
            row['Local CS/IT Sentiments'],
            row['AI Datasets'],
            row['AI Art'],
            row['AI Code Generation'],
            row['Survey Length'],
            row['Survey Difficulty'],
            row['Event Location'],
            row['Message for Dev8']
        )


def _add_participant(db: sqlite3.Cursor,
                     time_submitted: str,
                     gender: str,
                     location: str,
                     hometown: str,
                     age: str,
                     educational_attainment: str,
                     computer_used: str,
                     personal_description: str,
                     occupation: str,
                     programming_exp_length: str,
                     prof_programming_exp_length: str,
                     developer_type: str,
                     local_cs_it_sentiments: str,
                     all_data_ai_training_sentiment: str,
                     ai_art_sentiment: str,
                     oss_code_ai_training_sentiment: str,
                     is_survey_length_okay: str,
                     survey_difficulty: str,
                     event_location_suggestions: str,
                     message_for_dev8: str) -> int:
    query: str = (
        'INSERT INTO participant(time_submitted, gender, location,'
        '                        hometown, age, educational_attainment,'
        '                        computer_used, personal_description,'
        '                        occupation, programming_exp_length,'
        '                        prof_programming_exp_length, developer_type,'
        '                        local_cs_it_sentiments,'
        '                        all_data_ai_training_sentiment,'
        '                        ai_art_sentiment,'
        '                        oss_code_ai_training_sentiment,'
        '                        is_survey_length_okay, survey_difficulty,'
        '                        event_location_suggestions, message_for_dev8)'
        '            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
        '                    ?, ?, ?, ?, ?, ?);'
    )
    params: tuple = (
        time_submitted, gender, location, hometown, age, educational_attainment,
        computer_used, personal_description, occupation,
        programming_exp_length, prof_programming_exp_length, developer_type,
        local_cs_it_sentiments, all_data_ai_training_sentiment,
        ai_art_sentiment, oss_code_ai_training_sentiment,
        is_survey_length_okay, survey_difficulty, event_location_suggestions,
        message_for_dev8,
    )
    db.execute(query, params)

    return db.lastrowid


def _add_pc(db: sqlite3.Cursor, participant_id: int, os: str, specs: list[str]):
    pc_query: str = 'INSERT INTO pc(participant_id, os) VALUES (?, ?);'
    pc_spec_query: str = (
        'INSERT INTO pc_spec(participant_id, spec) VALUES (?, ?);'
    )

    db.execute(pc_query, (participant_id, os,))

    pc_id: int = db.lastrowid
    participant_specs: list[tuple[int, str]] = list()
    for spec in specs:
        participant_specs.append((pc_id, spec,))
    db.executemany(pc_spec_query, participant_specs)


def _add_mac(db: sqlite3.Cursor, participant_id: int, model: str, os: str):
    query: str = 'INSERT INTO mac(participant_id, model, os) VALUES (?, ?, ?);'
    db.execute(query, (participant_id, model, os,))


def _add_mobile(db: sqlite3.Cursor, participant_id: int, model: str):
    query: str = 'INSERT INTO mobile(participant_id, model) VALUES (?, ?);'
    db.execute(query, (participant_id, model,))


def _add_employment(db: sqlite3.Cursor,
                    participant_id: int,
                    employer_location: str,
                    employment_arrangement: str,
                    annual_income_range: str,
                    annual_income_satisfaction: str):
    query: str = (
        'INSERT INTO employment(participant_id, employer_location,'
        '                       employer_arrangement, annual_income_range,'
        '                       annual_income_satisfaction)'
        '            VALUES (?, ?, ?, ?, ?);'
    )
    db.execute(query, (
        participant_id,
        employer_location,
        employment_arrangement,
        annual_income_range,
        annual_income_satisfaction,)
    )


def _add_academics(db: sqlite3.Cursor, participant_id: int,
                   academic_arrangement: str):
    query: str = (
        'INSERT INTO academics(participant_id, academic_arrangement)'
        '            VALUES (?, ?);'
    )
    db.execute(query, (participant_id, academic_arrangement,))


def _add_higher_academics(db: sqlite3.Cursor, participant_id: int,
                          college_alma_mater: str, degree: str,
                          academic_learnings_satisfaction: str):
    query: str = (
        'INSERT INTO higher_academics(participant_id, college_alma_mater,'
        '                             degree, academic_arrangement)'
        '            VALUES (?, ?, ?, ?);'
    )
    params: tuple = (
        participant_id,
        college_alma_mater,
        degree,
        academic_learnings_satisfaction,
    )
    db.execute(query, params)


def _add_developer_activity(db: sqlite3.Cursor, participant_id: int,
                            activity: str):
    query: str = (
        'INSERT INTO developer_activity(participant_id, activity)'
        '            VALUES (?, ?);'
    )
    db.execute(query, (participant_id, activity,))


def _add_tech_event_in_region(db: sqlite3.Cursor, participant_id: int,
                              event: str):
    query: str = (
        'INSERT INTO tech_event_in_region(participant_id, event)'
        '            VALUES (?, ?);'
    )
    db.execute(query, (participant_id, event,))


def _add_tech_event_topic(db: sqlite3.Cursor, participant_id: int, topic: str):
    query: str = (
        'INSERT INTO tech_event_topic(participant_id, topic) VALUES (?, ?);'
    )
    db.execute(query, (participant_id, topic,))


def _add_tech_event_food_or_drink(db: sqlite3.Cursor, participant_id: int,
                                  suggestion: str):
    query: str = (
        'INSERT INTO tech_event_food_or_drink(participant_id, topic)'
        '            VALUES (?, ?);'
    )
    db.execute(query, (participant_id, suggestion,))


def _add_software(db: sqlite3.Cursor, participant_id: int, category: str):
    query: str = 'INSERT INTO software(participant_id, category) VALUES (?, ?);'
    db.execute(query, (participant_id, category,))


def _add_platform(db: sqlite3.Cursor, participant_id: int, platform: str):
    query: str = 'INSERT INTO platform(participant_id, platform) VALUES (?, ?);'
    db.execute(query, (participant_id, platform,))


def _add_programming_language(db: sqlite3.Cursor,
                              participant_id: int,
                              language: str,
                              did_not_like_using: bool,
                              used: bool,
                              want_to_use_next_year: bool,
                              is_primary_language: bool):
    query: str = (
        'INSERT INTO programming_language(participant_id, language,'
        '                                 did_not_like_using, used,'
        '                                 want_to_use_next_year,'
        '                                 is_primary_language)'
        '            VALUES (?, ?, ?, ?, ?, ?);'
    )
    params: tuple = (
        participant_id,
        language,
        did_not_like_using,
        used,
        want_to_use_next_year,
        is_primary_language,
    )
    db.execute(query, params)


def _add_library(db: sqlite3.Cursor,
                 participant_id: int,
                 library: str,
                 did_not_like_using: bool,
                 used: bool,
                 want_to_use_next_year: bool):
    query: str = (
        'INSERT INTO library(participant_id, library, did_not_like_using, '
        '                    used, want_to_use_next_year)'
        '            VALUES (?, ?, ?, ?, ?);'
    )
    params: tuple = (
        participant_id,
        library,
        did_not_like_using,
        used,
        want_to_use_next_year
    )
    db.execute(query, params)


def _add_tool(db: sqlite3.Cursor,
              participant_id: int,
              tool: str,
              did_not_like_using: bool,
              used: bool,
              want_to_use_next_year: bool):
    query: str = (
        'INSERT INTO tool(participant_id, tool,'
        '                 did_not_like_using, used,'
        '                 want_to_use_next_year)'
        '            VALUES (?, ?, ?, ?, ?);'
    )
    params: tuple = (
        participant_id,
        tool,
        did_not_like_using,
        used,
        want_to_use_next_year
    )
    db.execute(query, params)


def _add_coding_editor(db: sqlite3.Cursor,
                       participant_id: int,
                       editor: str,
                       did_not_like_using: bool,
                       used: bool,
                       want_to_use_next_year: bool):
    query: str = (
        'INSERT INTO coding_editor(participant_id, editor,'
        '                          did_not_like_using, used,'
        '                          want_to_use_next_year)'
        '            VALUES (?, ?, ?, ?, ?);'
    )
    params: tuple = (
        participant_id,
        editor,
        did_not_like_using,
        used,
        want_to_use_next_year
    )
    db.execute(query, params)


def _add_database(db: sqlite3.Cursor,
                  participant_id: int,
                  database: str,
                  did_not_like_using: bool,
                  used: bool,
                  want_to_use_next_year: bool):
    query: str = (
        'INSERT INTO database(participant_id, database,'
        '                     did_not_like_using, used,'
        '                     want_to_use_next_year)'
        '            VALUES (?, ?, ?, ?, ?);'
    )
    params: tuple = (
        participant_id,
        database,
        did_not_like_using,
        used,
        want_to_use_next_year
    )
    db.execute(query, params)


def _add_cloud_platform(db: sqlite3.Cursor,
                        participant_id: int,
                        platform: str,
                        did_not_like_using: bool,
                        used: bool,
                        want_to_use_next_year: bool):
    query: str = (
        'INSERT INTO cloud_platform(participant_id, platform,'
        '                           did_not_like_using, used,'
        '                           want_to_use_next_year)'
        '            VALUES (?, ?, ?, ?, ?);'
    )
    params: tuple = (
        participant_id,
        platform,
        did_not_like_using,
        used,
        want_to_use_next_year
    )
    db.execute(query, params)


def _add_work_management_tool(db: sqlite3.Cursor,
                              participant_id: int,
                              tool: str,
                              did_not_like_using: bool,
                              used: bool,
                              want_to_use_next_year: bool):
    query: str = (
        'INSERT INTO work_management_tool(participant_id, tool,'
        '                                 did_not_like_using, used,'
        '                                 want_to_use_next_year)'
        '            VALUES (?, ?, ?, ?, ?);'
    )
    params: tuple = (
        participant_id,
        tool,
        did_not_like_using,
        used,
        want_to_use_next_year
    )
    db.execute(query, params)


def _add_communication_tool(db: sqlite3.Cursor,
                            participant_id: int,
                            tool: str,
                            did_not_like_using: bool,
                            used: bool,
                            want_to_use_next_year: bool):
    query: str = (
        'INSERT INTO communication_tool(participant_id, tool,'
        '                               did_not_like_using, used,'
        '                               want_to_use_next_year)'
        '            VALUES (?, ?, ?, ?, ?);'
    )
    params: tuple = (
        participant_id,
        tool,
        did_not_like_using,
        used,
        want_to_use_next_year
    )
    db.execute(query, params)


def _add_ai_search_tool(db: sqlite3.Cursor,
                        participant_id: int,
                        tool: str,
                        did_not_like_using: bool,
                        used: bool,
                        want_to_use_next_year: bool):
    query: str = (
        'INSERT INTO ai_search_tool(participant_id, tool,'
        '                           did_not_like_using, used,'
        '                           want_to_use_next_year)'
        '            VALUES (?, ?, ?, ?, ?);'
    )
    params: tuple = (
        participant_id,
        tool,
        did_not_like_using,
        used,
        want_to_use_next_year
    )
    db.execute(query, params)


def _add_ai_developer_tool(db: sqlite3.Cursor,
                           participant_id: int,
                           tool: str,
                           did_not_like_using: bool,
                           used: bool,
                           want_to_use_next_year: bool):
    query: str = (
        'INSERT INTO ai_developer_tool(participant_id, tool,'
        '                              did_not_like_using, used,'
        '                              want_to_use_next_year)'
        '            VALUES (?, ?, ?, ?, ?);'
    )
    params: tuple = (
        participant_id,
        tool,
        did_not_like_using,
        used,
        want_to_use_next_year
    )
    db.execute(query, params)
