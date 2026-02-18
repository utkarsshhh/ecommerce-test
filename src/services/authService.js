// authService.js

import axios from 'axios';  // external-lib: axios

/**
 * AuthService handles authentication API calls.
 */
const AuthService = {
  /**
   * User login using the provided credentials.
   * @param {Object} credentials - User credentials { username, password }
   * @returns {Promise<Object>} - Response data from the API
   * @throws {Error} - Throws error if the login fails
   */
  login: async (credentials) => {
    try {
      const response = await axios.post('/api/login', credentials);
      return response.data;
    } catch (error) {
      // Handle error response
      if (error.response) {
        throw new Error(error.response.data.message || 'Login failed');
      } else {
        throw new Error('Network error');
      }
    }
  },
};

export default AuthService;
