PERSONAL_INFORMATION_SECTION_TITLES = {
        'contact information', 'personal details', 'personal information', 'personal background'}
EDUCATION_SECTION_TITLES = {
        'education', 'academic background', 'academic credentials', 'qualifications'}
EXPERIENCE_SECTION_TITLES = {
        'experience', 'professional', 'work', 'professional experience', 'work experience', 'employment history', 'career history', 'work history'}
SKILLS_SECTION_TITLES = {
        'skills', 'technical skills', 'key skills', 'professional skills'}

NUMBER_OF_SECTIONS = 4

SECTION_TITLES = [
        set(PERSONAL_INFORMATION_SECTION_TITLES), 
        set(EDUCATION_SECTION_TITLES), 
        set(EXPERIENCE_SECTION_TITLES), 
        set(SKILLS_SECTION_TITLES)]


TEXT_BLOCK_CATEGORIES = ['personal information', 'education', 'experience', 'skills']

PERSONAL_INFORMATION_WORDS = (PERSONAL_INFORMATION_SECTION_TITLES
        .union({'name', 'address', 'phone number', 'email address', 'linkedin profile', 'personal website', 
                'date of birth', 'nationality', 'gender', 'marital status', 'dependents', 'military service', 
                'volunteer experience', 'personal interests', 'professional memberships', 
                'referees', 'emergency contact', 'driver\'s license', 'passport', 
                'health and safety certifications'}))

EDUCATION_WORDS = (EDUCATION_SECTION_TITLES
        .union({'degree', 'major', 'minor', 'field of study', 'institution', 'graduation date', 'gpa', 'honors', 
                'awards', 'scholarships', 'thesis', 'dissertation', 'project', 'courses', 'certification', 'training', 
                'apprenticeship', 'relevant coursework', 'extracurricular activities', 'study abroad program'}))

EXPERIENCE_WORDS = (EXPERIENCE_SECTION_TITLES
        .union({'position', 'job title', 'company', 'dates of employment', 'responsibilities', 'achievements', 
                'skills used', 'key accomplishments', 'projects', 'team size', 'technologies used', 'problem solving', 
                'leadership', 'interpersonal skills', 'communication skills', 'time management', 'customer service', 
                'sales', 'marketing', 'financial analysis'}))

SKILLS_WORDS = (SKILLS_SECTION_TITLES
        .union({'classroom management', 'lesson planning', 'curriculum development', 'assessment and evaluation', 
                'student engagement', 'differentiated instruction', 'collaboration with colleagues', 
                'parent and student communication', 'classroom technology', 'behavioral management', 'special education', 
                'english as a second language (esl)', 'critical thinking skills', 'creative problem solving', 
                'mentorship', 'student motivation', 'positive reinforcement', 'cultural competence', 'adaptive teaching', 
                'classroom diversity'}))

WORDS = [set(PERSONAL_INFORMATION_WORDS), set(EDUCATION_WORDS), set(EXPERIENCE_WORDS), set(SKILLS_WORDS)]