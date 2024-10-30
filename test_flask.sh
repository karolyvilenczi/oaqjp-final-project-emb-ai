#!/bin/bash

curl -X POST http://localhost:5000/emotionDetector -H "Content-Type: application/json"  -d  "text=I love my life."