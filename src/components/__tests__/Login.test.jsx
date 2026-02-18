import React from 'react';  // external-lib: react
import { render, screen, fireEvent, waitFor } from '@testing-library/react';  // external-lib: @testing-library/react
import Login from '../Login';  // internal-file: Login
import '@testing-library/jest-dom/extend-expect';  // external-lib: @testing-library/jest-dom

// Mocking fetch for API calls
const mockFetch = jest.fn();
global.fetch = mockFetch;

describe('Login Component', () => {
  beforeEach(() => {
    // Clear mock calls before each test
    mockFetch.mockClear();
  });

  test('renders login form', () => {
    render(<Login />);
    expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /login/i })).toBeInTheDocument();
  });

  test('allows user to input email and password', () => {
    render(<Login />);
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'password123' } });

    expect(screen.getByLabelText(/email/i).value).toBe('test@example.com');
    expect(screen.getByLabelText(/password/i).value).toBe('password123');
  });

  test('calls API on login button click', async () => {
    mockFetch.mockResolvedValueOnce({ ok: true });  // Simulating successful API response
    render(<Login />);
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'password123' } });
    fireEvent.click(screen.getByRole('button', { name: /login/i }));

    await waitFor(() => {
      expect(mockFetch).toHaveBeenCalledWith('http://localhost:8000/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: 'test@example.com', password: 'password123' }),
      });
    });
  });

  test('displays error message on failed login', async () => {
    mockFetch.mockResolvedValueOnce({ ok: false, json: async () => ({ message: 'Invalid credentials' }) });
    render(<Login />);
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'password123' } });
    fireEvent.click(screen.getByRole('button', { name: /login/i }));

    await waitFor(() => {
      expect(screen.getByText(/invalid credentials/i)).toBeInTheDocument();
    });
  });
});
