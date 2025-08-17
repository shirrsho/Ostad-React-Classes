function CourseCard({ course, onEnroll, onToggleFavorite }) {
  return (
    <div className="course-card">
      <h3>{course.title}</h3>
      <p><strong>Instructor:</strong> {course.instructor}</p>
      <p><strong>Duration:</strong> {course.duration} hours</p>
      <p><strong>Price:</strong> ${course.price}</p>
      
      {/* Conditional Rendering - Ternary */}
      <p className={course.difficulty === 'Beginner' ? 'easy' : course.difficulty === 'Advanced' ? 'hard' : 'medium'}>
        Level: {course.difficulty}
      </p>
      
      {/* Conditional Rendering - Logical && */}
      {course.isPopular && <span className="popular-badge">Popular</span>}
      
      <div className="course-actions">
        <button onClick={() => onEnroll(course.title)}>
          Enroll Now
        </button>
        <button onClick={() => onToggleFavorite(course.title)}>
          Like
        </button>
      </div>
    </div>
  )
}

export default CourseCard