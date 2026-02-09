"""
===============================================================================
KOREAN TEXT PREPROCESSING FOR ORANGE DATA MINING
===============================================================================

This script helps you prepare Korean text data for analysis by:
1. Automatically installing the Korean language processing library (kiwipiepy)
2. Breaking Korean sentences into meaningful words (tokenization)
3. Identifying word types (nouns, verbs, adjectives, etc.)
4. Removing common words that don't add meaning (stopwords)
5. Cleaning up messy text (URLs, special characters, etc.)

WHY YOU NEED THIS:
Orange's built-in text preprocessing doesn't understand Korean grammar well.
Korean is an "agglutinative" language - words stick together with suffixes
that change meaning. For example: "먹다" (to eat) → "먹었습니다" (ate politely).
We need special tools to break these apart correctly.

HOW TO USE:
1. Load your data in Orange (must have a text column)
2. Add a "Python Script" widget
3. Paste this code
4. Change TEXT_COLUMN below to match YOUR column name
5. Run it!

===============================================================================
"""

# ===== IMPORTING LIBRARIES =====
# Think of these as toolboxes - we're opening up different toolboxes to use
# their tools throughout our script

import subprocess  # Lets us run terminal commands (to install packages)
import sys         # Gives us information about Python itself
import re          # "Regular expressions" - pattern matching for text (like find/replace on steroids)
import pandas as pd  # A popular library for working with data tables
from Orange.data import Table, Domain, StringVariable  # Orange-specific tools for handling data


# ===== AUTO-INSTALL SECTION =====
# This part checks if kiwipiepy is installed, and if not, installs it automatically
# You don't need to install anything manually - the script does it for you!

def install_package(package):
    """
    This function tries to import a package. If it fails (ImportError),
    it automatically installs the package using pip.
    
    Think of it like: "Do I have this tool? No? Let me go get it."
    """
    try:
        # Try to import the package - if this works, we already have it!
        __import__(package)
        return True
    except ImportError:
        # If we get here, the package isn't installed yet
        print(f"Installing {package}...")
        
        # This runs a command like you would type in a terminal:
        # "pip install kiwipiepy --quiet"
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
        
        print(f"✓ {package} installed")
        return True

# Actually install kiwipiepy (if needed)
install_package('kiwipiepy')

# Now that it's installed, we can import and use it
from kiwipiepy import Kiwi

# Initialize Kiwi - this "wakes it up" and loads Korean language models
# This might take a few seconds the first time
kiwi = Kiwi()


# ===== CONFIGURATION SECTION =====
# ***** IMPORTANT: CHANGE THIS TO YOUR COLUMN NAME *****

TEXT_COLUMN = 'full_text'  # <<< CHANGE THIS to match your actual text column name


# POS = "Part of Speech" (품사 in Korean)
# These are the types of words we want to keep.
# **IMPORTANT**: Adjust this based on what you're analyzing!

POS_TAGS = [
    'NNG',  # General nouns (일반명사) - like "사람" (person), "제품" (product), "서비스" (service)
    'NNP'  # Proper nouns (고유명사) - like "서울" (Seoul), "삼성" (Samsung), "BTS"
    #'VV',   # Verbs (동사) - like "먹다" (eat), "사용하다" (use), "추천하다" (recommend)
    #'VA',   # Adjectives (형용사) - like "좋다" (good), "맛있다" (delicious), "비싸다" (expensive)
    #'MAG'   # General adverbs (일반부사) - like "매우" (very), "정말" (really), "빨리" (quickly)
]

# NOTE, the hastag (#) removes the tags above. You can add them back; take away the hashtags. Mind your commas.

# ===== UNDERSTANDING WHAT GETS KEPT vs REMOVED =====
#
# WITH POS tagging, we can systematically remove grammatical "noise":
# ❌ REMOVED: Particles (은/는/이/가/을/를/에/에서) - 20-30% of tokens
# ❌ REMOVED: Verb endings (었/습니다/아요/지만) - 15-20% of tokens  
# ❌ REMOVED: Bound nouns (것/수/바) - grammatical placeholders
# ❌ REMOVED: Pronouns (나/너/그) - often not informative
#
# KEPT: Only content words based on POS_TAGS above
#
# Example transformation:
# Input:  "이 제품은 정말 좋았습니다!"
# Tokens: 이(pronoun) 제품(noun) 은(particle) 정말(adverb) 좋(adjective) 았(ending) 습니다(ending)
# Output: "제품 정말 좋" (product really good)
#
# WITHOUT POS tagging (Orange native): You'd keep everything and treat
# "좋다", "좋았다", "좋습니다", "좋아요" as four completely different words!

