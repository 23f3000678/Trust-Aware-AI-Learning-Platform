"""
Example usage of AIProcessingLayer for Trust-Aware AI Learning Platform.

This script demonstrates how to use the AIProcessingLayer to generate
AI responses with uncertainty tagging and confidence scoring.

Requirements:
- Set GROQ_API_KEY environment variable
- Install dependencies: GROQ, python-dotenv, pydantic
"""

import os
from dotenv import load_dotenv
from backend.engines.ai_processing_layer import AIProcessingLayer

# Load environment variables
load_dotenv()


def main():
    """Demonstrate AIProcessingLayer usage."""
    
    # Check for API key
    if not os.getenv("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY environment variable not set")
        print("Please set it in your .env file or environment")
        return
    
    # Initialize the AI Processing Layer
    print("Initializing AI Processing Layer...")
    layer = AIProcessingLayer()
    
    # Example queries
    queries = [
        "What is machine learning?",
        "When was Python programming language created?",
        "How does quantum computing work?",
    ]
    
    print("\n" + "="*80)
    print("AI Processing Layer Demo - Trust-Aware Responses")
    print("="*80 + "\n")
    
    for i, query in enumerate(queries, 1):
        print(f"\n{'─'*80}")
        print(f"Query {i}: {query}")
        print('─'*80)
        
        try:
            # Query the LLM
            response = layer.query_llm(query)
            
            # Display response
            print(f"\n📝 Response:")
            print(f"   {response.response_text}\n")
            
            # Display confidence information
            print(f"📊 Confidence Score: {response.confidence.score}/100")
            if response.confidence.should_warn:
                print("   ⚠️  WARNING: Low confidence - use with caution")
            
            print(f"\n💭 Justification:")
            print(f"   {response.confidence.justification}")
            
            # Display breakdown
            print(f"\n🔍 Confidence Breakdown:")
            print(f"   • Question Clarity: {response.confidence.breakdown.question_clarity}")
            print(f"   • Topic Complexity: {response.confidence.breakdown.topic_complexity}")
            print(f"   • Missing Information: {response.confidence.breakdown.missing_information}")
            
            # Display metadata
            print(f"\n🆔 Response ID: {response.response_id}")
            print(f"⏰ Timestamp: {response.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Check for uncertainty tags
            if "[UNCERTAIN]" in response.response_text:
                print("\n⚡ Note: This response contains uncertain statements marked with [UNCERTAIN] tags")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
    
    print("\n" + "="*80)
    print("Demo complete!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
