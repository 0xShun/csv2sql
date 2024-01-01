import csv
import sqlite3


def _add_participant(db: sqlite3.Cursor,
                     time_submitted: str,
                     gender: str,
                     location: str,
                     hometown: str,
                     age: str,
                     education_attainment: str,
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
        '                        hometown, age, education_attainment,'
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
        time_submitted, gender, location, hometown, age, education_attainment,
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


def convert(file: csv.DictReader, db: sqlite3.Cursor):
    next(file)  # Skip header.
    for row in file:
        print(row['Computer Specs'].split(';'))
        pass
