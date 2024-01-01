import csv
import sqlite3


def convert(file: csv.DictReader, db: sqlite3.Cursor):
    next(file)  # Skip header.
    for row in file:
        participant_id: int = _add_participant(
            db,
            row['Timestamp'],
            row['Gender'],
            row['Location'],
            row['Hometown'],
            row['Age'],
            row['Educational Attainment'],
            row['College/University Alma Mater'],
            row['Degree Programme'],
            row['Academic Learnings'],
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
        print(participant_id)


def _add_participant(db: sqlite3.Cursor,
                     time_submitted: str,
                     gender: str,
                     location: str,
                     hometown: str,
                     age: str,
                     educational_attainment: str,
                     college_alma_mater: str,
                     degree: str,
                     academic_learnings_satisfaction: str,
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
        '                        college_alma_mater, degree,'
        '                        academic_learnings_satisfaction,'
        '                        computer_used, personal_description,'
        '                        occupation, programming_exp_length,'
        '                        prof_programming_exp_length, developer_type,'
        '                        local_cs_it_sentiments,'
        '                        all_data_ai_training_sentiment,'
        '                        ai_art_sentiment,'
        '                        oss_code_ai_training_sentiment,'
        '                        is_survey_length_okay, survey_difficulty,'
        '                        event_location_suggestions, message_for_dev8)'
        '            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
        '                   ?, ?, ?, ?, ?, ?);'
    )
    params: tuple = (
        time_submitted, gender, location, hometown, age, educational_attainment,
        college_alma_mater, degree, academic_learnings_satisfaction,
        computer_used, personal_description, occupation,
        programming_exp_length, prof_programming_exp_length, developer_type,
        local_cs_it_sentiments, all_data_ai_training_sentiment,
        ai_art_sentiment, oss_code_ai_training_sentiment,
        is_survey_length_okay, survey_difficulty, event_location_suggestions,
        message_for_dev8,
    )
    db.execute(query, params)

    return db.lastrowid


def _add_participant_pc(db: sqlite3.Cursor, participant_id: int,
                        os: str, specs: list[str]):
    pc_query: str = 'INSERT INTO pc(participant_id, os) VALUES (?, ?);'
    pc_spec_query: str = (
        'INSERT INTO pc_spec(participant_id, spec) VALUES (?, ?);'
    )
