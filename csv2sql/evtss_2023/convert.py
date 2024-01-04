import csv
import sqlite3


def convert(file: csv.DictReader, db: sqlite3.Cursor):
    attainments_for_higher_acads: tuple = (
        'Some university/college without earning a degree',
        'Associate Degree (A.A., A.S., etc.)',
        'Bachelor\'s Degree (B.A., B.S., B.Eng, etc.)',
        'Master\'s Degree (M.A., M.S., M.Eng., MBA, etc.)',
        'Professional Degree (JD, MD, Ph.D, Ed.D, etc.)',
    )
    languages: tuple = (
        'Ada', 'Apex', 'APL', 'Assembly', 'C', 'C++', 'C#', 'Clojure', 'Cobol',
        'Crystal', 'Dart', 'DataWeave', 'Delphi', 'Elixir', 'Erlang', 'F#',
        'Flow', 'Fortran', 'GDScript', 'Go', 'Groovy', 'Haskell', 'HTML/CSS',
        'Java', 'JavaScript', 'Julia', 'Kotlin', 'LISP', 'Lua', 'MATLAB', 'Nim',
        'Objective-C', 'OCaml', 'Perl', 'PHP', 'PowerShell', 'Prolog', 'Python',
        'Ruby', 'R', 'Raku', 'Rust', 'SAS', 'Scala', 'Shell (e.g. Bash, ZSH)',
        'Solidity', 'SQL', 'Swift', 'SystemVerilog', 'TypeScript', 'Verilog',
        'Visual Basic (6 or earlier)', 'Visual Basic .NET', 'VBA', 'Zig',
    )
    libraries: tuple = (
        '.NET 5+', '.NET Framework 1.0 - 4.8', '.NET MAUI', 'Angular',
        'AngularJS', 'Apache Kafka', 'Apache Spark', 'ASP.Net', 'ASP.Net Core',
        'bandit', 'Blazor', 'Boost.Test', 'Capacitor', 'Catch', 'CodeIgniter',
        'Compose Multiplatform', 'Cordova', 'cppunit', 'CUDA', 'Deno',
        'DirectX 12', 'DirectX 9 - 11', 'Django', 'doctest', 'Drupal',
        'Electron', 'ELFspy', 'Elm', 'Express', 'FastAPI', 'Fastify', 'Flask',
        'Flutter', 'Gatsby', 'GLFW', 'Google Test', 'GTK', 'Hadoop',
        'Hugging Face Transformers', 'Ionic', 'JAX', 'jQuery', 'Keras',
        'Kotlin Multiplatform', 'Kivy', 'Ktor', 'Laravel', 'liblittletest',
        'Lit', 'Metal', 'MFC', 'Micronaut', 'NestJS', 'Next.js', 'Node.js',
        'NumPy', 'Nuxt.js', 'OpenCL', 'OpenCV', 'OpenGL', 'Pandas', 'Phoenix',
        'Play Framework', 'Qt', 'Quarkus', 'Qwik', 'RabbitMQ', 'React',
        'React Native', 'Remix', 'Ruby on Rails', 'SciKit-Learn', 'SDL', 'SFML',
        'snitch', 'Solid.js', 'Spring Boot', 'Spring Framework', 'Svelte',
        'SwiftUI', 'Symfony', 'Tauri', 'TensorFlow', 'Tidyverse',
        'Torch/PyTorch', 'Uno Platform', 'Vue.js', 'Vulkan', 'WordPress',
        'Xamarin',
    )
    tools: tuple = (
        'Ansible', 'Ant', 'APT', 'build2', 'Bun', 'Cargo', 'Chef', 'Chocolatey',
        'CMake', 'Composer', 'Dagger', 'Docker', 'GNU GCC', 'Godot', 'Gradle',
        'Homebrew', 'Kubernetes', 'LLVM Clang', 'Make', 'Maven', 'Meson',
        'MSBuild', 'MSVC', 'Ninja', 'Nix', 'npm', 'NuGet', 'Pacman', 'Pip',
        'pnpm', 'Podman', 'Pulumi', 'Puppet', 'QMake', 'Scons', 'Terraform',
        'Unity 3D', 'Unreal Engine', 'Vite', 'Wasmer', 'Webpack', 'Yarn',
    )
    editors: tuple = (
        'Android Studio', 'Atom', 'BBEdit', 'CLion', 'Code::Blocks', 'condo',
        'DataGrip', 'Eclipse', 'Emacs', 'Fleet', 'Geany', 'Goland', 'Helix',
        'IntelliJ IDEA', 'IPython', 'Jupyter Notebook/JupyterLab', 'Kate',
        'Micro', 'Nano', 'Neovim', 'NetBeans', 'Notepad++', 'Nova', 'PhpStorm',
        'PyCharm', 'Qt Creator', 'RAD Studio', 'Rider', 'RStudio', 'RubyMine',
        'RustRover', 'Spyder', 'Sublime Text', 'TextMate', 'Vim',
        'Visual Studio', 'Visual Studio Code', 'VSCodium', 'WebStorm', 'XCode',
    )
    databases: tuple = (
        'BigQuery', 'Cassandra', 'Clickhouse', 'Cloud Firestore', 'CockroachDB',
        'Cosmos DB', 'CouchDB', 'Datomic', 'DuckDB', 'DynamoDB',
        'ElasticSearch', 'Firebase Realtime Database', 'Firebird', 'H2',
        'IBM DB2', 'InfluxDB', 'MariaDB', 'Microsoft Access',
        'Microsoft SQL Server', 'MongoDB', 'MySQL', 'Neo4J', 'Oracle',
        'PostgreSQL', 'RavenDB', 'Redis', 'Snowflake', 'Solr', 'SQLite',
        'Supabase', 'Text Files', 'TiDB',
    )
    cloud_platforms: tuple = (
        'Amazon Web Services (AWS)', 'Cloudflare', 'Colocation', 'DigitalOcean',
        'Firebase', 'Fly.io', 'Google Cloud Platform', 'Heroku', 'Hetzner',
        'IBM Cloud or Watson', 'Linode (now Akamai)', 'Managed Hosting',
        'Microsoft Azure', 'Netlify', 'OpenShift', 'OpenStack',
        'Oracle Cloud Infrastructure', 'OVH', 'Render', 'Scaleway',
        'Self-Hosted', 'Vercel', 'VMware', 'Vultr',
    )
    work_management_tools: tuple = (
        'Adobe Workfront', 'Airtable', 'Asana', 'Azure DevOps', 'Basecamp',
        'Cerri', 'ClickUp', 'Confluence', 'Dingtalk (Teambition)',
        'Document360', 'Doxygen', 'GitHub Discussions', 'Jira', 'Leankor',
        'Linear', 'Markdown File', 'Microsoft Lists', 'Microsoft Planner',
        'Miro', 'Monday.com', 'Notion', 'Nuclino',
        'Planview Projectplace or Clarizen', 'Redmine', 'Redocly', 'Shortcut',
        'Smartsheet', 'StackOverflow for Teams', 'Swit', 'Tettra', 'Trello',
        'Wikis', 'Workzone', 'Wrike', 'YouTrack',
    )
    communication_tools: tuple = (
        'Cisco Webex Teams', 'Coolfire Core', 'Discord',
        'Facebook Messenger', 'Google Chat', 'Google Meet', 'IRC', 'Jitsi',
        'Matrix', 'Mattermost', 'Microsoft Teams', 'Ringcentral', 'Rocketchat',
        'Signal', 'Skype', 'Slack', 'Symphony', 'Telegram', 'Unify Circuit',
        'Whatsapp', 'Wickr', 'Wire', 'Zoom', 'Zulip',
    )
    ai_search_tools: tuple = (
        'Andi', 'Bing AI', 'ChatGPT', 'Google Bard AI', 'Metaphor', 'Neeva AI',
        'Perplexity AI', 'Phind', 'Quora Poe', 'WolframAlpha', 'You.com',
        'Others',
    )
    ai_developer_tools: tuple = (
        'Adrenaline', 'AWS CodeWhisperer', 'Codeium', 'GitHub Copilot',
        'Mintlify', 'Replit Ghostwriter', 'Rubber Duck.AI', 'Synk Code',
        'TabNine', 'Whispr AI', 'Others',
    )

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

        if row['Educational Attainment'] in attainments_for_higher_acads:
            _add_higher_academics(db,
                                  participant_id,
                                  row['College/University Alma Mater'],
                                  row['Degree Programme'],
                                  row['Academic Learnings'])

        computer_used: str = row['Computer Used Most of the Time']
        if computer_used in ('Desktop PC', 'Laptop PC',):
            os: str = row['Operating System (PC)']
            specs: list[str] = row['Computer Specs'].split(';')
            _add_pc(db, participant_id, os, specs)
        elif computer_used == 'Mac':
            os: str = row['Operating System (Mac)']
            model: str = row['Mac Model']
            _add_mac(db, participant_id, model, os)
        elif computer_used in ('Tablet', 'Smartphone',):
            model: str = row['Tablet/Smartphone Model']
            _add_mobile(db, participant_id, model)

        if row['Occupation'] == 'Professional/Freelancer':
            employer_location: str = row['Employer Location']
            employment_arrangement: str = row['Employment Arrangement']
            annual_income_range: str = row['Annual Income Range']
            annual_income_satisfaction: str = row['Annual Income Satisfaction']
            _add_employment(db,
                            participant_id,
                            employer_location,
                            employment_arrangement,
                            annual_income_range,
                            annual_income_satisfaction)
        elif row['Occupation'] == 'Student':
            academic_arrangement: str = row['Academic Arrangement']
            _add_academics(db, participant_id, academic_arrangement)

        developer_activities: list[str] = row['Developer Activities'].split(';')
        for activity in developer_activities:
            _add_developer_activity(db, participant_id, activity)

        primary_languages: set[str] = set(row['Primary Languages'].split(';'))
        for lang in languages:
            column_name: str = f'Languages Used, Loved, and Hated [{lang}]'
            lang_interest: set[str] = set(row[column_name].split(';'))
            did_not_like_using: bool = 'Did not like using' in lang_interest
            used: bool = 'Used this year' in lang_interest
            want_to_use_next_yr: bool = 'Want to use next year' in lang_interest
            is_primary_language: bool = lang in primary_languages
            _add_programming_language(db,
                                      participant_id,
                                      lang,
                                      did_not_like_using,
                                      used,
                                      want_to_use_next_yr,
                                      is_primary_language)

        column_name: str = 'Software Being Developed'
        software_being_developed: list[str] = row[column_name].split(';')
        for software in software_being_developed:
            _add_software(db, participant_id, software)

        platforms: list[str] = row['Platforms'].split(';')
        for platform in platforms:
            _add_platform(db, participant_id, platform)

        for library in libraries:
            column_name: str = f'Frameworks and Libraries [{library}]'
            lib_interest: set[str] = set(row[column_name].split(';'))
            did_not_like_using: bool = 'Did not like using' in lib_interest
            used: bool = 'Used this year' in lib_interest
            want_to_use_next_yr: bool = 'Want to use next year' in lib_interest
            _add_library(db,
                         participant_id,
                         library,
                         did_not_like_using,
                         used,
                         want_to_use_next_yr)

        for tool in tools:
            column_name: str = f'Tools [{tool}]'
            tool_interest: set[str] = set(row[column_name].split(';'))
            did_not_like_using: bool = 'Did not like using' in tool_interest
            used: bool = 'Used this year' in tool_interest
            want_to_use_next_yr: bool = 'Want to use next year' in tool_interest
            _add_tool(db,
                      participant_id,
                      tool,
                      did_not_like_using,
                      used,
                      want_to_use_next_yr)

        for editor in editors:
            column_name: str = f'IDEs and Text Editors [{editor}]'
            editor_interest: set[str] = set(row[column_name].split(';'))
            did_not_like_using: bool = 'Did not like using' in editor_interest
            used: bool = 'Used this year' in editor_interest
            want_to_use_ny: bool = 'Want to use next year' in editor_interest
            _add_coding_editor(db,
                               participant_id,
                               editor,
                               did_not_like_using,
                               used,
                               want_to_use_ny)

        for database in databases:
            column_name: str = f'Databases Used, Loved, and Hated [{database}]'
            db_interest: set[str] = set(row[column_name].split(';'))
            did_not_like_using: bool = 'Did not like using' in db_interest
            used: bool = 'Used this year' in db_interest
            want_to_use_next_yr: bool = 'Want to use next year' in db_interest
            _add_database(db,
                          participant_id,
                          database,
                          did_not_like_using,
                          used,
                          want_to_use_next_yr)

        for platform in cloud_platforms:
            col_name: str = f'Cloud Platforms Used, Loved, and Hated [{platform}]'
            platform_interest: set[str] = set(row[col_name].split(';'))
            did_not_like_using: bool = 'Did not like using' in platform_interest
            used: bool = 'Used this year' in platform_interest
            want_to_use_ny: bool = 'Want to use next year' in platform_interest
            _add_cloud_platform(db,
                                participant_id,
                                platform,
                                did_not_like_using,
                                used,
                                want_to_use_ny)

        for tool in work_management_tools:
            col_name: str = f'Work Management and Code Documentation [{tool}]'
            tool_interest: set[str] = set(row[col_name].split(';'))
            did_not_like_using: bool = 'Did not like using' in tool_interest
            used: bool = 'Used this year' in tool_interest
            want_to_use_ny: bool = 'Want to use next year' in tool_interest
            _add_work_management_tool(db,
                                      participant_id,
                                      tool,
                                      did_not_like_using,
                                      used,
                                      want_to_use_ny)

        for tool in communication_tools:
            column_name: str = f'Communication Tools [{tool}]'
            tool_interest: set[str] = set(row[column_name].split(';'))
            did_not_like_using: bool = 'Did not like using' in tool_interest
            used: bool = 'Used this year' in tool_interest
            want_to_use_ny: bool = 'Want to use next year' in tool_interest
            _add_communication_tool(db,
                                    participant_id,
                                    tool,
                                    did_not_like_using,
                                    used,
                                    want_to_use_ny)

        for tool in communication_tools:
            column_name: str = f'Communication Tools [{tool}]'
            tool_interest: set[str] = set(row[column_name].split(';'))
            did_not_like_using: bool = 'Did not like using' in tool_interest
            used: bool = 'Used this year' in tool_interest
            want_to_use_ny: bool = 'Want to use next year' in tool_interest
            _add_communication_tool(db,
                                    participant_id,
                                    tool,
                                    did_not_like_using,
                                    used,
                                    want_to_use_ny)

        tech_events: list[str] = row['Tech Events in the Region'].split(';')
        for event in tech_events:
            _add_tech_event_in_region(db, participant_id, event)

        topics: list[str] = row['Topics'].split(';')
        for topic in topics:
            _add_tech_event_topic(db, participant_id, topic)

        for tool in ai_search_tools:
            column_name: str = f'AI Search Tools [{tool}]'
            tool_interest: set[str] = set(row[column_name].split(';'))
            did_not_like_using: bool = 'Did not like using' in tool_interest
            used: bool = 'Used this year' in tool_interest
            want_to_use_ny: bool = 'Want to use next year' in tool_interest
            _add_ai_search_tool(db,
                                participant_id,
                                tool,
                                did_not_like_using,
                                used,
                                want_to_use_ny)

        for tool in ai_developer_tools:
            column_name: str = f'AI Developer Tools [{tool}]'
            tool_interest: set[str] = set(row[column_name].split(';'))
            did_not_like_using: bool = 'Did not like using' in tool_interest
            used: bool = 'Used this year' in tool_interest
            want_to_use_ny: bool = 'Want to use next year' in tool_interest
            _add_ai_developer_tool(db,
                                   participant_id,
                                   tool,
                                   did_not_like_using,
                                   used,
                                   want_to_use_ny)

        victuals: list[str] = row['Event Food and Drinks'].split(';')
        for victual in victuals:
            _add_tech_event_food_or_drink(db, participant_id, victual)


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
