import ChatInterface from '@/components/ChatInterface'

export default function Home() {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
      {/* Main Chat Area */}
      <div className="lg:col-span-2">
        <ChatInterface />
      </div>
      
      {/* Sidebar - Placeholder for future features */}
      <div className="lg:col-span-1">
        <div className="bg-white rounded-lg shadow-md p-4 mb-4">
          <h2 className="text-lg font-semibold text-gray-900 mb-3">
            Quick Stats
          </h2>
          <div className="space-y-2 text-sm text-gray-600">
            <div className="flex justify-between">
              <span>Total Searches</span>
              <span className="font-medium">-</span>
            </div>
            <div className="flex justify-between">
              <span>Candidates Found</span>
              <span className="font-medium">-</span>
            </div>
            <div className="flex justify-between">
              <span>Avg. Match Score</span>
              <span className="font-medium">-</span>
            </div>
          </div>
        </div>
        
        {/* Placeholder for Dashboard */}
        <div className="bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-semibold text-gray-900 mb-3">
            Dashboard
          </h2>
          <p className="text-sm text-gray-500 mb-4">
            Analytics and reporting coming soon.
          </p>
          <div className="h-32 bg-gray-100 rounded-lg flex items-center justify-center">
            <span className="text-gray-400 text-sm">Placeholder</span>
          </div>
        </div>
        
        {/* Placeholder for Settings */}
        <div className="bg-white rounded-lg shadow-md p-4 mt-4">
          <h2 className="text-lg font-semibold text-gray-900 mb-3">
            Settings
          </h2>
          <p className="text-sm text-gray-500">
            API configuration coming soon.
          </p>
        </div>
      </div>
    </div>
  )
}