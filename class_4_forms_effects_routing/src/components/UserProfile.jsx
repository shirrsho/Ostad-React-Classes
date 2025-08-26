import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'

function UserProfile() {
  const { id } = useParams()
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
      .then(response => response.json())
      .then(data => {
        setUser(data)
        setLoading(false)
      })
  }, [id])

  if (loading) return <div className="loading">Loading...</div>

  return (
    <div className="container">
      <h2>User Profile</h2>
      
      <Link to="/api" className="btn">Back to Users</Link>

      {user && (
        <div className="card">
          <h3>{user.name}</h3>
          <p>Email: {user.email}</p>
          <p>Phone: {user.phone}</p>
          <p>City: {user.address.city}</p>
          <p>Company: {user.company.name}</p>
        </div>
      )}

      <div className="controls">
        <Link to="/user/1" className="btn">User 1</Link>
        <Link to="/user/2" className="btn">User 2</Link>
        <Link to="/user/3" className="btn">User 3</Link>
      </div>
    </div>
  )
}

export default UserProfile