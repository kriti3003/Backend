import React from 'react';

const SkillsFilter = ({ skills, selectedSkill, onSkillSelect }) => {
  if (!skills || skills.length === 0) {
    return (
      <div className="skills-filter">
        <h3>Top Skills</h3>
        <p style={{ fontSize: '0.9rem', color: '#666' }}>No skills available</p>
      </div>
    );
  }

  return (
    <div className="skills-filter">
      <h3>Filter Projects by Skill</h3>
      
      {selectedSkill && (
        <button 
          onClick={() => onSkillSelect('')}
          className="clear-filter"
        >
          Clear Filter
        </button>
      )}
      
      <div className="skills-list">
        {skills.map((skill) => (
          <button
            key={skill.id || skill.name}
            onClick={() => onSkillSelect(skill.name)}
            className={`skill-button ${selectedSkill === skill.name ? 'active' : ''}`}
          >
            {skill.name}
            {skill.count && (
              <span style={{ marginLeft: '0.5rem', color: '#666', fontSize: '0.8rem' }}>
                ({skill.count})
              </span>
            )}
          </button>
        ))}
      </div>
    </div>
  );
};

export default SkillsFilter;