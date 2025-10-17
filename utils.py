"""
Utility functions for token calculation, file generation, and session management
"""

import json
import streamlit as st
from datetime import datetime
from typing import Dict, List



def create_workout_json_output(form_data: Dict, days_data: List[Dict]) -> str:
    """Create comprehensive JSON output for workout plan"""
    
    # Calculate weekly stats
    total_exercises = sum(len(day['exercises']) for day in days_data)
    total_duration = sum(day.get('workout_duration', 0) for day in days_data)
    
    # Process days data
    processed_days = []
    for day_data in days_data:
        day_exercises = []
        
        for exercise in day_data.get('exercises', []):
            exercise_info = {
                "exercise_name": exercise.get('exercise_name', ''),
                "exercise_type": exercise.get('exercise_type', ''),
                "equipment_required": exercise.get('equipment_required', ''),
                "target_muscle_group": exercise.get('target_muscle_group', ''),
                "parameters": {
                    "total_sets": exercise.get('total_sets', 1),
                    "reps": exercise.get('reps', ''),
                    "tempo": exercise.get('tempo', ''),
                    "rest_time": exercise.get('rest_time', ''),
                    "weight": exercise.get('weight', ''),
                    "speed_level": exercise.get('speed_level', ''),
                    "breathing_pattern": exercise.get('breathing_pattern', ''),
                    "superset_indicator": exercise.get('superset_indicator', 'None')
                }
            }
            day_exercises.append(exercise_info)
        
        processed_days.append({
            "day": day_data.get('title', f"Day {day_data.get('day', 1)}"),
            "workout_type": day_data.get('workout_type', 'Workout'),
            "workout_duration": day_data.get('workout_duration', 0),
            "total_exercises": len(day_exercises),
            "exercises": day_exercises
        })
    
    # Create the complete JSON structure
    workout_json = {
        "workout_plan": {
            "plan_name": f"{form_data.get('training_days_per_week', form_data.get('weekly_frequency', 3))}-Day {form_data['goal']} Workout Plan",
            "meta_data": {
                "name": form_data.get('name', ''),
                "goal": form_data.get('goal', ''),
                "fitness_level": form_data.get('fitness_level', ''),
                "age": form_data.get('age', 0),
                "gender": form_data.get('gender', ''),
                "weight": form_data.get('weight', 0),
                "height": form_data.get('height', 0),
                "workout_preferences": form_data.get('workout_preferences', []),
                "training_days_per_week": form_data.get('training_days_per_week', form_data.get('weekly_frequency', 3)),
                "session_duration": form_data.get('session_duration', form_data.get('duration_per_session', 45)),
                "available_equipment": form_data.get('available_equipment', []),
                "target_areas": form_data.get('target_areas', []),
                "health_limitations": form_data.get('health_limitations', ''),
                "exercises_to_avoid": form_data.get('exercises_to_avoid', ''),
                "additional_notes": form_data.get('additional_notes', '')
            },
            "days": processed_days,
            "weekly_summary": {
                "total_workout_days": len(days_data),
                "total_exercises": total_exercises,
                "total_weekly_duration_minutes": total_duration,
                "average_duration_per_session": round(total_duration / len(days_data)) if days_data else 0
            },
            "audit_info": {
                "created_by": "AI Workout Plan Generator",
                "created_on": datetime.now().isoformat(),
                "updated_by": None,
                "updated_on": None
            }
        }
    }
    
    return json.dumps(workout_json, indent=2, ensure_ascii=False)

def create_text_format(days_data: List[Dict], user_data: Dict) -> str:
    """Create a formatted text version of the workout plan"""
    text_content = []
    
    # Header
    text_content.append("=" * 70)
    text_content.append("💪 PERSONALIZED WORKOUT PLAN")
    text_content.append("=" * 70)
    text_content.append("")
    
    # User profile summary
    text_content.append("👤 PROFILE SUMMARY:")
    text_content.append("-" * 30)
    text_content.append(f"Name: {user_data.get('name', 'N/A')}")
    text_content.append(f"Age: {user_data.get('age', 'N/A')} years")
    text_content.append(f"Gender: {user_data.get('gender', 'N/A').title()}")
    text_content.append(f"Weight: {user_data.get('weight', 'N/A')} kg")
    text_content.append(f"Height: {user_data.get('height', 'N/A')} cm")
    text_content.append(f"Fitness Goal: {user_data.get('goal', 'N/A')}")
    text_content.append(f"Fitness Level: {user_data.get('fitness_level', 'N/A')}")
    text_content.append(f"Training Days: {user_data.get('training_days_per_week', user_data.get('weekly_frequency', 'N/A'))} days/week")
    text_content.append(f"Session Duration: {user_data.get('session_duration', user_data.get('duration_per_session', 'N/A'))} minutes")
    
    if user_data.get('workout_preferences'):
        text_content.append(f"Workout Preferences: {', '.join(user_data['workout_preferences'])}")
    
    if user_data.get('available_equipment'):
        text_content.append(f"Available Equipment: {', '.join(user_data['available_equipment'])}")
    
    if user_data.get('target_areas'):
        text_content.append(f"Target Areas: {', '.join(user_data['target_areas'])}")
    
    if user_data.get('health_limitations'):
        text_content.append(f"Health Limitations: {user_data['health_limitations']}")
    
    text_content.append("")
    text_content.append("")
    
    # Daily workout plans
    for day_data in days_data:
        text_content.append("=" * 70)
        text_content.append(f"🏋️ {day_data['title']}")
        text_content.append(f"Workout Type: {day_data['workout_type']}")
        text_content.append(f"Duration: {day_data['workout_duration']} minutes")
        text_content.append("=" * 70)
        text_content.append("")
        
        for exercise in day_data['exercises']:
            text_content.append(f"💪 {exercise['exercise_name'].upper()}")
            text_content.append("-" * 50)
            
            if exercise.get('exercise_type'):
                text_content.append(f"Type: {exercise['exercise_type']}")
            if exercise.get('target_muscle_group'):
                text_content.append(f"Target Muscles: {exercise['target_muscle_group']}")
            if exercise.get('equipment_required'):
                text_content.append(f"Equipment: {exercise['equipment_required']}")
            
            # Exercise parameters
            params = []
            if exercise.get('reps'):
                params.append(f"Reps: {exercise['reps']}")
            if exercise.get('rest_time'):
                params.append(f"Rest: {exercise['rest_time']}")
            if exercise.get('weight'):
                params.append(f"Weight: {exercise['weight']}")
            if exercise.get('tempo'):
                params.append(f"Tempo: {exercise['tempo']}")
            
            if params:
                text_content.append(f"Parameters: {' | '.join(params)}")
            
            if exercise.get('breathing_pattern'):
                text_content.append(f"Breathing: {exercise['breathing_pattern']}")
            
            text_content.append("")
        
        text_content.append("")
    
    # Footer
    text_content.append("=" * 70)
    text_content.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    text_content.append("Generated by: AI Workout Plan Generator")
    text_content.append("=" * 70)
    
    return "\n".join(text_content)
