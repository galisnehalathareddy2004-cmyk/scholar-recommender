Set-Content -Path README.md -Value @"
# Smart Scholarship & Financial Aid Recommender

A system that collects student profiles and recommends ranked scholarships based on eligibility, deadlines, and benefits.

## Folders
- backend/   – FastAPI code
- frontend/  – React app
- scrapers/  – Web scraping (Selenium/BS4)
- nlp/       – Parsing, ranking logic
- docs/      – PPT, diagrams
- data/      – Seed/sample datasets

## Quick Start
1) Backend: FastAPI + PostgreSQL
2) Scrapers: load scholarships into DB
3) API: return ranked scholarships per student
4) Frontend: forms + results UI
"@
