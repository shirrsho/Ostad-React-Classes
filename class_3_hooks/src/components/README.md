# Immutability in React

## What is Immutability?

Immutability means that once data is created, it cannot be changed. Instead of modifying existing data, you create new data with the desired changes.

## Why Immutability Matters in React

- **State Updates**: React detects state changes by comparing object references
- **Performance**: Enables efficient re-rendering optimizations
- **Predictability**: Prevents unexpected side effects from data mutations

## ImmutabilityDemo Examples

### Object Updates
```jsx
// ❌ Wrong - Direct mutation
user.name = 'Jane Smith'
setUser(user)

// ✅ Correct - Create new object
setUser(prev => ({ ...prev, name: 'Jane Smith' }))
```

### Nested Object Updates
```jsx
// ✅ Spread both levels
setUser(prev => ({
  ...prev,
  address: { ...prev.address, city: 'Los Angeles' }
}))
```

### Array Operations
```jsx
// ✅ Add item
setItems(prev => [...prev, newItem])

// ✅ Remove item
setItems(prev => prev.filter((_, i) => i !== index))

// ✅ Update item
setItems(prev => prev.map((item, i) => i === index ? newValue : item))
```

## Key Principles

1. **Never mutate state directly**
2. **Use spread operator (...) for copying**
3. **Create new objects/arrays for updates**
4. **Use immutable array methods (map, filter, slice)**