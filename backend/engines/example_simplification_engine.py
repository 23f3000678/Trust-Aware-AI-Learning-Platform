"""
Example usage of SimplificationEngine for Trust-Aware AI Learning Platform MVP.

This script demonstrates how to use the SimplificationEngine to simplify
complex AI responses for better comprehension.
"""

from backend.engines.simplification_engine import SimplificationEngine


def main():
    """Demonstrate SimplificationEngine usage."""
    
    # Initialize the engine (uses GROQ_API_KEY from environment)
    engine = SimplificationEngine()
    
    # Example 1: Simplify a complex technical response
    print("=" * 70)
    print("Example 1: Simplifying Technical Content")
    print("=" * 70)
    
    complex_text = """
    Quantum entanglement is a physical phenomenon that occurs when a group of 
    particles are generated, interact, or share spatial proximity in a way such 
    that the quantum state of each particle of the group cannot be described 
    independently of the state of the others, including when the particles are 
    separated by a large distance. The topic of quantum entanglement is at the 
    heart of the disparity between classical and quantum physics: entanglement 
    is a primary feature of quantum mechanics not present in classical mechanics.
    """
    
    try:
        result = engine.simplify(
            text=complex_text.strip(),
            response_id="example-response-001"
        )
        
        print("\nOriginal Text:")
        print(result.original_text)
        print("\nSimplified Text:")
        print(result.simplified_text)
        print(f"\nResponse ID: {result.response_id}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Simplify a response with uncertainty markers
    print("\n" + "=" * 70)
    print("Example 2: Simplifying Response with Uncertainty Markers")
    print("=" * 70)
    
    uncertain_text = """
    The exact date of the invention of the printing press is [UNCERTAIN]believed 
    to be around 1440[/UNCERTAIN], when Johannes Gutenberg developed movable type 
    printing in Europe. [UNCERTAIN]Some historians suggest it may have been as 
    early as 1436[/UNCERTAIN], but the first major work, the Gutenberg Bible, 
    was completed around 1455.
    """
    
    try:
        result = engine.simplify(
            text=uncertain_text.strip(),
            response_id="example-response-002"
        )
        
        print("\nOriginal Text:")
        print(result.original_text)
        print("\nSimplified Text:")
        print(result.simplified_text)
        print(f"\nResponse ID: {result.response_id}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Simplify a medical/scientific explanation
    print("\n" + "=" * 70)
    print("Example 3: Simplifying Medical Content")
    print("=" * 70)
    
    medical_text = """
    Photosynthesis is the process by which green plants and certain other 
    organisms transform light energy into chemical energy. During photosynthesis 
    in green plants, light energy is captured and used to convert water, carbon 
    dioxide, and minerals into oxygen and energy-rich organic compounds through 
    a series of complex biochemical reactions involving chlorophyll molecules.
    """
    
    try:
        result = engine.simplify(
            text=medical_text.strip(),
            response_id="example-response-003"
        )
        
        print("\nOriginal Text:")
        print(result.original_text)
        print("\nSimplified Text:")
        print(result.simplified_text)
        print(f"\nResponse ID: {result.response_id}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 70)
    print("Examples completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()
