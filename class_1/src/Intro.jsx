function Intro({ information }){
    return(
        <div style={{fontSize: '1.5rem', padding:'6px', fontWeight: 'bold', marginBottom: '1rem', border:'2px solid yellow'}}>
            <h1>{information.name}</h1>
            <p>{information.institute}</p>
        </div>
    )
}

export default Intro