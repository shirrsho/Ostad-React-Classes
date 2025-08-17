import React from 'react'
import ConditionalRendering from './components/ConditionalRendering'
import PropsDemo from './components/PropsDemo'
import EventHandling from './components/EventHandling'
import './App.css'

function App() {
  return (
    <div>
      <h1>React Class 2 Demo</h1>
      
      <ConditionalRendering />
      <PropsDemo />
      <EventHandling />
    </div>
  )
}

export default App