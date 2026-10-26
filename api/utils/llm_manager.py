import os

from langchain_google_genai import GoogleGenerativeAI


class LLMManager:

    @staticmethod
    def get_gemini_llm():
        gemini_api_key = os.getenv("GOOGLE_API_KEY")
        if not gemini_api_key:
            raise ValueError("Gemini API Key not provided. Please provide GOOGLE_API_KEY as an environment variable")
        return GoogleGenerativeAI(model="gemini-3.5-flash-lite", api_key=gemini_api_key)