import { useState } from 'react'

function ImmutabilityDemo() {
  const [user, setUser] = useState({
    name: 'John Doe',
    age: 25,
    address: { city: 'New York', country: 'USA' }
  })

  const [items, setItems] = useState(['Apple', 'Banana', 'Orange'])
  const [newItem, setNewItem] = useState('')

  // Immutable Object Updates
  const updateName = () => {
    setUser(prev => ({ ...prev, name: 'Jane Smith' }))
  }

  const incrementAge = () => {
    setUser(prev => ({ ...prev, age: prev.age + 1 }))
  }

  const updateCity = () => {
    setUser(prev => ({
      ...prev,
      address: { ...prev.address, city: 'Los Angeles' }
    }))
  }

  // Immutable Array Updates
  const addItem = () => {
    if (newItem.trim()) {
      setItems(prev => [...prev, newItem])
      setNewItem('')
    }
  }

  const removeItem = (index) => {
    setItems(prev => prev.filter((_, i) => i !== index))
  }

  const updateItem = (index, newValue) => {
    setItems(prev => prev.map((item, i) => i === index ? newValue : item))
  }

  return (
    <section>
      <h2>3. Immutability & Spread Operator</h2>
      
      <div className="demo-box">
        <h3>Immutable Object Updates</h3>
        <div className="highlight">
          <p>Name: {user.name}</p>
          <p>Age: {user.age}</p>
          <p>City: {user.address.city}</p>
        </div>
        <button onClick={updateName}>Update Name</button>
        <button onClick={incrementAge}>Increment Age</button>
        <button onClick={updateCity}>Update City</button>
      </div>

      <div className="demo-box">
        <h3>Immutable Array Operations</h3>
        <input
          value={newItem}
          onChange={(e) => setNewItem(e.target.value)}
          placeholder="Add new item"
        />
        <button onClick={addItem}>Add Item</button>
        
        <ul className="item-list">
          {items.map((item, index) => (
            <li key={index}>
              <span>{item}</span>
              <div>
                <button onClick={() => updateItem(index, prompt('New value:', item))}>
                  Edit
                </button>
                <button onClick={() => removeItem(index)}>Remove</button>
              </div>
            </li>
          ))}
        </ul>
      </div>

      <div className="demo-box">
        <h3>Spread Operator Principles</h3>
        <div className="success">
          <p>✅ Objects: spread operator with property override</p>
          <p>✅ Nested: spread both outer and inner objects</p>
          <p>✅ Arrays: spread existing array with new items</p>
          <p>❌ Never mutate state directly</p>
        </div>
      </div>
    </section>
  )
}

export default ImmutabilityDemo