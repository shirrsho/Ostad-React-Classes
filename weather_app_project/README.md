# 🌤️ Weather App - React + Vite + Tailwind CSS

A complete weather application built with React, Vite, and Tailwind CSS, demonstrating modern React concepts, component architecture, and utility-first CSS.

## 🚀 Features

### Core Functionality
- **Real-time Weather Data**: Fetches live weather data using OpenWeatherMap API
- **City Search**: Search weather for any city worldwide
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

### Technical Features
- **React Hooks**: Uses `useState` for state management
- **API Integration**: Real API calls with proper error handling
- **Loading States**: Beautiful loading animations during data fetching
- **Error Handling**: User-friendly error messages for failed requests
- **Tailwind CSS**: Utility-first CSS framework for rapid styling

### UI/UX Features
- **Weather Icons**: Dynamic weather icons from OpenWeatherMap
- **Detailed Information**: Temperature, humidity, wind speed, pressure, visibility
- **Smooth Animations**: CSS transitions and keyframe animations
- **Glass Morphism**: Modern glass-like design with backdrop blur
- **Interactive Elements**: Hover effects and button animations

## 🛠️ Technologies Used

- **React 18** - Modern React with hooks
- **Vite** - Fast build tool and development server
- **Tailwind CSS** - Utility-first CSS framework
- **OpenWeatherMap API** - Weather data provider

## 📋 Prerequisites

- Node.js (v20.19+ or v22.12+ recommended)
- npm or yarn package manager
- Internet connection for API calls

## 🚀 Getting Started

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Start Development Server**
   ```bash
   npm run dev
   ```

3. **Open Browser**
   Navigate to `http://localhost:5173`

## 📖 Code Structure

```
src/
├── components/
│   ├── SearchBar.jsx              # Search input & button
│   ├── LoadingSpinner.jsx         # Loading state
│   ├── ErrorMessage.jsx           # Error display
│   ├── WeatherCard.jsx            # Weather information
│   └── index.js                   # Component exports
├── App.jsx                        # Main application component
├── App.css                        # Global styles & Tailwind imports
├── main.jsx                       # Application entry point
└── assets/                        # Static assets
```

## 🏗️ Component Architecture

### Component Responsibilities

#### **SearchBar Component**
- Handles city input and search functionality
- Manages Enter key press for search
- Displays loading state on search button

#### **LoadingSpinner Component**
- Shows loading animation during API calls
- Provides visual feedback for user actions

#### **ErrorMessage Component**
- Displays API errors and network issues
- Shows user-friendly error messages

#### **WeatherCard Component**
- Displays comprehensive weather information
- Shows weather icons, temperature, and details
- Responsive grid layout for weather details

## 🎯 Learning Objectives

This project demonstrates:

1. **Component Architecture**
   - Breaking down UI into reusable components
   - Props passing between components
   - Component composition

2. **State Management**
   - Lifting state up to parent components
   - Managing complex state with multiple hooks
   - State synchronization between components

3. **API Integration**
   - Making HTTP requests with fetch
   - Handling async/await operations
   - API key management

4. **Error Handling**
   - Try-catch blocks
   - User-friendly error messages
   - Loading states

5. **Modern CSS**
   - CSS Grid and Flexbox
   - CSS Animations and Transitions
   - Responsive design principles
   - Component-scoped styling

## 📝 Component Props Reference

### SearchBar
```javascript
<SearchBar
  city={string}           // Current city input value
  setCity={function}      // Function to update city value
  onSearch={function}     // Function to trigger search
  loading={boolean}       // Loading state
/>
```

### WeatherCard
```javascript
<WeatherCard
  weather={object}        // Weather data object from API
/>
```

### ErrorMessage
```javascript
<ErrorMessage
  message={string}        // Error message to display
/>
```

## 🔧 API Configuration

The app uses OpenWeatherMap's Current Weather Data API. **You need to get your own free API key** to use this app.

### **How to Get Your Free API Key:**

1. **Sign up** at [OpenWeatherMap](https://openweathermap.org/api)
2. **Verify your email** (required for API access)
3. **Go to your dashboard** and copy your API key
4. **Replace** `YOUR_API_KEY_HERE` in `src/App.jsx` with your actual key

### **API Key Setup:**
```javascript
const API_KEY = 'YOUR_API_KEY_HERE' // Replace with your actual API key
```

**Current API Configuration:**
- **Version**: OpenWeatherMap API v2.5
- **Endpoint**: `https://api.openweathermap.org/data/2.5/weather`
- **Units**: Metric (°C, m/s, hPa)
- **Free Tier**: 1,000 calls/day included

## 🧪 Testing Without API Key

If you want to test the app's UI without getting an API key, you can:

1. **Use Mock Data**: Temporarily replace the API call with mock weather data
2. **Test Error States**: The app has built-in error handling you can test
3. **Check Loading States**: The loading animations work without API calls

### **Quick Mock Data Setup:**
```javascript
// In App.jsx, temporarily replace fetchWeather function:
const fetchWeather = async (cityName) => {
  setLoading(true)
  setError('')
  // Simulate API delay
  setTimeout(() => {
    const mockData = {
      name: cityName,
      sys: { country: 'US' },
      weather: [{ description: 'clear sky', icon: '01d' }],
      main: { temp: 22, feels_like: 25, humidity: 60, pressure: 1013 },
      wind: { speed: 3.5 },
      visibility: 10000
    }
    setWeather(mockData)
    setLoading(false)
  }, 1000)
}
```

## 🎨 Tailwind CSS Features Used

### Utility Classes
- **Layout**: `flex`, `grid`, `container`, `mx-auto`
- **Spacing**: `p-8`, `m-4`, `gap-4`, `mb-6`
- **Colors**: `bg-blue-500`, `text-white`, `bg-white/10`
- **Typography**: `text-2xl`, `font-bold`, `text-center`
- **Effects**: `shadow-lg`, `backdrop-blur-md`, `opacity-80`

### Custom Utilities
- **Animations**: `animate-fade-in`, `animate-shake`, `animate-pulse`
- **Text Shadows**: `text-shadow-lg`, `text-shadow-2xl`
- **Responsive**: `md:grid-cols-2`, `lg:grid-cols-4`

## 🚀 Deployment

Build for production:
```bash
npm run build
```

Preview production build:
```bash
npm run preview
```

## 📝 Future Enhancements

- [ ] Add weather forecasts (5-day, hourly)
- [ ] Implement geolocation for current location weather
- [ ] Add favorite cities feature
- [ ] Include weather alerts and warnings
- [ ] Add dark/light theme toggle
- [ ] Implement unit conversion (°C/°F)
- [ ] Add weather maps integration

## 🤝 Contributing

This is an educational project. Feel free to:
- Add new features
- Improve the UI/UX
- Fix bugs
- Optimize performance

## 📄 License

This project is for educational purposes. OpenWeatherMap data is subject to their terms of service.

---

**Happy Coding! 🎉**
