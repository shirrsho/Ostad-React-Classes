function LoadingSpinner() {
  return (
    <div className="flex flex-col items-center justify-center py-12">
      <div className="relative">
        {/* Outer ring */}
        <div className="w-16 h-16 border-4 border-white/20 rounded-full animate-spin">
        </div>
        {/* Inner ring */}
        <div className="absolute top-0 left-0 w-16 h-16 border-4 border-transparent border-t-white rounded-full animate-spin"
             style={{ animationDuration: '0.8s' }}>
        </div>
        {/* Center dot */}
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-3 h-3 bg-white rounded-full animate-pulse">
        </div>
      </div>

      <div className="mt-6 text-center">
        <div className="text-xl font-semibold text-white mb-2">Fetching Weather Data</div>
        <div className="text-blue-100 text-sm">Please wait while we get the latest information...</div>
      </div>

      {/* Animated dots */}
      <div className="flex gap-1 mt-4">
        <div className="w-2 h-2 bg-white rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
        <div className="w-2 h-2 bg-white rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
        <div className="w-2 h-2 bg-white rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
      </div>
    </div>
  )
}

export default LoadingSpinner
