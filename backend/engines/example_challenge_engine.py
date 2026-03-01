"""
Example usage of ChallengeEngine for Trust-Aware AI Learning Platform MVP.

This demonstrates how to generate verification challenges based on Q&A pairs.
"""

import os
from dotenv import load_dotenv
from backend.engines.challenge_engine import ChallengeEngine


def main():
    """Demonstrate ChallengeEngine usage."""
    # Load environment variables
    load_dotenv()
    
    # Ensure API key is set
    if not os.getenv("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY environment variable not set")
        print("Please set it in your .env file or environment")
        return
    
    # Initialize the engine
    print("Initializing ChallengeEngine...")
    engine = ChallengeEngine()
    print(f"Using model: {engine.model}\n")
    
    # Example 1: Generate challenge for a Python question
    print("=" * 60)
    print("Example 1: Python Programming Question")
    print("=" * 60)
    
    query_text = "What is Python and why is it popular?"
    response_text = """Python is a high-level, interpreted programming language known for its simplicity and readability. It's popular because:
1. Easy to learn syntax that resembles natural language
2. Extensive standard library and third-party packages
3. Versatile - used for web development, data science, AI, automation
4. Strong community support and documentation
5. Cross-platform compatibility"""
    response_id = "resp-python-001"
    
    print(f"Query: {query_text}")
    print(f"\nResponse: {response_text}")
    print("\nGenerating verification challenge...")
    
    try:
        challenge = engine.generate_challenge(
            response_text=response_text,
            query_text=query_text,
            response_id=response_id
        )
        
        print(f"\nChallenge ID: {challenge.challenge_id}")
        print(f"Related Response ID: {challenge.related_response_id}")
        print(f"Verification Question: {challenge.question_text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Generate challenge for a science question
    print("\n" + "=" * 60)
    print("Example 2: Science Question")
    print("=" * 60)
    
    query_text = "How does photosynthesis work?"
    response_text = """Photosynthesis is the process by which plants convert light energy into chemical energy. [UNCERTAIN]The process occurs primarily in the chloroplasts of plant cells[/UNCERTAIN]. It involves two main stages:
1. Light-dependent reactions: Light energy is captured and converted to ATP and NADPH
2. Light-independent reactions (Calvin cycle): CO2 is fixed into glucose using ATP and NADPH
The overall equation is: 6CO2 + 6H2O + light energy → C6H12O6 + 6O2"""
    response_id = "resp-science-001"
    
    print(f"Query: {query_text}")
    print(f"\nResponse: {response_text}")
    print("\nGenerating verification challenge...")
    
    try:
        challenge = engine.generate_challenge(
            response_text=response_text,
            query_text=query_text,
            response_id=response_id
        )
        
        print(f"\nChallenge ID: {challenge.challenge_id}")
        print(f"Related Response ID: {challenge.related_response_id}")
        print(f"Verification Question: {challenge.question_text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Generate challenge for a history question
    print("\n" + "=" * 60)
    print("Example 3: History Question")
    print("=" * 60)
    
    query_text = "When did World War II end?"
    response_text = """World War II ended in 1945. The war in Europe ended on May 8, 1945 (V-E Day) when Germany surrendered. The war in the Pacific ended on September 2, 1945 (V-J Day) when Japan formally surrendered aboard the USS Missouri."""
    response_id = "resp-history-001"
    
    print(f"Query: {query_text}")
    print(f"\nResponse: {response_text}")
    print("\nGenerating verification challenge...")
    
    try:
        challenge = engine.generate_challenge(
            response_text=response_text,
            query_text=query_text,
            response_id=response_id
        )
        
        print(f"\nChallenge ID: {challenge.challenge_id}")
        print(f"Related Response ID: {challenge.related_response_id}")
        print(f"Verification Question: {challenge.question_text}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 60)
    print("Challenge generation examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
