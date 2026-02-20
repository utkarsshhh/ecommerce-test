import React from 'react'; // stdlib
import Login from './components/Login'; // internal-file: components/Login

const App = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <Login />
    </div>
  );
};

export default App; // Exporting the main App component
