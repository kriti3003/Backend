import React from 'react';

const ProfileDetail = ({ profile, onBack }) => {
  if (!profile) {
    return <div className="loading">Loading profile...</div>;
  }

  return (
    <div className="profile-detail">
      <div className="profile-detail-header">
        <h1>{profile.name}</h1>
        <button onClick={onBack} className="back-button">
          ← Back to List
        </button>
      </div>
      
      <div className="email">{profile.email}</div>
      
      {profile.description && (
        <div className="description">{profile.description}</div>
      )}
      
      {/* External Links */}
      {(profile.github_url || profile.linkedin_url || profile.portfolio_url) && (
        <div className="profile-section">
          <h2>Links</h2>
          <div className="profile-external-links">
            {profile.github_url && (
              <a 
                href={profile.github_url} 
                className="external-link"
                target="_blank"
                rel="noopener noreferrer"
              >
                GitHub
              </a>
            )}
            {profile.linkedin_url && (
              <a 
                href={profile.linkedin_url} 
                className="external-link"
                target="_blank"
                rel="noopener noreferrer"
              >
                LinkedIn
              </a>
            )}
            {profile.portfolio_url && (
              <a 
                href={profile.portfolio_url} 
                className="external-link"
                target="_blank"
                rel="noopener noreferrer"
              >
                Portfolio
              </a>
            )}
          </div>
        </div>
      )}
      
      {/* Skills */}
      {profile.skills && profile.skills.length > 0 && (
        <div className="profile-section">
          <h2>Skills</h2>
          <div className="skills-grid">
            {profile.skills.map((skill) => (
              <div key={skill.id} className="skill-item">
                {skill.name}
              </div>
            ))}
          </div>
        </div>
      )}
      
      {/* Projects */}
      {profile.projects && profile.projects.length > 0 && (
        <div className="profile-section">
          <h2>Projects</h2>
          <div className="projects-list">
            {profile.projects.map((project) => (
              <div key={project.id} className="project-item">
                <h3>{project.title}</h3>
                {project.description && <p>{project.description}</p>}
              </div>
            ))}
          </div>
        </div>
      )}
      
      {/* Work Experience */}
      {profile.work_experiences && profile.work_experiences.length > 0 && (
        <div className="profile-section">
          <h2>Work Experience</h2>
          <div className="work-experience-list">
            {profile.work_experiences.map((work) => (
              <div key={work.id} className="work-item">
                <h3>{work.position}</h3>
                <div className="company">{work.company}</div>
                {work.description && <p>{work.description}</p>}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ProfileDetail;