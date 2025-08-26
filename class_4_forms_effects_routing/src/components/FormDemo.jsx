import { useState } from 'react'

function FormDemo() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [submitted, setSubmitted] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault()
    setSubmitted(true)
  }

  if (submitted) {
    return (
      <div className="container">
        <h2>Form Submitted!</h2>
        <p>Name: {name}</p>
        <p>Email: {email}</p>
        <button className="btn" onClick={() => setSubmitted(false)}>
          Go Back
        </button>
      </div>
    )
  }

  return (
    <div className="container">
      <h2>Simple Form</h2>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>

        <button type="submit" className="btn">
          Submit
        </button>
      </form>
    </div>
  )
}

export default FormDemo