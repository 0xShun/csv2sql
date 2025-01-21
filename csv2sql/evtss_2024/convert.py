from .data_insertion import (
    insert_participant,
    insert_work_arrangement,
    insert_developer_activity,
    insert_programming_language,
    insert_software_category,
    insert_platform,
    insert_library,
    insert_coding_editor,
    insert_tool,
    insert_database,
    insert_cloud_platform,
    insert_code_platform,
    insert_work_management_tool,
    insert_communication_tool,
    insert_ai_usage,
    insert_ai_ethical_issue,
    insert_tech_event_category,
    insert_tech_event_topic,
    insert_tech_event_consumable,
)

def convert(csv_data, cursor):
    """
    Converts CSV data into database entries.

    :param csv_data: A csv.DictReader object containing the parsed CSV data
    :param cursor: SQLite database cursor
    """
    for row in csv_data:
        # Insert into Participant table and get the generated ID
        participant_data = {
            'time_submitted': row.get('Timestamp'),
            'gender': row.get('😎 Gender'),
            'location': row.get('📌 Location'),
            'hometown': row.get('🌻 Hometown'),
            'age': row.get('🤓 Age'),
            'education_level': row.get('📚 Educational Attainment'),
            'educational_attainment': row.get('📚 Educational Attainment'),
            'degree_programme': row.get('🎓 Degree Programme'),
            'computer_used': row.get('🖥️ Computer Used Most of the Time'),
            'computer_specs': row.get('💪 Computer Specs'),
            'os': row.get('💿 Operating System'),
            'personal_description': row.get('🌟 Personal Description'),
            'occupation': row.get('⚒️ Occupation'),
            'programming_exp_length': row.get('💪 Length of Programming Experience'),
            'prof_programming_exp_length': row.get('👔Length of Professional Programming Experience'),
            'developer_type': row.get('🧰 Developer Type'),
            'local_cs_it_sentiments': row.get('💡 Local CS/IT Sentiments'),
            'ai_dev_use': row.get('🤖 Using AI in Development'),
            'ai_trust': row.get('🥰 Trust in AI'),
            'ai_lawsuit_awareness': row.get('🧑‍⚖️ AI Lawsuit Awareness'),
            'oss_license_compliance': row.get('🖊️ OSS License Compliance'),
            'survey_length_opinion': row.get('📏 Survey Length'),
            'survey_difficulty': row.get('😰 Survey Difficulty'),
            'survey_comment': row.get('💪 Survey Comments'),
            'event_location_suggestions': row.get('📌 Event Location'),
            'message_for_dev8': row.get('💬 Message for Dev8'),
            'message_for_partners': row.get('💬 Message for our partners'),
            'programming_fuel': row.get('☕ Programming Fuel')
        }
        insert_participant(cursor, participant_data)
        participant_id = cursor.lastrowid

        # Insert into WorkArrangement table
        work_arrangement_data = {
            'participant_id': participant_id,
            'sector': row.get('🏢 Sector'),
            'employer_location': row.get('🏛️ Employer Location'),
            'employment_arrangement': row.get('💺 Employment Arrangement'),
            'average_monthly_income_range': row.get('💵 Average Monthly Income Range'),
            'income_satisfaction': row.get('🕶️ Income Satisfaction')
        }
        insert_work_arrangement(cursor, work_arrangement_data)

        # Insert into DeveloperActivity table
        if row.get('🧑‍💻 Developer Activities'):
            activities = row['🧑‍💻 Developer Activities'].split(';')
            for activity in activities:
                developer_activity_data = {
                    'participant_id': participant_id,
                    'activity': activity.strip()
                }
                insert_developer_activity(cursor, developer_activity_data)

        # Insert programming languages
        languages = [col for col in row.keys() if col.startswith('⚒️ Languages Used')]
        for lang_col in languages:
            if row[lang_col]:
                lang_name = lang_col.split('[')[1].split(']')[0]
                programming_language_data = {
                    'participant_id': participant_id,
                    'name': lang_name,
                    'did_not_like_using': 'did_not_like' in row[lang_col].lower(),
                    'used': 'used' in row[lang_col].lower(),
                    'want_to_use_next_year': 'want_to_use' in row[lang_col].lower(),
                    'is_primary_language': lang_name in (row.get('💖 Primary Languages', '').split(';'))
                }
                insert_programming_language(cursor, programming_language_data)

        # Insert software categories
        if row.get('🚀 Software Being Developed'):
            categories = row['🚀 Software Being Developed'].split(';')
            for category in categories:
                software_category_data = {
                    'participant_id': participant_id,
                    'name': category.strip()
                }
                insert_software_category(cursor, software_category_data)

        # Insert platforms
        if row.get('💻 Platforms'):
            platforms = row['💻 Platforms'].split(';')
            for platform in platforms:
                platform_data = {
                    'participant_id': participant_id,
                    'name': platform.strip()
                }
                insert_platform(cursor, platform_data)

        # Insert libraries/frameworks
        libraries = [col for col in row.keys() if col.startswith('🛠️ Frameworks')]
        for lib_col in libraries:
            if row[lib_col]:
                lib_name = lib_col.split('[')[1].split(']')[0]
                library_data = {
                    'participant_id': participant_id,
                    'name': lib_name,
                    'did_not_like_using': 'did_not_like' in row[lib_col].lower(),
                    'used': 'used' in row[lib_col].lower(),
                    'want_to_use_next_year': 'want_to_use' in row[lib_col].lower()
                }
                insert_library(cursor, library_data)

        # Insert coding editors
        editors = [col for col in row.keys() if col.startswith('🖊️ IDEs and Text Editors')]
        for editor_col in editors:
            if row[editor_col]:
                editor_name = editor_col.split('[')[1].split(']')[0]
                editor_data = {
                    'participant_id': participant_id,
                    'name': editor_name,
                    'did_not_like_using': 'did_not_like' in row[editor_col].lower(),
                    'used': 'used' in row[editor_col].lower(),
                    'want_to_use_next_year': 'want_to_use' in row[editor_col].lower()
                }
                insert_coding_editor(cursor, editor_data)

        # Insert tools
        tools = [col for col in row.keys() if col.startswith('🛠️ Tools')]
        for tool_col in tools:
            if row[tool_col]:
                tool_name = tool_col.split('[')[1].split(']')[0]
                tool_data = {
                    'participant_id': participant_id,
                    'name': tool_name,
                    'did_not_like_using': 'did_not_like' in row[tool_col].lower(),
                    'used': 'used' in row[tool_col].lower(),
                    'want_to_use_next_year': 'want_to_use' in row[tool_col].lower()
                }
                insert_tool(cursor, tool_data)

        # Insert databases
        databases = [col for col in row.keys() if col.startswith('📃 Databases Used')]
        for db_col in databases:
            if row[db_col]:
                db_name = db_col.split('[')[1].split(']')[0]
                db_data = {
                    'participant_id': participant_id,
                    'name': db_name,
                    'did_not_like_using': 'did_not_like' in row[db_col].lower(),
                    'used': 'used' in row[db_col].lower(),
                    'want_to_use_next_year': 'want_to_use' in row[db_col].lower()
                }
                insert_database(cursor, db_data)

        # Insert cloud platforms
        cloud_platforms = [col for col in row.keys() if col.startswith('☁️ Cloud Platforms Used')]
        for platform_col in cloud_platforms:
            if row[platform_col]:
                platform_name = platform_col.split('[')[1].split(']')[0]
                cloud_platform_data = {
                    'participant_id': participant_id,
                    'name': platform_name,
                    'did_not_like_using': 'did_not_like' in row[platform_col].lower(),
                    'used': 'used' in row[platform_col].lower(),
                    'want_to_use_next_year': 'want_to_use' in row[platform_col].lower()
                }
                insert_cloud_platform(cursor, cloud_platform_data)

        # Insert code platforms
        code_platforms = [col for col in row.keys() if col.startswith('🖥️ Code Repository and CI/CD')]
        for platform_col in code_platforms:
            if row[platform_col]:
                platform_name = platform_col.split('[')[1].split(']')[0]
                code_platform_data = {
                    'participant_id': participant_id,
                    'name': platform_name,
                    'did_not_like_using': 'did_not_like' in row[platform_col].lower(),
                    'used': 'used' in row[platform_col].lower(),
                    'want_to_use_next_year': 'want_to_use' in row[platform_col].lower()
                }
                insert_code_platform(cursor, code_platform_data)

        # Insert work management tools
        work_tools = [col for col in row.keys() if col.startswith('📖 Work Management and Code Documentation')]
        for tool_col in work_tools:
            if row[tool_col]:
                tool_name = tool_col.split('[')[1].split(']')[0]
                work_tool_data = {
                    'participant_id': participant_id,
                    'name': tool_name,
                    'did_not_like_using': 'did_not_like' in row[tool_col].lower(),
                    'used': 'used' in row[tool_col].lower(),
                    'want_to_use_next_year': 'want_to_use' in row[tool_col].lower()
                }
                insert_work_management_tool(cursor, work_tool_data)

        # Insert communication tools
        comm_tools = [col for col in row.keys() if col.startswith('💬 Communication Tools')]
        for tool_col in comm_tools:
            if row[tool_col]:
                tool_name = tool_col.split('[')[1].split(']')[0]
                comm_tool_data = {
                    'participant_id': participant_id,
                    'name': tool_name,
                    'did_not_like_using': 'did_not_like' in row[tool_col].lower(),
                    'used': 'used' in row[tool_col].lower(),
                    'want_to_use_next_year': 'want_to_use' in row[tool_col].lower()
                }
                insert_communication_tool(cursor, comm_tool_data)

        # Insert AI usage
        ai_usages = [col for col in row.keys() if col.startswith('💻 Usage of AI')]
        for usage_col in ai_usages:
            if row[usage_col]:
                usage_name = usage_col.split('[')[1].split(']')[0]
                ai_usage_data = {
                    'participant_id': participant_id,
                    'name': usage_name,
                    'did_not_like_using': False,  # These fields might need adjustment based on actual data
                    'used': True,
                    'want_to_use_next_year': True
                }
                insert_ai_usage(cursor, ai_usage_data)

        # Insert AI ethical issues
        if row.get('🎆 AI Ethical Issues'):
            issues = row['🎆 AI Ethical Issues'].split(';')
            for issue in issues:
                ethical_issue_data = {
                    'participant_id': participant_id,
                    'name': issue.strip()
                }
                insert_ai_ethical_issue(cursor, ethical_issue_data)

        # Insert tech event categories
        if row.get('🥳 Tech Events in the Region'):
            categories = row['🥳 Tech Events in the Region'].split(';')
            for category in categories:
                tech_event_category_data = {
                    'participant_id': participant_id,
                    'name': category.strip()
                }
                insert_tech_event_category(cursor, tech_event_category_data)

        # Insert tech event topics
        if row.get('🤔 Topics'):
            topics = row['🤔 Topics'].split(';')
            for topic in topics:
                tech_event_topic_data = {
                    'participant_id': participant_id,
                    'name': topic.strip()
                }
                insert_tech_event_topic(cursor, tech_event_topic_data)

        # Insert tech event consumables
        if row.get('🍔 Event Food and Drinks'):
            consumables = row['🍔 Event Food and Drinks'].split(';')
            for consumable in consumables:
                tech_event_consumable_data = {
                    'participant_id': participant_id,
                    'name': consumable.strip()
                }
                insert_tech_event_consumable(cursor, tech_event_consumable_data)
