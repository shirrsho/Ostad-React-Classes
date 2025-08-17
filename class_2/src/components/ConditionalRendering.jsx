import React from 'react'

function ConditionalRendering() {
  const isLoggedIn = false
  const userName = "Alice"
  const currentTime = new Date().getHours()
  const courses = [
    { id: 1, title: 'React Basics' },
    { id: 2, title: 'JavaScript' },
    { id: 3, title: 'CSS' },
    { id: 4, title: 'Node.js' }
  ]

  // If/Else function
  const renderWelcomeMessage = () => {
    if (isLoggedIn) {
      return <p>Welcome back, {userName}!</p>
    } else {
      return <p>Please log in to continue</p>
    }
  }

  // Switch statement function
  const renderTimeGreeting = () => {
    switch (true) {
      case (currentTime < 12):
        return <p>🌅 Good Morning!</p>
      case (currentTime < 18):
        return <p>☀️ Good Afternoon!</p>
      default:
        return <p>🌙 Good Evening!</p>
    }
  }

  return (
    <section>
      <h2>1. Conditional Rendering</h2>
      
      {/* Ternary Operator */}
      <p className={`${isLoggedIn ? 'greenlogin' : 'redlogin'}`}>Status: {isLoggedIn ? 'Online' : 'Offline'}</p>

      {/* Logical && */}
      {isLoggedIn && <p>You have 3 new messages</p>}
      
      {/* If/Else using function */}
      {renderWelcomeMessage()}
      
      {/* Switch Statement */}
      {renderTimeGreeting()}
      
      {/* IIFE (Immediately Invoked Function) */}
      {(() => {
        const courseCount = courses.length
        if (courseCount > 3) return <p>We have many courses available!</p>
        return <p>Limited courses available</p>
      })()}
    </section>
  )
}

export default ConditionalRendering