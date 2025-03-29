import openai
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
from dotenv import load_dotenv

load_dotenv()

class ContentGenerator:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        
    def generate(self, subject, topic, difficulty):
        """
        Generate educational content based on subject and topic
        """
        if subject.lower() == 'coding':
            return self._generate_coding_content(topic, difficulty)
        elif subject.lower() == 'visual arts':
            return self._generate_visual_arts_content(topic, difficulty)
        elif subject.lower() == 'performing arts':
            return self._generate_performing_arts_content(topic, difficulty)
        elif subject.lower() == 'financial literacy':
            return self._generate_financial_literacy_content(topic, difficulty)
        elif subject.lower() == 'science':
            return self._generate_science_content(topic, difficulty)
        else:
            raise ValueError(f"Unsupported subject: {subject}")

    def _generate_coding_content(self, topic, difficulty):
        """Generate coding tutorials and examples"""
        prompt = f"Create a coding tutorial for {topic} at {difficulty} level. Include code examples and explanations."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert programming instructor."},
                {"role": "user", "content": prompt}
            ]
        )
        return {
            'type': 'coding',
            'content': response.choices[0].message.content,
            'topic': topic,
            'difficulty': difficulty
        }

    def _generate_visual_arts_content(self, topic, difficulty):
        """Generate visual arts tutorials and design ideas"""
        prompt = f"Create a visual arts tutorial for {topic} at {difficulty} level. Include step-by-step instructions and design principles."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert visual arts instructor."},
                {"role": "user", "content": prompt}
            ]
        )
        return {
            'type': 'visual_arts',
            'content': response.choices[0].message.content,
            'topic': topic,
            'difficulty': difficulty
        }

    def _generate_performing_arts_content(self, topic, difficulty):
        """Generate performing arts tutorials and exercises"""
        prompt = f"Create a performing arts tutorial for {topic} at {difficulty} level. Include exercises and performance tips."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert performing arts instructor."},
                {"role": "user", "content": prompt}
            ]
        )
        return {
            'type': 'performing_arts',
            'content': response.choices[0].message.content,
            'topic': topic,
            'difficulty': difficulty
        }

    def _generate_financial_literacy_content(self, topic, difficulty):
        """Generate financial literacy lessons and examples"""
        prompt = f"Create a financial literacy lesson for {topic} at {difficulty} level. Include practical examples and real-world applications."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert financial literacy instructor."},
                {"role": "user", "content": prompt}
            ]
        )
        return {
            'type': 'financial_literacy',
            'content': response.choices[0].message.content,
            'topic': topic,
            'difficulty': difficulty
        }

    def _generate_science_content(self, topic, difficulty):
        """Generate science lessons and experiments"""
        prompt = f"Create a science lesson for {topic} at {difficulty} level. Include explanations, examples, and simple experiments."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert science instructor."},
                {"role": "user", "content": prompt}
            ]
        )
        return {
            'type': 'science',
            'content': response.choices[0].message.content,
            'topic': topic,
            'difficulty': difficulty
        } 