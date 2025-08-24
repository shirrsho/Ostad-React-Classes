import UseRefDemo from './components/UseRefDemo'
import UseStateDemo from './components/UseStateDemo'
import ImmutabilityDemo from './components/ImmutabilityDemo'
import './App.css'
import DemoHook from './components/DemoHook'

function App() {

  return (
    <div>
      <h1>React Hooks & State Management</h1>
      {/* <DemoHook/> */}
      <UseStateDemo />
      <UseRefDemo />
      <ImmutabilityDemo />
    </div>
  )
}

export default App