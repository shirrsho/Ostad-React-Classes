import './App.css'
import Intro from './Intro'

function App() {

  const students = [
    {
      name:"Rahim",
      institute:"Daffodil International University",
    },
    {
      name:"Karim",
      institute:"Dhaka University",
    },
    {
      name:"Jamal",
      institute:"BUET",
    },
  ];

  return (
    <div className='ml-12' style={{display:'flex', gap:'12px'}}>
      {
        students.map((s) => <Intro information={s} /> )
      }
    </div>
  )
}

export default App
