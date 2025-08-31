import React, { useState, useCallback, useEffect } from 'react';

const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState('');

  // Debounce search to avoid too many API calls
  const debounceSearch = useCallback(() => {
    const timeoutId = setTimeout(() => {
      onSearch(query);
    }, 300);

    return () => clearTimeout(timeoutId);
  }, [query, onSearch]);

  useEffect(() => {
    const cleanup = debounceSearch();
    return cleanup;
  }, [debounceSearch]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(query);
  };

  const handleClear = () => {
    setQuery('');
    onSearch('');
  };

  return (
    <div className="search-bar">
      <form onSubmit={handleSubmit}>
        <div style={{ position: 'relative' }}>
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search profiles by name, skills, or description..."
          />
          {query && (
            <button
              type="button"
              onClick={handleClear}
              style={{
                position: 'absolute',
                right: '8px',
                top: '50%',
                transform: 'translateY(-50%)',
                background: 'none',
                border: 'none',
                cursor: 'pointer',
                fontSize: '18px',
                color: '#666',
              }}
            >
              ×
            </button>
          )}
        </div>
      </form>
    </div>
  );
};

export default SearchBar;