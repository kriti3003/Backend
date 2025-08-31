import React from 'react';

const ProfileList = ({ profiles, onProfileSelect }) => {
  if (!profiles || profiles.length === 0) {
    return (
      <div className="empty-state">
        <h3>No profiles found</h3>
        <p>Try adjusting your search criteria or check that the backend is running.</p>
      </div>
    );
  }

  return (
    <div className="profile-list">
      {profiles.map((profile) => (
        <div
          key={profile.id}
          className="profile-card"
          onClick={() => onProfileSelect(profile.id)}
        >
          <h3>{profile.name}</h3>
          <div className="email">{profile.email}</div>
          
          {profile.description && (
            <div className="description">{profile.description}</div>
          )}
          
          {profile.skills && profile.skills.length > 0 && (
            <div className="profile-skills">
              {profile.skills.slice(0, 5).map((skill) => (
                <span key={skill.id} className="skill-tag">
                  {skill.name}
                </span>
              ))}
              {profile.skills.length > 5 && (
                <span className="skill-tag">+{profile.skills.length - 5} more</span>
              )}
            </div>
          )}
          
          <div className="profile-links">
            {profile.github_url && (
              <a 
                href={profile.github_url} 
                className="profile-link"
                onClick={(e) => e.stopPropagation()}
                target="_blank"
                rel="noopener noreferrer"
              >
                GitHub
              </a>
            )}
            {profile.linkedin_url && (
              <a 
                href={profile.linkedin_url} 
                className="profile-link"
                onClick={(e) => e.stopPropagation()}
                target="_blank"
                rel="noopener noreferrer"
              >
                LinkedIn
              </a>
            )}
            {profile.portfolio_url && (
              <a 
                href={profile.portfolio_url} 
                className="profile-link"
                onClick={(e) => e.stopPropagation()}
                target="_blank"
                rel="noopener noreferrer"
              >
                Portfolio
              </a>
            )}
          </div>
        </div>
      ))}
    </div>
  );
};

export default ProfileList;