import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const apiService = {
  // Health check
  healthCheck: () => api.get('/health'),
  
  // Profile endpoints
  getProfiles: () => api.get('/profiles'),
  getProfile: (id) => api.get(`/profile/${id}`),
  
  // Search functionality
  searchProfiles: (query) => api.get(`/search?q=${encodeURIComponent(query)}`),
  
  // Skills and projects
  getTopSkills: () => api.get('/skills/top'),
  getProjectsBySkill: (skill) => api.get(`/projects?skill=${encodeURIComponent(skill)}`),
};

export default apiService;