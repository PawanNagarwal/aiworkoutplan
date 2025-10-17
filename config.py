"""
Configuration constants and settings for the AI Workout Plan Generator
"""

# GPT-4o Pricing Constants (per 1M tokens)
GPT4O_INPUT_COST_PER_MILLION = 2.5  # $2.5 per 1M input tokens
GPT4O_OUTPUT_COST_PER_MILLION = 10.0  # $10.0 per 1M output tokens

# Streamlit page configuration
PAGE_CONFIG = {
    "page_title": "AI Workout Plan Generator",
    "page_icon": "💪",
    "layout": "wide",
    "initial_sidebar_state": "collapsed"
}

# Form options
FITNESS_LEVELS = ["Beginner", "Intermediate", "Advanced"]
GOAL_OPTIONS = ["Muscle Gain", "Weight Loss", "General Fitness", "Strength Building", "Endurance", "Flexibility"]
TRAINING_DAYS_OPTIONS = [3, 4, 5, 6, 7]
DURATION_OPTIONS = [30, 45, 60, 75, 90]
TARGET_AREA_OPTIONS = ["Chest", "Back", "Shoulders", "Arms", "Core", "Legs", "Glutes", "Full Body"]
EQUIPMENT_OPTIONS = [
    "Dumbbells", "Barbells", "Kettlebells", "Resistance Bands",
    "Pull-up Bar", "Gym Machine", "Bodyweight Only", "Yoga Mat", "Stability Ball"
]
PREFERENCE_OPTIONS = [
    "Strength", "Cardio", "Flexibility", "HIIT/Circuit", "Mixed", "Calisthenics", "Pilates", "Yoga"
]

# Fitness level descriptions
FITNESS_LEVEL_DESCRIPTIONS = {
    "Beginner": "New to structured exercise, learning proper form",
    "Intermediate": "Regular exercise routine, familiar with basic movements",
    "Advanced": "Experienced with complex exercises and training principles"
}

# Gender options
GENDER_OPTIONS = ["Male", "Female", "Other"]
