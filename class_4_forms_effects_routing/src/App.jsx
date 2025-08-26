import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import FormDemo from './components/FormDemo'
import EffectsDemo from './components/EffectsDemo'
import ApiDemo from './components/ApiDemo'
import UserProfile from './components/UserProfile'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <div>
        <nav>
          <h1>React Basics</h1>
          <Link to="/">Forms</Link>
          <Link to="/effects">Effects</Link>
          <Link to="/api">API</Link>
          <Link to="/user/1">User</Link>
        </nav>

        <Routes>
          <Route path="/" element={<FormDemo />} />
          <Route path="/effects" element={<EffectsDemo />} />
          <Route path="/api" element={<ApiDemo />} />
          <Route path="/user/:id" element={<UserProfile />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App