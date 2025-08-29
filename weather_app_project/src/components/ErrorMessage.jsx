function ErrorMessage({ message }) {
  return (
    <div className="bg-gradient-to-r from-red-500/90 to-red-600/90 backdrop-blur-sm border border-red-400/50 text-white px-6 py-4 rounded-2xl mb-6 shadow-lg animate-fade-in">
      <div className="flex items-center gap-3">
        <div className="flex-shrink-0">
          <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
          </svg>
        </div>
        <div className="flex-1">
          <div className="font-semibold text-lg mb-1">Oops! Something went wrong</div>
          <div className="text-red-100">{message}</div>
        </div>
      </div>
    </div>
  )
}

export default ErrorMessage
