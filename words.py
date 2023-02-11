EDUCATION_SECTION_TITLES = {'education'}
EXPERIENCE_SECTION_TITLES = {'experience'}

NUMBER_OF_SECTIONS = 2

SECTION_TITLES = [set(EDUCATION_SECTION_TITLES), set(EXPERIENCE_SECTION_TITLES)]


TEXT_BLOCK_CATEGORIES = ['education', 'experience']

EDUCATION_WORDS = (EDUCATION_SECTION_TITLES
                    .union({'Degree', 'Major', 'Minor', 'Field of study', 'Institution', 'Graduation date', 'GPA', 'Honors', 
                            'Awards', 'Scholarships', 'Thesis', 'Dissertation', 'Project', 'Courses', 'Certification', 'Training', 
                            'Apprenticeship', 'Relevant coursework', 'Extracurricular activities', 'Study abroad program'}))

EXPERIENCE_WORDS = (EXPERIENCE_SECTION_TITLES
                    .union({'Position', 'Job title', 'Company', 'Dates of employment', 'Responsibilities', 'Achievements', 
                            'Skills used', 'Key accomplishments', 'Projects', 'Team size', 'Technologies used', 'Problem solving', 
                            'Leadership', 'Interpersonal skills', 'Communication skills', 'Time management', 'Customer service', 
                            'Sales', 'Marketing', 'Financial analysis'}))

WORDS = [set(EDUCATION_WORDS), set(EXPERIENCE_WORDS)]