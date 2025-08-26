import { use, useState } from 'react'

function ApiDemo() {
  const [users, setUsers] = useState([])
  const [loading, setLoading] = useState(false)
const [errorMessage, setErrorMessage] = useState('')
  // Using Async/Await
  const fetchWithAsync = async () => {
    try{
      setLoading(true)
      const response = await fetch('https://jsonplaceholder.typicode.com/users')
      const data = await response.json()
      setUsers(data.slice(0, 5)) // Only show 5 users
    } catch (error) {
      setErrorMessage('Failed to fetch users')
    } finally {
      setLoading(false)
    }
  }

  // Using Promises
  const fetchWithPromise = () => {
    setLoading(true)
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => response.json())
      .then(data => {
        setUsers(data.slice(0, 3)) // Only show 3 users
        setLoading(false)
      })
  }

  return (
    <div className="container">
      <h2>API Calls</h2>
      
      <div className="controls">
        <button className="btn" onClick={fetchWithAsync}>
          Get Users
        </button>
        <button className="btn btn-secondary" onClick={() => setUsers([])}>
          Clear
        </button>
      </div>

      {loading && <div className="loading">Loading...</div>}
      {errorMessage && <div className="error">{errorMessage}</div>}
      <div className="user-list">
        {users.map(user => (
          <div key={user.id} className="user-card">
            <h4>{user.name}</h4>
            <p>{user.email}</p>
            <p>{user.address.city}</p>
            <p>{user.company.name}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default ApiDemo