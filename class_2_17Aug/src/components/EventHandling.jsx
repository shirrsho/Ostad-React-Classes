function EventHandling() {
  const handleFormSubmit = (e) => {
    const formData = new FormData(e.target)
    const title = formData.get('title')
    const instructor = formData.get('instructor')
    
    alert(`New course added: ${title} by ${instructor}`)
    console.log(`Course: ${title}, Instructor: ${instructor}`)
  }

  const handleButtonClick = (buttonName) => {
    alert(`You clicked the ${buttonName} button!`)
    console.log(`Button clicked: ${buttonName}`)
  }

  return (
    <section>
      <h2>3. Event Handling</h2>
      
      {/* Click Events */}
      <div className="demo-buttons">
        <button onClick={() => handleButtonClick('Red')}>Red Button</button>
        <button onClick={() => handleButtonClick('Blue')}>Blue Button</button>
        <button onClick={() => handleButtonClick('Green')}>Green Button</button>
      </div>
      
      {/* Form Submission */}
      <h3>Add New Course Form:</h3>
      <form onSubmit={handleFormSubmit}>
        <input
          type="text"
          name="title"
          placeholder="Course Title"
          required
        />
        <input
          type="text"
          name="instructor"
          placeholder="Instructor Name"
          required
        />
        <button type="submit">Add Course</button>
      </form>
    </section>
  )
}

export default EventHandling