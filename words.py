EDUCATION_SECTION_TITLES = {'education'}
EXPERIENCE_SECTION_TITLES = {'experience'}

NUMBER_OF_SECTIONS = 2

SECTION_TITLES = (EDUCATION_SECTION_TITLES
     .union(EXPERIENCE_SECTION_TITLES))

EDUCATION_WORDS = (EDUCATION_SECTION_TITLES
                    .union({'Degree', 'Major', 'Minor', 'Field of study', 'Institution', 'Graduation date', 'GPA', 'Honors', 
                            'Awards', 'Scholarships', 'Thesis', 'Dissertation', 'Project', 'Courses', 'Certification', 'Training', 
                            'Apprenticeship', 'Relevant coursework', 'Extracurricular activities', 'Study abroad program'}))

EXPERIENCE_WRODS = (EXPERIENCE_SECTION_TITLES
                    .union({'Position', 'Job title', 'Company', 'Dates of employment', 'Responsibilities', 'Achievements', 
                            'Skills used', 'Key accomplishments', 'Projects', 'Team size', 'Technologies used', 'Problem solving', 
                            'Leadership', 'Interpersonal skills', 'Communication skills', 'Time management', 'Customer service', 
                            'Sales', 'Marketing', 'Financial analysis'}))
