function DemoHook() {
    let value = 0;

    function addOne() {
      value = value + 1;
      console.log(value);
    }

  return (
    <div>
      <h2>Demo Hook Component</h2>
      <p>Value: {value}</p>
      <button onClick={addOne}>Add One</button>
    </div>
  )
}

export default DemoHook;