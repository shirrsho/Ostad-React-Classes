import CourseCard from "./CourseCard"
function PropsDemo() {
  const courses = [
    { id: 1, title: 'React Basics', instructor: 'John Doe', duration: 20, price: 99, difficulty: 'Beginner', isPopular: true },
    { id: 2, title: 'Advanced JavaScript', instructor: 'Jane Smith', duration: 35, price: 149, difficulty: 'Advanced', isPopular: false },
    { id: 3, title: 'CSS Flexbox', instructor: 'Mike Johnson', duration: 15, price: 79, difficulty: 'Intermediate', isPopular: true },
    { id: 4, title: 'Node.js Backend', instructor: 'Sarah Wilson', duration: 40, price: 199, difficulty: 'Advanced', isPopular: false }
  ]

  const handleEnroll = (courseTitle) => {
    alert(`You clicked Enroll for: ${courseTitle}`)
    console.log(`Enrolled in: ${courseTitle}`)
  }

  const handleToggleFavorite = (courseTitle) => {
    alert(`You liked: ${courseTitle}`)
    console.log(`Added to favorites: ${courseTitle}`)
  }

  return (
    <section>
      <h2>2. Props Demo - Course Cards</h2>
      <p>Passing data from parent to child components:</p>
      <div className="courses-grid">
        {courses.map(course => (
          <CourseCard
            // key={course.id}
            course={course}
            onEnroll={handleEnroll}
            onToggleFavorite={handleToggleFavorite}
          />
        ))}
      </div>
    </section>
  )
}

export default PropsDemo