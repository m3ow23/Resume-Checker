PERSONAL_INFORMATION_SECTION_TITLES = [
        'contact information', 'personal details', 'personal information', 'personal background']
EDUCATION_SECTION_TITLES = [
        'training and certifications', 'licenses and certifications', 'academic background', 'academic credentials', 
        'professional certifications', 'professional development', 'technical certifications', 'industry certifications', 
        'relevant certifications', 'qualifications', 'education', 'credentials', 'certifications']
EXPERIENCE_SECTION_TITLES = [
        'professional experience', 'work experience', 'employment history', 'career history', 'work history',
        'summary statement', 'professional summary', 'career summary', 'summary of qualifications', 'executive summary',
        'experience', 'professional', 'work', 'profile']
SKILLS_SECTION_TITLES = [
        'professional skills', 'technical skills', 'key skills', 'skills', 'languages']

NUMBER_OF_SECTIONS = 4

SECTION_TITLES = [
        PERSONAL_INFORMATION_SECTION_TITLES, 
        EDUCATION_SECTION_TITLES, 
        EXPERIENCE_SECTION_TITLES, 
        SKILLS_SECTION_TITLES]


TEXT_BLOCK_CATEGORIES = ['personal information', 'education', 'experience', 'skills']

PERSONAL_INFORMATION_WORDS = PERSONAL_INFORMATION_SECTION_TITLES + [
        'name', 'address', 'phone number', 'email address', 'linkedin profile', 'personal website', 
        'date of birth', 'nationality', 'gender', 'marital status', 'dependents', 'military service', 
        'volunteer experience', 'personal interests', 'professional memberships', 
        'referees', 'emergency contact', 'driver\'s license', 'passport', 
        'health and safety certifications', 'language proficiency', 'hobbies and interests', 
        'awards and recognition', 'publications', 'patents']

EDUCATION_WORDS = EDUCATION_SECTION_TITLES + [
        'degree', 'major', 'minor', 'field of study', 'institution', 'graduation date', 'gpa', 'honors', 
        'awards', 'scholarships', 'thesis', 'dissertation', 'project', 'courses', 'certification', 'training', 
        'apprenticeship', 'relevant coursework', 'extracurricular activities', 'study abroad program', 'bachelor', 
        'master', 'doctorate', 'post-graduate program', 'diploma']

EXPERIENCE_WORDS = EXPERIENCE_SECTION_TITLES + [
        'position', 'job title', 'company', 'dates of employment', 'responsibilities', 'achievements', 
        'skills used', 'key accomplishments', 'projects', 'team size', 'technologies used', 'problem solving', 
        'leadership', 'interpersonal skills', 'communication skills', 'time management', 'customer service', 
        'sales', 'marketing', 'financial analysis', 'supervisory experience', 'management experience', 
        'client interaction', 'conflict resolution', 'presentation skills', 'negotiation skills']

LANGUAGES = ['english', 'spanish', 'french', 'german', 'chinese']

SKILLS_WORDS = SKILLS_SECTION_TITLES + LANGUAGES + [
        'classroom management', 'lesson planning', 'curriculum development', 'assessment and evaluation', 
        'student engagement', 'differentiated instruction', 'collaboration with colleagues', 
        'parent and student communication', 'classroom technology', 'behavioral management', 'special education', 
        'english as a second language (esl)', 'critical thinking skills', 'creative problem solving', 
        'mentorship', 'student motivation', 'positive reinforcement', 'cultural competence', 'adaptive teaching', 
        'classroom diversity', 'teaching methods', 'educational technology', 'student support services',    
        'behavior management', 'group facilitation', 'professional development', 'teacher training']

WORDS = [PERSONAL_INFORMATION_WORDS, EDUCATION_WORDS, EXPERIENCE_WORDS, SKILLS_WORDS]