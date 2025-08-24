import { useRef } from 'react'

function UseRefDemo() {
  const textRef = useRef(null)
  const inputRef = useRef(null)

  // DOM Manipulation Examples
  const changeInnerText = () => {
    textRef.current.innerText = 'Text changed with innerText!'
  }

  const changeInnerHTML = () => {
    textRef.current.innerHTML = '<strong>HTML changed with innerHTML!</strong>'
  }

  const changeAttribute = () => {
    textRef.current.setAttribute('data-custom', 'Custom attribute added!')
    textRef.current.style.color = 'red'
  }

  const focusInput = () => {
    inputRef.current.focus()
  }

  const getInputValue = () => {
    alert(`Input value: ${inputRef.current.value}`)
  }

  const addCSSClass = () => {
    textRef.current.classList.add('highlight')
  }

  const removeCSSClass = () => {
    textRef.current.classList.remove('highlight')
  }

  return (
    <section>
      <h2>2. useRef Hook Demonstrations</h2>
      
      <div className="demo-box">
        <h3>DOM Manipulation</h3>
        <p ref={textRef}>Original text content</p>
        
        <button onClick={changeInnerText}>Change innerText</button>
        <button onClick={changeInnerHTML}>Change innerHTML</button>
        <button onClick={changeAttribute}>Change Attribute</button>
        <button onClick={addCSSClass}>Add CSS Class</button>
        <button onClick={removeCSSClass}>Remove CSS Class</button>
      </div>

      <div className="demo-box">
        <h3>Input Element Control</h3>
        <input ref={inputRef} type="text" placeholder="Type something..." />
        <button onClick={focusInput}>Focus Input</button>
        <button onClick={getInputValue}>Get Value</button>
      </div>
    </section>
  )
}

export default UseRefDemo