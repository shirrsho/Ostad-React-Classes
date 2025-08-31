import { useState } from 'react'
import './App.css'
import AddTask from './components/AddTask'
import TaskList from './components/TaskList'

function App() {
  const [tasks, setTasks] = useState([])
  const [filter, setFilter] = useState('all')

  const addTask = (text) => {
    const newTask = {
      id: Date.now(),
      text,
      completed: false,
    }
    setTasks([...tasks, newTask])
  }

  const toggleTask = (id) => {
    setTasks(tasks.map(task =>
      task.id === id ? { ...task, completed: !task.completed } : task
    ))
  }

  const deleteTask = (id) => {
    setTasks(tasks.filter(task => task.id !== id))
  }

  const updateTask = (id, newText) => {
    setTasks(tasks.map(task =>
      task.id === id ? { ...task, text: newText } : task
    ))
  }

  const filteredTasks = tasks.filter(task => {
    if (filter === 'completed') return task.completed
    if (filter === 'incomplete') return !task.completed
    return true
  })

  return (
    <div className="min-w-screen min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-800">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <header className="text-center mb-12">
          <div className="inline-flex items-center justify-center w-20 h-20 bg-white/20 backdrop-blur-sm rounded-full mb-6 shadow-lg">
            <span className="text-4xl">✅</span>
          </div>
          <h1 className="text-5xl md:text-6xl font-bold text-white mb-4 drop-shadow-lg">
            Task Manager
          </h1>
          <p className="text-slate-300 text-lg md:text-xl max-w-2xl mx-auto leading-relaxed">
            Organize your tasks and boost your productivity
          </p>
        </header>

        {/* Main Content */}
        <main className="max-w-2xl mx-auto">
          <div className="bg-white/10 backdrop-blur-lg rounded-3xl p-8 md:p-12 shadow-2xl border border-white/20">
            <AddTask onAddTask={addTask} />

            {/* Filter Buttons */}
            <div className="flex gap-2 mb-6">
              <button
                onClick={() => setFilter('all')}
                className={`px-4 py-2 rounded-lg transition-colors ${
                  filter === 'all'
                    ? 'bg-indigo-600 text-white'
                    : 'bg-white/20 text-white hover:bg-white/30'
                }`}
              >
                All ({tasks.length})
              </button>
              <button
                onClick={() => setFilter('incomplete')}
                className={`px-4 py-2 rounded-lg transition-colors ${
                  filter === 'incomplete'
                    ? 'bg-indigo-600 text-white'
                    : 'bg-white/20 text-white hover:bg-white/30'
                }`}
              >
                Pending ({tasks.filter(t => !t.completed).length})
              </button>
              <button
                onClick={() => setFilter('completed')}
                className={`px-4 py-2 rounded-lg transition-colors ${
                  filter === 'completed'
                    ? 'bg-indigo-600 text-white'
                    : 'bg-white/20 text-white hover:bg-white/30'
                }`}
              >
                Completed ({tasks.filter(t => t.completed).length})
              </button>
            </div>
            <TaskList
              tasks={filteredTasks}
              onToggle={toggleTask}
              onDelete={deleteTask}
              onUpdate={updateTask}
            />
          </div>
        </main>

        {/* Footer */}
        <footer className="text-center mt-12 text-slate-400/70 text-sm">
          <p>Built with React & Tailwind CSS</p>
        </footer>
      </div>
    </div>
  )
}

export default App
