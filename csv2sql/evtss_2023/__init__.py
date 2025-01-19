from .table_schema import create_tables
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

def create_tables(cursor):
    """
    Creates all database tables.
    Delegates to the `create_tables` function in table_schema.py.
    :param cursor: SQLite database cursor
    """
    create_tables(cursor)

def convert(csv_data, cursor):
    """
    Converts CSV data to the database by inserting records.
    :param csv_data: CSV DictReader object
    :param cursor: SQLite database cursor
    """
    for row in csv_data:
        # Insert participant data
        insert_participant(cursor, row)

        # Insert work arrangement data if available
        work_arrangement_data = {
            'participant_id': row['id'],
            'sector': row.get('sector'),
            'employer_location': row.get('employer_location'),
            'employment_arrangement': row.get('employment_arrangement'),
            'average_monthly_income_range': row.get('average_monthly_income_range'),
            'income_satisfaction': row.get('income_satisfaction'),
        }
        insert_work_arrangement(cursor, work_arrangement_data)

        # Insert developer activity
        if 'activity' in row:
            developer_activity_data = {
                'participant_id': row['id'],
                'activity': row['activity'],
            }
            insert_developer_activity(cursor, developer_activity_data)

        # Insert programming languages
        if 'programming_languages' in row:
            languages = row['programming_languages'].split(';')
            for lang in languages:
                programming_language_data = {
                    'participant_id': row['id'],
                    'name': lang,
                    'did_not_like_using': None,
                    'used': None,
                    'want_to_use_next_year': None,
                    'is_primary_language': None,
                }
                insert_programming_language(cursor, programming_language_data)

        # Insert software categories
        if 'software_categories' in row:
            categories = row['software_categories'].split(';')
            for category in categories:
                software_category_data = {
                    'participant_id': row['id'],
                    'name': category,
                }
                insert_software_category(cursor, software_category_data)

        # Insert platforms
        if 'platforms' in row:
            platforms = row['platforms'].split(';')
            for platform in platforms:
                platform_data = {
                    'participant_id': row['id'],
                    'name': platform,
                }
                insert_platform(cursor, platform_data)

        # Insert libraries
        if 'libraries' in row:
            libraries = row['libraries'].split(';')
            for library in libraries:
                library_data = {
                    'participant_id': row['id'],
                    'name': library,
                    'did_not_like_using': None,
                    'used': None,
                    'want_to_use_next_year': None,
                }
                insert_library(cursor, library_data)

        # Insert coding editors
        if 'coding_editors' in row:
            editors = row['coding_editors'].split(';')
            for editor in editors:
                coding_editor_data = {
                    'participant_id': row['id'],
                    'name': editor,
                    'did_not_like_using': None,
                    'used': None,
                    'want_to_use_next_year': None,
                }
                insert_coding_editor(cursor, coding_editor_data)

        # Insert tools
        if 'tools' in row:
            tools = row['tools'].split(';')
            for tool in tools:
                tool_data = {
                    'participant_id': row['id'],
                    'name': tool,
                    'did_not_like_using': None,
                    'used': None,
                    'want_to_use_next_year': None,
                }
                insert_tool(cursor, tool_data)

        # Insert databases
        if 'databases' in row:
            databases = row['databases'].split(';')
            for database in databases:
                database_data = {
                    'participant_id': row['id'],
                    'name': database,
                    'did_not_like_using': None,
                    'used': None,
                    'want_to_use_next_year': None,
                }
                insert_database(cursor, database_data)

        # Insert cloud platforms
        if 'cloud_platforms' in row:
            cloud_platforms = row['cloud_platforms'].split(';')
            for cloud_platform in cloud_platforms:
                cloud_platform_data = {
                    'participant_id': row['id'],
                    'name': cloud_platform,
                    'did_not_like_using': None,
                    'used': None,
                    'want_to_use_next_year': None,
                }
                insert_cloud_platform(cursor, cloud_platform_data)

        # Insert code platforms
        if 'code_platforms' in row:
            code_platforms = row['code_platforms'].split(';')
            for code_platform in code_platforms:
                code_platform_data = {
                    'participant_id': row['id'],
                    'name': code_platform,
                    'did_not_like_using': None,
                    'used': None,
                    'want_to_use_next_year': None,
                }
                insert_code_platform(cursor, code_platform_data)

        # Insert work management tools
        if 'work_management_tools' in row:
            management_tools = row['work_management_tools'].split(';')
            for tool in management_tools:
                work_management_tool_data = {
                    'participant_id': row['id'],
                    'name': tool,
                }
                insert_work_management_tool(cursor, work_management_tool_data)

        # Insert communication tools
        if 'communication_tools' in row:
            communication_tools = row['communication_tools'].split(';')
            for comm_tool in communication_tools:
                communication_tool_data = {
                    'participant_id': row['id'],
                    'name': comm_tool,
                    'did_not_like_using': None,
                    'used': None,
                    'want_to_use_next_year': None,
                }
                insert_communication_tool(cursor, communication_tool_data)

        # Insert AI usage
        if 'ai_usage' in row:
            ai_usages = row['ai_usage'].split(';')
            for ai in ai_usages:
                ai_usage_data = {
                    'participant_id': row['id'],
                    'name': ai,
                    'did_not_like_using': None,
                    'used': None,
                    'want_to_use_next_year': None,
                }
                insert_ai_usage(cursor, ai_usage_data)

        # Insert AI ethical issues
        if 'ai_ethical_issues' in row:
            ethical_issues = row['ai_ethical_issues'].split(';')
            for issue in ethical_issues:
                ai_ethical_issue_data = {
                    'participant_id': row['id'],
                    'name': issue,
                }
                insert_ai_ethical_issue(cursor, ai_ethical_issue_data)

        # Insert tech event categories
        if 'tech_event_categories' in row:
            categories = row['tech_event_categories'].split(';')
            for category in categories:
                tech_event_category_data = {
                    'participant_id': row['id'],
                    'name': category,
                }
                insert_tech_event_category(cursor, tech_event_category_data)

        # Insert tech event topics
        if 'tech_event_topics' in row:
            topics = row['tech_event_topics'].split(';')
            for topic in topics:
                tech_event_topic_data = {
                    'participant_id': row['id'],
                    'name': topic,
                }
                insert_tech_event_topic(cursor, tech_event_topic_data)

        # Insert tech event consumables
        if 'tech_event_consumables' in row:
            consumables = row['tech_event_consumables'].split(';')
            for consumable in consumables:
                tech_event_consumable_data = {
                    'participant_id': row['id'],
                    'name': consumable,
                }
                insert_tech_event_consumable(cursor, tech_event_consumable_data)
