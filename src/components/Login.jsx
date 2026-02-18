// Login.jsx
import React, { useState } from 'react'; // stdlib
import axios from 'axios'; // external-lib: axios

const Login = () => {
  const [email, setEmail] = useState(''); // State for email input
  const [password, setPassword] = useState(''); // State for password input
  const [loading, setLoading] = useState(false); // State for loading indicator
  const [error, setError] = useState(''); // State for error message

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent default form submission
    setLoading(true); // Set loading to true
    setError(''); // Clear previous error

    try {
      const response = await axios.post('/api/login', { email, password }); // API call for login
      // Handle successful login (e.g., redirect or store token)
      console.log('Login successful:', response.data);
    } catch (err) {
      // Handle error from API
      setError('Login failed. Please check your credentials.');
      console.error('Login error:', err);
    } finally {
      setLoading(false); // Reset loading indicator
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <form className="bg-white p-6 rounded shadow-md w-80" onSubmit={handleSubmit}>
        <h2 className="text-lg font-semibold mb-4">Login</h2>
        {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
        <div className="mb-4">
          <label className="block text-gray-700">Email:</label>
          <input
            type="email"
            className="mt-1 block w-full p-2 border border-gray-300 rounded"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Password:</label>
          <input
            type="password"
            className="mt-1 block w-full p-2 border border-gray-300 rounded"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
          disabled={loading} // Disable button during loading
        >
          {loading ? 'Logging in...' : 'Login'} // Show loading text if logging in
        </button>
        {loading && <div className="loader mt-4">Loading...</div>} // Loading indicator
      </form>
    </div>
  );
};

export default Login; // Export the Login component