# ===== HOW TO ADJUST POS_TAGS FOR YOUR ANALYSIS =====
#
# Different analyses need different word types. Here are common configurations:
#
# OPTION 1: NOUNS ONLY - For topic modeling, document clustering
# POS_TAGS = ['NNG', 'NNP']
# → Focuses on "WHAT" is being discussed
# → Example: "제품 서비스 가격" (product service price)
# → Best for: identifying subjects, categorizing documents, finding entities
#
# OPTION 2: NOUNS + ADJECTIVES - For sentiment analysis, reviews
# POS_TAGS = ['NNG', 'NNP', 'VA']  
# → Focuses on "WHAT" and "HOW IT'S EVALUATED"
# → Example: "제품 좋 서비스 친절 가격 비싸" (product good service kind price expensive)
# → Best for: customer feedback, product reviews, sentiment detection
# → **RECOMMENDED FOR MOST STUDENT PROJECTS**
#
# OPTION 3: NOUNS + VERBS + ADJECTIVES - For action + sentiment
# POS_TAGS = ['NNG', 'NNP', 'VV', 'VA']
# → Adds "WHAT'S HAPPENING" to the mix
# → Example: "제품 구매 좋 서비스 만족" (product purchase good service satisfy)
# → Best for: behavioral analysis, complaint detection, process descriptions
#
# OPTION 4: EVERYTHING - Maximum information
# POS_TAGS = ['NNG', 'NNP', 'VV', 'VA', 'MAG']
# → Keeps intensity markers too (very, really, extremely)
# → Can be noisy but preserves nuance
# → Best for: exploratory analysis, when you're not sure what matters yet
#
# **TIP**: Start with OPTION 2 (nouns + adjectives). This gives you the core content
# plus evaluative language, which is what most text analysis needs.
# You can always add 'VV' back if you need verbs later.

# ===== WHAT EACH TAG MEANS (Reference) =====
# Full list of tags you might want to add or understand:
#
# NOUNS:
#   NNG  - General noun (일반명사): 사람, 집, 책
#   NNP  - Proper noun (고유명사): 서울, 한국, 구글
#   NNB  - Bound noun (의존명사): 것, 수, 바 [usually skip these]
#
# VERBS & ADJECTIVES:
#   VV   - Verb (동사): 먹다, 가다, 만들다
#   VA   - Adjective (형용사): 좋다, 크다, 예쁘다
#   VX   - Auxiliary verb (보조용언): 있다, 없다, 않다
#
# MODIFIERS:
#   MAG  - General adverb (일반부사): 매우, 정말, 빨리
#   MAJ  - Conjunctive adverb (접속부사): 그러나, 그리고
#
# See full tag list: https://github.com/bab2min/kiwipiepy#품사-태그


# STOPWORDS - words that appear frequently but don't help us understand meaning
# Like English "the", "and", "or" - technically words, but not informative
# This list below is just for instructional purposes. For BA2/3 students with Dr. Denney/ Mr. v/d Pol,
# it is recommend ODM useres add an additional text preprocessing widget and select the provided stopwords list.
# You can also tell ODM via Python (here) to load and use a stopgap words document. So as to reduce an already complex thing, we are not doing that.
STOPWORDS = {
    '있다',   # to exist/have
    '없다',   # to not exist
    '되다',   # to become
    '하다',   # to do
    '그',     # that
    '저',     # that (formal)
    '이',     # this
    '것',     # thing
    '등',     # etc.
    '및',     # and
    '수',     # number/can
    '때',     # time/when
    '년',     # year
    '월',     # month
    '일',     # day
    '더',     # more
    '또',     # also/again
    '즉',     # that is
    '통해',   # through
    '위해'    # for (purpose)
}

# You can add more stopwords here based on your specific data!
# Just add them inside the curly braces with commas, like:
# '단어', '추가', '가능'


# ===== PREPROCESSING FUNCTIONS =====
# These are the "recipes" we'll use to clean and process the text

