// App.jsx
// Main application file that includes the LoginForm component

import React from 'react'; // stdlib
import LoginForm from './components/LoginForm'; // internal-file: components/LoginForm
import './index.css'; // internal-file: index.css

const App = () => {
  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <LoginForm />
    </div>
  );
};

export default App;
