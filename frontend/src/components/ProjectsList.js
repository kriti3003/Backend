import React from 'react';

const ProjectsList = ({ projects }) => {
  if (!projects || projects.length === 0) {
    return (
      <div className="projects-sidebar">
        <h3>Projects</h3>
        <p style={{ fontSize: '0.9rem', color: '#666' }}>No projects found for this skill</p>
      </div>
    );
  }

  return (
    <div className="projects-sidebar">
      <h3>Projects ({projects.length})</h3>
      <div className="projects-sidebar-list">
        {projects.map((project) => (
          <div key={project.id} className="project-sidebar-item">
            <h4>{project.title}</h4>
            {project.description && (
              <p>{project.description}</p>
            )}
            {project.profile_name && (
              <div style={{ 
                fontSize: '0.75rem', 
                color: '#007bff', 
                marginTop: '0.25rem',
                fontWeight: 'bold' 
              }}>
                by {project.profile_name}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProjectsList;