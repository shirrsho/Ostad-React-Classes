function WeatherCard({ weather }) {
  // Get weather icon URL
  const getWeatherIcon = (iconCode) => {
    return `https://openweathermap.org/img/wn/${iconCode}@4x.png`
  }

  // Format time
  const formatTime = (timestamp) => {
    return new Date(timestamp * 1000).toLocaleTimeString([], {
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  return (
    <div className="bg-white/15 backdrop-blur-xl border border-white/30 rounded-3xl p-8 md:p-10 shadow-2xl animate-fade-in">
      {/* Location and Main Weather */}
      <div className="text-center mb-8">
        <div className="flex items-center justify-center gap-4 mb-4 flex-wrap">
          <div className="text-2xl">
            📍
          </div>
          <h2 className="text-2xl md:text-3xl font-bold text-white text-shadow-lg">
            {weather.name}, {weather.sys.country}
          </h2>
        </div>

        <div className="flex items-center justify-center gap-6 mb-6">
          {weather.weather[0].icon && (
            <img
              src={getWeatherIcon(weather.weather[0].icon)}
              alt={weather.weather[0].description}
              className="w-24 h-24 md:w-28 md:h-28 drop-shadow-2xl animate-float"
            />
          )}
          <div className="text-left">
            <div className="text-6xl md:text-7xl font-bold text-white text-shadow-2xl mb-2">
              {Math.round(weather.main.temp)}°
            </div>
            <div className="text-blue-100 text-lg">
              Feels like {Math.round(weather.main.feels_like)}°C
            </div>
          </div>
        </div>

        <div className="text-xl md:text-2xl text-white font-medium capitalize mb-2">
          {weather.weather[0].description}
        </div>
        <div className="text-blue-100 text-sm">
          H: {Math.round(weather.main.temp_max)}° L: {Math.round(weather.main.temp_min)}°
        </div>
      </div>

      {/* Weather Details Grid */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
        <div className="bg-white/20 p-4 rounded-2xl text-center hover:bg-white/30 transition-all duration-300 hover:scale-105 shadow-lg">
          <div className="text-2xl mb-2">💧</div>
          <div className="text-xs text-blue-100 uppercase tracking-wide font-semibold mb-1">Humidity</div>
          <div className="text-xl font-bold text-white">{weather.main.humidity}%</div>
        </div>

        <div className="bg-white/20 p-4 rounded-2xl text-center hover:bg-white/30 transition-all duration-300 hover:scale-105 shadow-lg">
          <div className="text-2xl mb-2">💨</div>
          <div className="text-xs text-blue-100 uppercase tracking-wide font-semibold mb-1">Wind Speed</div>
          <div className="text-xl font-bold text-white">{weather.wind.speed} m/s</div>
        </div>

        <div className="bg-white/20 p-4 rounded-2xl text-center hover:bg-white/30 transition-all duration-300 hover:scale-105 shadow-lg">
          <div className="text-2xl mb-2">📊</div>
          <div className="text-xs text-blue-100 uppercase tracking-wide font-semibold mb-1">Pressure</div>
          <div className="text-xl font-bold text-white">{weather.main.pressure} hPa</div>
        </div>

        <div className="bg-white/20 p-4 rounded-2xl text-center hover:bg-white/30 transition-all duration-300 hover:scale-105 shadow-lg">
          <div className="text-2xl mb-2">👁️</div>
          <div className="text-xs text-blue-100 uppercase tracking-wide font-semibold mb-1">Visibility</div>
          <div className="text-xl font-bold text-white">{(weather.visibility / 1000).toFixed(1)} km</div>
        </div>
      </div>

      {/* Additional Info */}
      <div className="border-t border-white/30 pt-6">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-center">
          <div className="text-blue-100">
            <div className="text-sm font-medium">Sunrise</div>
            <div className="text-lg font-semibold text-white">{formatTime(weather.sys.sunrise)}</div>
          </div>
          <div className="text-blue-100">
            <div className="text-sm font-medium">Sunset</div>
            <div className="text-lg font-semibold text-white">{formatTime(weather.sys.sunset)}</div>
          </div>
          <div className="text-blue-100">
            <div className="text-sm font-medium">Last Updated</div>
            <div className="text-lg font-semibold text-white">{new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default WeatherCard
