import { useState, useEffect } from 'react'

function EffectsDemo() {
  const [count, setCount] = useState(0)
  const [message, setMessage] = useState('Hello!')

  // Runs every time
  useEffect(() => {
    document.title = `Count: ${count}`
  })

  // Runs once
  useEffect(() => {
    setMessage('Component loaded!')
  }, [])

  // Runs when count changes
  useEffect(() => {
    if (count > 5) {
      setMessage('Count is high!')
    } else if (count > 10) {
      setMessage('Count is very high!')
    } else if(count>0) {
      setMessage('Count is low')
    }
  }, [count])

  return (
    <div className="container">
      <h2>useEffect Examples</h2>
      
      <div className="card">
        <h3>Message: {message}</h3>
      </div>

      <div className="counter">{count}</div>
      
      <div className="controls">
        <button className="btn" onClick={() => setCount(count + 1)}>
          Add 1
        </button>
        <button className="btn btn-secondary" onClick={() => setCount(0)}>
          Reset
        </button>
      </div>

      <div className="card">
        <p>Check your browser tab title!</p>
      </div>
    </div>
  )
}

export default EffectsDemo