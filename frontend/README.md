# Candidate Profile Frontend

A minimal React frontend for the candidate profile playground API.

## Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Ensure the backend is running on `http://localhost:8000`

3. Start the development server:
```bash
npm start
```

The app will open at `http://localhost:3000`

## Features

- **Profile List**: Browse all candidate profiles with basic info and skills
- **Search**: Search profiles by name, skills, or description
- **Profile Details**: View complete profile information including projects and work experience
- **Skills Filter**: Filter projects by specific skills
- **Responsive Design**: Works on desktop and mobile devices

## API Endpoints Used

- `GET /api/v1/profiles` - List all profiles
- `GET /api/v1/profile/{id}` - Get profile details
- `GET /api/v1/search?q={query}` - Search profiles
- `GET /api/v1/projects?skill={skill}` - Filter projects by skill
- `GET /api/v1/skills/top` - Get top skills
- `GET /api/v1/health` - Health check

## Component Structure

- `App.js` - Main application component with state management
- `components/ProfileList.js` - Grid of profile cards
- `components/ProfileDetail.js` - Detailed profile view
- `components/SearchBar.js` - Search functionality with debouncing
- `components/SkillsFilter.js` - Skills filter sidebar
- `components/ProjectsList.js` - Projects filtered by skill
- `api.js` - API service layer

## Styling

Uses vanilla CSS with a clean, functional design focused on usability over aesthetics.