function SearchBar({ city, setCity, onSearch, loading }) {
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      onSearch()
    }
  }

  return (
    <div className="flex flex-col sm:flex-row justify-center gap-3 max-w-lg mx-auto">
      <div className="relative flex-1">
        <input
          type="text"
          placeholder="Enter city name (e.g., London, New York)"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          onKeyPress={handleKeyPress}
          disabled={loading}
          className="w-full px-6 py-4 text-lg border-2 border-white/30 rounded-2xl bg-white/95 text-gray-800 outline-none focus:border-white focus:bg-white focus:ring-4 focus:ring-white/30 disabled:opacity-60 disabled:cursor-not-allowed transition-all duration-300 placeholder-gray-500 shadow-lg"
        />
        <div className="absolute right-4 top-1/2 transform -translate-y-1/2 text-gray-400">
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
      </div>
      <button
        onClick={onSearch}
        disabled={loading || !city.trim()}
        className="px-8 py-4 text-lg font-semibold rounded-2xl bg-gradient-to-r from-blue-600 to-blue-700 text-white shadow-lg hover:from-blue-700 hover:to-blue-800 hover:shadow-xl disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none transition-all duration-300 transform hover:scale-105 active:scale-95 min-w-[140px] border-2 border-white/20"
      >
        {loading ? (
          <div className="flex items-center justify-center gap-2">
            <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
            <span>Searching...</span>
          </div>
        ) : (
          <span>Search</span>
        )}
      </button>
    </div>
  )
}

export default SearchBar
