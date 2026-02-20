// authService.js

import fetch from 'node-fetch'; // Import fetch for making API requests

/**
 * AuthService is responsible for handling user authentication requests.
 * It communicates with the backend FastAPI service to log in users.
 */

const API_URL = 'http://localhost:8000/api/auth/login'; // Update with your API URL

/**
 * Login function to authenticate user credentials.
 *
 * @param {string} username - The username of the user.
 * @param {string} password - The password of the user.
 * @returns {Promise<object>} - Returns the response data from the API.
 * @throws {Error} - Throws an error if the request fails.
 */
export const login = async (username, password) => {
  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    // Check if the response is not OK
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Login failed');
    }

    // Parse and return response data
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Authentication error:', error);
    throw error; // Re-throw the error for further handling
  }
};
