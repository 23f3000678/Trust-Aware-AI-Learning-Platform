"""
Quick start script for running the FastAPI server.

Usage:
    python run_server.py
    
Or with custom host/port:
    python run_server.py --host 0.0.0.0 --port 8080
"""

import argparse
import uvicorn


def main():
    parser = argparse.ArgumentParser(
        description="Run the Trust-Aware AI Learning Platform API server"
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind to (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind to (default: 8000)"
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for development"
    )
    
    args = parser.parse_args()
    
    print(f"Starting server at http://{args.host}:{args.port}")
    print(f"API docs available at http://{args.host}:{args.port}/docs")
    print(f"Health check at http://{args.host}:{args.port}/health")
    print("\nPress CTRL+C to stop the server\n")
    
    uvicorn.run(
        "backend.api.main:app",
        host=args.host,
        port=args.port,
        reload=args.reload
    )


if __name__ == "__main__":
    main()
