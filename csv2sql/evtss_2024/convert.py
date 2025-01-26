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

    csv_data.fieldnames = [header.strip() for header in csv_data.fieldnames]
    for row in csv_data:
        cleaned_row = {key.strip(): value.strip() if isinstance(value, str) else value for key, value in row.items()}
        participant_data = {
            'time_submitted': cleaned_row.get('Timestamp', ''),
            'gender': cleaned_row.get('😎 Gender', ''),
            'location': cleaned_row.get('📌 Location', ''),
            'hometown': cleaned_row.get('🌻 Hometown', ''),
            'age': cleaned_row.get('🤓 Age', ''),
            'educational_attainment': cleaned_row.get('📚 Educational Attainment', ''),
            'degree_programme': cleaned_row.get('🎓 Degree Programme', ''),
            'computer_used': cleaned_row.get('🖥️ Computer Used Most of the Time', ''),
            'computer_specs': cleaned_row.get('💪 Computer Specs', ''),
            'os': cleaned_row.get('💿 Operating System', ''),
            'personal_description': cleaned_row.get('🌟 Personal Description', ''),
            'occupation': cleaned_row.get('⚒️ Occupation', ''),
            'programming_exp_length': cleaned_row.get('💪 Length of Programming Experience', ''),
            'prof_programming_exp_length': cleaned_row.get('👔Length of Professional Programming Experience', ''),
            'developer_type': cleaned_row.get('🧰 Developer Type', ''),
            'local_cs_it_sentiments': cleaned_row.get('💡 Local CS/IT Sentiments', ''),
            'ai_dev_use': cleaned_row.get('🤖 Using AI in Development', ''),
            'ai_trust': cleaned_row.get('🥰 Trust in AI', ''),
            'ai_lawsuit_awareness': cleaned_row.get('🧑‍⚖️ AI Lawsuit Awareness', ''),
            'oss_license_compliance': cleaned_row.get('🖊️ OSS License Compliance', ''),
            'survey_length_opinion': cleaned_row.get('📏 Survey Length', ''),
            'survey_difficulty': cleaned_row.get('😰 Survey Difficulty', ''),
            'survey_comment': cleaned_row.get('💪 Survey Comments', ''),
            'event_location_suggestions': cleaned_row.get('📌 Event Location', ''),
            'message_for_dev8': cleaned_row.get('💬 Message for Dev8', ''),
            'message_for_partners': cleaned_row.get('💬 Message for our partners', ''),
            'programming_fuel': cleaned_row.get('☕ Programming Fuel', '')
        }
        participant_id = insert_participant(cursor, participant_data)

        # Insert into WorkArrangement table
        work_arrangement_data = {
            'participant_id': participant_id,
            'sector': cleaned_row.get('🏢 Sector', ''),
            'employer_location': cleaned_row.get('🏛️ Employer Location', ''),
            'employment_arrangement': cleaned_row.get('💺 Employment Arrangement', ''),
            'average_monthly_income_range': cleaned_row.get('💵 Average Monthly Income Range', ''),
            'income_satisfaction': cleaned_row.get('🕶️ Income Satisfaction', '')
        }
        insert_work_arrangement(cursor, work_arrangement_data)

        # Insert into DeveloperActivity table
        activities_str = cleaned_row.get('🧑‍💻 Developer Activities', '')
        if activities_str:
            activities = [a.strip() for a in activities_str.split(';') if a.strip()]
            for activity in activities:
                developer_activity_data = {
                    'participant_id': participant_id,
                    'activity': activity
                }
                insert_developer_activity(cursor, developer_activity_data)

        # Insert programming languages
        languages = [col for col in cleaned_row.keys() if col.startswith('⚒️ Languages Used')]
        primary_languages = [lang.strip() for lang in cleaned_row.get('💖 Primary Languages', '').split(';') if lang.strip()]
        for lang_col in languages:
            if cleaned_row.get(lang_col):
                lang_parts = lang_col.split('[')
                if len(lang_parts) > 1:
                    lang_name = lang_parts[1].split(']')[0]
                    programming_language_data = {
                        'participant_id': participant_id,
                        'name': lang_name,
                        'did_not_like_using': 1 if 'did not like using' in cleaned_row[lang_col].lower() else 0,
                        'used': 1 if 'used this year' in cleaned_row[lang_col].lower() else 0,
                        'want_to_use_next_year': 1 if 'want to use next year' in cleaned_row[lang_col].lower() else 0,
                        'is_primary_language': 1 if lang_name in primary_languages else 0
                    }
                    insert_programming_language(cursor, programming_language_data)

        # Insert software categories
        categories_str = cleaned_row.get('🚀 Software Being Developed', '')
        if categories_str:
            categories = [c.strip() for c in categories_str.split(';') if c.strip()]
            for category in categories:
                software_category_data = {
                    'participant_id': participant_id,
                    'name': category
                }
                insert_software_category(cursor, software_category_data)

        # Insert platforms
        platforms_str = cleaned_row.get('💻 Platforms', '')
        if platforms_str:
            platforms = [p.strip() for p in platforms_str.split(';') if p.strip()]
            for platform in platforms:
                platform_data = {
                    'participant_id': participant_id,
                    'name': platform
                }
                insert_platform(cursor, platform_data)

        # Insert libraries/frameworks
        libraries = [col for col in cleaned_row.keys() if col.startswith('🛠️ Frameworks')]
        for lib_col in libraries:
            if cleaned_row.get(lib_col):
                lib_parts = lib_col.split('[')
                if len(lib_parts) > 1:
                    lib_name = lib_parts[1].split(']')[0]
                    library_data = {
                        'participant_id': participant_id,
                        'name': lib_name,
                        'did_not_like_using': 1 if 'did not like using' in cleaned_row[lib_col].lower() else 0,
                        'used': 1 if 'used this year' in cleaned_row[lib_col].lower() else 0,
                        'want_to_use_next_year': 1 if 'want to use next year' in cleaned_row[lib_col].lower() else 0
                    }
                    insert_library(cursor, library_data)

        # Insert coding editors
        editors = [col for col in cleaned_row.keys() if col.startswith('🖊️ IDEs and Text Editors')]
        for editor_col in editors:
            if cleaned_row.get(editor_col):
                editor_parts = editor_col.split('[')
                if len(editor_parts) > 1:
                    editor_name = editor_parts[1].split(']')[0]
                    editor_data = {
                        'participant_id': participant_id,
                        'name': editor_name,
                        'did_not_like_using': 1 if 'did not like using' in cleaned_row[editor_col].lower() else 0,
                        'used': 1 if 'used' in cleaned_row[editor_col].lower() else 0,
                        'want_to_use_next_year': 1 if 'want to use next year' in cleaned_row[editor_col].lower() else 0
                    }
                    insert_coding_editor(cursor, editor_data)

        # Insert tools
        tools = [col for col in cleaned_row.keys() if col.startswith('🛠️ Tools')]
        for tool_col in tools:
            if cleaned_row.get(tool_col):
                tool_parts = tool_col.split('[')
                if len(tool_parts) > 1:
                    tool_name = tool_parts[1].split(']')[0]
                    tool_data = {
                        'participant_id': participant_id,
                        'name': tool_name,
                        'did_not_like_using': 1 if 'did not like using' in cleaned_row[tool_col].lower() else 0,
                        'used': 1 if 'used' in cleaned_row[tool_col].lower() else 0,
                        'want_to_use_next_year': 1 if 'want to use next year' in cleaned_row[tool_col].lower() else 0
                    }
                    insert_tool(cursor, tool_data)

        # Insert databases
        databases = [col for col in cleaned_row.keys() if col.startswith('📃 Databases Used')]
        for db_col in databases:
            if cleaned_row.get(db_col):
                db_parts = db_col.split('[')
                if len(db_parts) > 1:
                    db_name = db_parts[1].split(']')[0]
                    db_data = {
                        'participant_id': participant_id,
                        'name': db_name,
                        'did_not_like_using': 1 if 'did not like using' in cleaned_row[db_col].lower() else 0,
                        'used': 1 if 'used' in cleaned_row[db_col].lower() else 0,
                        'want_to_use_next_year': 1 if 'want to use next year' in cleaned_row[db_col].lower() else 0
                    }
                    insert_database(cursor, db_data)

        # Insert cloud platforms
        cloud_platforms = [col for col in cleaned_row.keys() if col.startswith('☁️ Cloud Platforms Used')]
        for platform_col in cloud_platforms:
            if cleaned_row.get(platform_col):
                platform_parts = platform_col.split('[')
                if len(platform_parts) > 1:
                    platform_name = platform_parts[1].split(']')[0]
                    cloud_platform_data = {
                        'participant_id': participant_id,
                        'name': platform_name,
                        'did_not_like_using': 1 if 'did not like using' in cleaned_row[platform_col].lower() else 0,
                        'used': 1 if 'used' in cleaned_row[platform_col].lower() else 0,
                        'want_to_use_next_year': 1 if 'want to use next year' in cleaned_row[platform_col].lower() else 0
                    }
                    insert_cloud_platform(cursor, cloud_platform_data)

        # Insert code platforms
        code_platforms = [col for col in cleaned_row.keys() if col.startswith('🖥️ Code Repository and CI/CD')]
        for platform_col in code_platforms:
            if cleaned_row.get(platform_col):
                platform_parts = platform_col.split('[')
                if len(platform_parts) > 1:
                    platform_name = platform_parts[1].split(']')[0]
                    code_platform_data = {
                        'participant_id': participant_id,
                        'name': platform_name,
                        'did_not_like_using': 1 if 'did not like using' in cleaned_row[platform_col].lower() else 0,
                        'used': 1 if 'used' in cleaned_row[platform_col].lower() else 0,
                        'want_to_use_next_year': 1 if 'want to use next year' in cleaned_row[platform_col].lower() else 0
                    }
                    insert_code_platform(cursor, code_platform_data)

        # Insert work management tools
        work_tools = [col for col in cleaned_row.keys() if col.startswith('📖 Work Management and Code Documentation')]
        for tool_col in work_tools:
            if cleaned_row.get(tool_col):
                tool_parts = tool_col.split('[')
                if len(tool_parts) > 1:
                    tool_name = tool_parts[1].split(']')[0]
                    work_tool_data = {
                        'participant_id': participant_id,
                        'name': tool_name,
                        'did_not_like_using': 1 if 'did not like using' in cleaned_row[tool_col].lower() else 0,
                        'used': 1 if 'used' in cleaned_row[tool_col].lower() else 0,
                        'want_to_use_next_year': 1 if 'want to use next year' in cleaned_row[tool_col].lower() else 0
                    }
                    insert_work_management_tool(cursor, work_tool_data)

        # Insert communication tools
        comm_tools = [col for col in cleaned_row.keys() if col.startswith('💬 Communication Tools')]
        for tool_col in comm_tools:
            if cleaned_row.get(tool_col):
                tool_parts = tool_col.split('[')
                if len(tool_parts) > 1:
                    tool_name = tool_parts[1].split(']')[0]
                    comm_tool_data = {
                        'participant_id': participant_id,
                        'name': tool_name,
                        'did_not_like_using': 1 if 'did not like using' in cleaned_row[tool_col].lower() else 0,
                        'used': 1 if 'used' in cleaned_row[tool_col].lower() else 0,
                        'want_to_use_next_year': 1 if 'want to use next year' in cleaned_row[tool_col].lower() else 0
                    }
                    insert_communication_tool(cursor, comm_tool_data)

        # Insert AI usage
        ai_usages = [col for col in cleaned_row.keys() if col.startswith('💻 Usage of AI')]
        for usage_col in ai_usages:
            if cleaned_row.get(usage_col):
                usage_parts = usage_col.split('[')
                if len(usage_parts) > 1:
                    usage_name = usage_parts[1].split(']')[0]
                    usage_value = cleaned_row[usage_col].lower()
                    ai_usage_data = {
                        'participant_id': participant_id,
                        'name': usage_name,
                        'did_not_like_using': 1 if 'did not like using' in usage_value else 0,
                        'used': 1 if 'used this year' in usage_value else 0,
                        'want_to_use_next_year': 1 if 'want to use next year' in usage_value else 0
                    }
                    insert_ai_usage(cursor, ai_usage_data)

        # Insert AI ethical issues
        issues_str = cleaned_row.get('🎆 AI Ethical Issues', '')
        if issues_str:
            issues = [i.strip() for i in issues_str.split(';') if i.strip()]
            for issue in issues:
                ethical_issue_data = {
                    'participant_id': participant_id,
                    'name': issue
                }
                insert_ai_ethical_issue(cursor, ethical_issue_data)

        # Insert tech event categories
        categories_str = cleaned_row.get('🥳 Tech Events in the Region', '')
        if categories_str:
            categories = [c.strip() for c in categories_str.split(';') if c.strip()]
            for category in categories:
                tech_event_category_data = {
                    'participant_id': participant_id,
                    'name': category
                }
                insert_tech_event_category(cursor, tech_event_category_data)

        # Insert tech event topics
        topics_str = cleaned_row.get('🤔 Topics', '')
        if topics_str:
            topics = [t.strip() for t in topics_str.split(';') if t.strip()]
            for topic in topics:
                tech_event_topic_data = {
                    'participant_id': participant_id,
                    'name': topic
                }
                insert_tech_event_topic(cursor, tech_event_topic_data)

        # Insert tech event consumables
        consumables_str = cleaned_row.get('🍔 Event Food and Drinks', '')
        if consumables_str:
            consumables = [c.strip() for c in consumables_str.split(';') if c.strip()]
            for consumable in consumables:
                tech_event_consumable_data = {
                    'participant_id': participant_id,
                    'name': consumable
                }
                insert_tech_event_consumable(cursor, tech_event_consumable_data)
