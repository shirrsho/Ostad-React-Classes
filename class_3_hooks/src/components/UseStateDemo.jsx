import { useState } from 'react'

function UseStateDemo() {
  const [count, setCount] = useState(0)
  const [name, setName] = useState('')
  const [isVisible, setIsVisible] = useState(true)

  const incrementCount = () => {
    setCount(count + 1)
  }

  const decrementCount = () => {
    setCount(count - 1)
  }

  const resetCount = () => {
    setCount(0)
  }

  const handleNameChange = (e) => {
    const newName = e.target.value
    setName(newName)
  }

  const toggleVisibility = () => {
    setIsVisible(!isVisible)
  }

  return (
    <section>
      <h2>1. useState Understanding Inside</h2>
      
      <div className="demo-box">
        <h3>Basic State Management</h3>
        <p>Count: {count}</p>
        <button onClick={incrementCount}>Increment</button>
        <button onClick={decrementCount}>Decrement</button>
        <button onClick={resetCount}>Reset</button>
      </div>

      <div className="demo-box">
        <h3>Input State</h3>
        <input 
          type="text" 
          value={name}
          onChange={handleNameChange}
          placeholder="Enter your name"
        />
        <p>Hello, {name || 'Guest'}!</p>
      </div>

      <div className="demo-box">
        <h3>Boolean State</h3>
        <button onClick={toggleVisibility}>
          {isVisible ? 'Hide' : 'Show'} Content
        </button>
        {isVisible && (
          <div className="success">
            <p>This content is conditionally rendered!</p>
          </div>
        )}
      </div>
    </section>
  )
}

export default UseStateDemo