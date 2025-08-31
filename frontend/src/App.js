import React, { useState, useEffect } from 'react';
import './App.css';
import ProfileList from './components/ProfileList';
import ProfileDetail from './components/ProfileDetail';
import SearchBar from './components/SearchBar';
import SkillsFilter from './components/SkillsFilter';
import ProjectsList from './components/ProjectsList';
import apiService from './api';

function App() {
  const [profiles, setProfiles] = useState([]);
  const [selectedProfile, setSelectedProfile] = useState(null);
  const [topSkills, setTopSkills] = useState([]);
  const [selectedSkill, setSelectedSkill] = useState('');
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');

  // Load initial data
  useEffect(() => {
    const loadInitialData = async () => {
      try {
        setLoading(true);
        setError(null);
        
        // Load profiles and top skills
        const [profilesResponse, skillsResponse] = await Promise.all([
          apiService.getProfiles(),
          apiService.getTopSkills()
        ]);
        
        setProfiles(profilesResponse.data);
        setTopSkills(skillsResponse.data);
      } catch (err) {
        console.error('Error loading initial data:', err);
        setError('Failed to load data. Please ensure the backend is running on http://localhost:8000');
      } finally {
        setLoading(false);
      }
    };

    loadInitialData();
  }, []);

  // Handle search
  const handleSearch = async (query) => {
    try {
      setSearchQuery(query);
      setSelectedProfile(null);
      
      if (!query.trim()) {
        // If search is empty, reload all profiles
        const response = await apiService.getProfiles();
        setProfiles(response.data);
      } else {
        // Search profiles
        const response = await apiService.searchProfiles(query);
        setProfiles(response.data);
      }
    } catch (err) {
      console.error('Error searching profiles:', err);
      setError('Failed to search profiles');
    }
  };

  // Handle skill filter
  const handleSkillFilter = async (skill) => {
    try {
      setSelectedSkill(skill);
      
      if (!skill) {
        setProjects([]);
        return;
      }
      
      const response = await apiService.getProjectsBySkill(skill);
      setProjects(response.data);
    } catch (err) {
      console.error('Error filtering projects by skill:', err);
      setError('Failed to filter projects');
    }
  };

  // Handle profile selection
  const handleProfileSelect = async (profileId) => {
    try {
      const response = await apiService.getProfile(profileId);
      setSelectedProfile(response.data);
    } catch (err) {
      console.error('Error loading profile details:', err);
      setError('Failed to load profile details');
    }
  };

  const clearSelection = () => {
    setSelectedProfile(null);
  };

  if (loading) {
    return <div className="app"><div className="loading">Loading...</div></div>;
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>Candidate Profile Playground</h1>
      </header>

      {error && (
        <div className="error-banner">
          {error}
          <button onClick={() => setError(null)}>×</button>
        </div>
      )}

      <main className="app-main">
        <div className="sidebar">
          <SearchBar onSearch={handleSearch} />
          
          <SkillsFilter 
            skills={topSkills} 
            selectedSkill={selectedSkill}
            onSkillSelect={handleSkillFilter}
          />
          
          {selectedSkill && projects.length > 0 && (
            <ProjectsList projects={projects} />
          )}
        </div>

        <div className="main-content">
          {selectedProfile ? (
            <ProfileDetail 
              profile={selectedProfile} 
              onBack={clearSelection}
            />
          ) : (
            <>
              <div className="profiles-header">
                <h2>
                  {searchQuery ? `Search Results for "${searchQuery}"` : 'All Profiles'}
                  {profiles.length > 0 && ` (${profiles.length})`}
                </h2>
              </div>
              
              <ProfileList 
                profiles={profiles} 
                onProfileSelect={handleProfileSelect}
              />
            </>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;