def clean_text(text):
    """
    This function removes messy stuff from text that we don't want:
    - URLs (web links)
    - Email addresses
    - @mentions (like on Twitter/X)
    - Special characters and punctuation
    - Extra spaces
    
    INPUT: Raw text (might be messy)
    OUTPUT: Cleaned text (only Korean characters and spaces)
    """
    
    # Handle missing/empty values
    if pd.isna(text):
        return ""
    
    # Make sure it's a string (not a number or other type)
    text = str(text)
    
    # Remove URLs - anything starting with http:// or https://
    # The pattern r'http[s]?://\S+' means:
    # - http or https
    # - ://
    # - followed by any non-space characters
    text = re.sub(r'http[s]?://\S+', '', text)
    
    # Remove email addresses (anything like text@text.com)
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove @mentions (like @username)
    text = re.sub(r'@\w+', '', text)
    
    # Keep ONLY these characters:
    # - \w: Regular word characters (letters, numbers)
    # - \s: Spaces
    # - \u3131-\u3163: Korean Hangul Jamo (individual consonants/vowels)
    # - \uac00-\ud7a3: Korean Hangul syllables (complete characters like 가, 나, 다)
    # - \u1100-\u11ff: More Korean Hangul components
    # Everything else gets replaced with a space
    text = re.sub(r'[^\w\s\u3131-\u3163\uac00-\ud7a3\u1100-\u11ff]', ' ', text)
    
    # Replace multiple spaces with a single space, and remove spaces at start/end
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def preprocess(text):
    """
    This is the MAIN preprocessing function that does everything:
    1. Cleans the text
    2. Breaks it into words with POS tags
    3. Filters for important word types
    4. Removes stopwords
    5. Removes very short words
    
    INPUT: One piece of text (like one tweet or one review)
    OUTPUT: Processed text ready for analysis
    """
    
    # Step 1: Clean the text
    text = clean_text(text)
    
    # If nothing left after cleaning, return empty string
    if not text:
        return ""
    
    # Step 2: Use Kiwi to tokenize and POS tag
    # "Tokenize" means breaking text into individual words/morphemes
    # Each token has a .form (the word) and .tag (its POS type)
    tokens = kiwi.tokenize(text)
    
    # Step 3: Keep only the word types we want (from POS_TAGS above)
    # This is a "list comprehension" - a compact way to filter a list
    # It reads: "keep token.form IF token.tag is in our POS_TAGS list"
    morphemes = [token.form for token in tokens if token.tag in POS_TAGS]
    
    # Step 4 & 5: Remove stopwords and short words (less than 2 characters)
    # Again using list comprehension to filter
    # Conditions: word NOT in stopwords AND word length > 1
    filtered = [w for w in morphemes if w not in STOPWORDS and len(w) > 1]
    
    # Join the remaining words back together with spaces
    result = ' '.join(filtered)
    
    return result


# ===== MAIN DATA PROCESSING =====
# This is where we actually process your Orange data

# Orange passes data to this script as a variable called "in_data"
# We need to extract the text column from it

try:
    # Method 1: Try to get documents if data is in Corpus format
    text_data = in_data.documents
except AttributeError:
    # Method 2: If that doesn't work, get the specific text column by name
    # Find which column number matches our TEXT_COLUMN name
    text_column_index = in_data.domain.index(TEXT_COLUMN)
    
    # Extract all the text from that column
    # This creates a list where each item is one row's text
    text_data = [str(row[text_column_index]) for row in in_data]


# Now process every single piece of text using our preprocess function
# This is another list comprehension: 
# "For each text in text_data, run preprocess(text) on it"
processed = [preprocess(text) for text in text_data]


# ===== CREATE OUTPUT FOR ORANGE =====
# We need to add our processed text back to the Orange table as a new column

# Create a new variable (column) called 'processed_text'
new_var = StringVariable('processed_text')

# Create a new domain (think of this as the "structure" of the table)
# It includes:
# - All original attributes (regular columns)
# - All original class variables (target/label columns)
# - All original meta attributes PLUS our new processed_text column
new_domain = Domain(
    in_data.domain.attributes,      # Keep all original columns
    in_data.domain.class_vars,      # Keep any target variables
    in_data.domain.metas + (new_var,)  # Add our new column to meta attributes
)

# Transform the input data to match our new domain structure
out_data = in_data.transform(new_domain)

# Fill in our new column with the processed text
# We need to "unlock" the data temporarily to modify it
with out_data.unlocked():
    out_data.get_column(new_var)[:] = processed

# Print a success message so you know it worked!
print(f"✓ Processed {len(processed)} documents")

# The variable "out_data" is automatically passed to the next Orange widget


# ===== YOU'RE DONE! =====
# The output will now have a new column called 'processed_text' with
# your cleaned, tokenized, POS-filtered Korean text ready for analysis.
#
# NEXT STEPS:
# - You will probably need to connect a Corpus widget AGAIN so as to specify the processed text (processed_text).
# - Connect this to Word Cloud to visualize common words
# - Use it with Topic Modeling to find themes
# - Feed it into Sentiment Analysis
# - Create a Bag of Words or TF-IDF columns for analysis
# - Etc.
#
# TROUBLESHOOTING:
# - Error about TEXT_COLUMN? Make sure you changed it to your actual column name
# - No output? Check that your text column has data
# - Strange results? Try adjusting POS_TAGS or adding more STOPWORDS
# - Still stuck? Go to the DH lab or contact an instructor