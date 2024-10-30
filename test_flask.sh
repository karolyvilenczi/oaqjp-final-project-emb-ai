#!/bin/bash

# curl -X POST http://localhost:5000/emotionDetector -H "Content-Type: application/json"  -d  "text=I love my life."

curl -X POST http://127.0.0.1:5000/emotionDetector -H "Content-Type: application/json" -d '{"text": "I love my life"}'