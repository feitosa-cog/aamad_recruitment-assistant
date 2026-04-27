'use client';

import { useState, FormEvent } from 'react';
import { ChatMessage, submitJobDescription, checkHealth } from '@/lib/api';
import MessageBubble from './MessageBubble';
import ResultsList from './ResultsList';
import LoadingIndicator from './LoadingIndicator';

export default function ChatInterface() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [backendConnected, setBackendConnected] = useState<boolean | null>(null);

  // Check backend health on mount
  useState(() => {
    checkHealth().then(setBackendConnected);
  });

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    
    if (!input.trim() || isLoading) return;

    const userMessage: ChatMessage = {
      id: Date.now().toString(),
      role: 'user',
      content: input.trim(),
    };

    const loadingMessage: ChatMessage = {
      id: (Date.now() + 1).toString(),
      role: 'assistant',
      content: 'Processing your request...',
      isLoading: true,
    };

    setMessages(prev => [...prev, userMessage, loadingMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await submitJobDescription(userMessage.content);
      
      const assistantMessage: ChatMessage = {
        id: loadingMessage.id,
        role: 'assistant',
        content: `Found ${response.candidates.length} candidates from ${response.total_searched} searched in ${response.processing_time_seconds.toFixed(1)}s`,
        candidates: response.candidates,
        isLoading: false,
      };

      setMessages(prev => [
        ...prev.slice(0, -1), // Remove loading message
        assistantMessage,
      ]);
    } catch (error) {
      const errorMessage: ChatMessage = {
        id: loadingMessage.id,
        role: 'assistant',
        content: error instanceof Error ? error.message : 'An error occurred while processing your request.',
        isLoading: false,
      };

      setMessages(prev => [
        ...prev.slice(0, -1),
        errorMessage,
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClear = () => {
    setMessages([]);
  };

  return (
    <div className="bg-white rounded-lg shadow-md">
      {/* Header */}
      <div className="border-b px-6 py-4">
        <div className="flex items-center justify-between">
          <h2 className="text-lg font-semibold text-gray-900">
            Candidate Search
          </h2>
          <div className="flex items-center gap-2">
            <span className={`w-2 h-2 rounded-full ${
              backendConnected === true ? 'bg-green-500' :
              backendConnected === false ? 'bg-red-500' :
              'bg-gray-300'
            }`} />
            <span className="text-sm text-gray-500">
              {backendConnected === true ? 'Backend Connected' :
               backendConnected === false ? 'Backend Disconnected' :
               'Checking...'}
            </span>
          </div>
        </div>
      </div>

      {/* Messages */}
      <div className="h-96 overflow-y-auto px-6 py-4 space-y-4">
        {messages.length === 0 ? (
          <div className="text-center text-gray-500 py-8">
            <p className="text-lg mb-2">Welcome to AI Recruitment Assistant</p>
            <p className="text-sm">
              Enter a job description to find and evaluate candidates
            </p>
          </div>
        ) : (
          messages.map(message => (
            <div key={message.id}>
              <MessageBubble message={message} />
              {message.candidates && message.candidates.length > 0 && (
                <ResultsList candidates={message.candidates} />
              )}
            </div>
          ))
        )}
        {isLoading && <LoadingIndicator />}
      </div>

      {/* Input Form */}
      <form onSubmit={handleSubmit} className="border-t px-6 py-4">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Enter job description (e.g., 'Looking for a Python developer with ML experience...')"
            className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent outline-none"
            disabled={isLoading}
          />
          <button
            type="submit"
            disabled={!input.trim() || isLoading}
            className="px-6 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isLoading ? 'Processing...' : 'Search'}
          </button>
        </div>
      </form>

      {/* Clear Button */}
      {messages.length > 0 && (
        <div className="border-t px-6 py-3">
          <button
            onClick={handleClear}
            className="text-sm text-gray-500 hover:text-gray-700"
          >
            Clear conversation
          </button>
        </div>
      )}
    </div>
  );
}