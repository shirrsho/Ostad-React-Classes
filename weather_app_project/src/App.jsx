import { useState } from 'react'
import './App.css'
import SearchBar from './components/SearchBar'
import LoadingSpinner from './components/LoadingSpinner'
import ErrorMessage from './components/ErrorMessage'
import WeatherCard from './components/WeatherCard'

function App() {
  const [city, setCity] = useState('')
  const [weather, setWeather] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  // OpenWeatherMap API key (free tier) - In production, use environment variables
  const API_KEY = '575530f8485c621232285553dc6d72e0'
  const API_URL = 'https://api.openweathermap.org/data/2.5/weather'

  // Fetch weather data from API
  const fetchWeather = async (cityName) => {
    setLoading(true)
    setError('')
    try {
      const response = await fetch(`${API_URL}?q=${cityName}&appid=${API_KEY}&units=metric`)
      if (!response.ok) {
        throw new Error('City not found')
      }
      const data = await response.json()
      setWeather(data)
    } catch (err) {
      setError(err.message)
      setWeather(null)
    } finally {
      setLoading(false)
    }
  }

  const handleSearch = () => {
    if (city.trim()) {
      fetchWeather(city.trim())
    }
  }

  return (
    <div className="min-w-screen min-h-screen bg-gradient-to-br from-blue-400 via-blue-500 to-blue-600">
      <div className="container mx-auto px-4 py-8">
        {/* Header Section */}
        <header className="text-center mb-12">
          <div className="inline-flex items-center justify-center w-20 h-20 bg-white/20 backdrop-blur-sm rounded-full mb-6 shadow-lg">
            <span className="text-4xl">🌤️</span>
          </div>
          <h1 className="text-5xl md:text-6xl font-bold text-white mb-4 drop-shadow-lg">
            Weather App
          </h1>
          <p className="text-blue-100 text-lg md:text-xl max-w-2xl mx-auto leading-relaxed">
            Get real-time weather information for any city around the world
          </p>
        </header>

        {/* Main Content */}
        <main className="max-w-4xl mx-auto">
          <div className="bg-white/10 backdrop-blur-lg rounded-3xl p-8 md:p-12 shadow-2xl border border-white/20">
            <SearchBar
              city={city}
              setCity={setCity}
              onSearch={handleSearch}
              loading={loading}
            />

            <div className="mt-8">
              {error && <ErrorMessage message={error} />}
              {loading && <LoadingSpinner />}
              {weather && !loading && <WeatherCard weather={weather} />}
            </div>
          </div>
        </main>

        {/* Footer */}
        <footer className="text-center mt-12 text-blue-100/70 text-sm">
          <p>Powered by OpenWeatherMap API • Built with React & Tailwind CSS</p>
        </footer>
      </div>
    </div>
  )
}

export default App
