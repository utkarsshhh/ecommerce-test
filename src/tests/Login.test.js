import React from 'react'; // stdlib
import { render, screen, fireEvent } from '@testing-library/react'; // external-lib: @testing-library/react
import Login from '../components/Login'; // internal-file: components/Login

describe('Login Component', () => {
  test('renders login form', () => {
    render(<Login />);
    expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
  });

  test('displays error message for invalid login', async () => {
    global.fetch = jest.fn(() => Promise.resolve({ ok: false })); // Mocking fetch
    render(<Login />);
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'wrongpassword' } });
    fireEvent.click(screen.getByText(/login/i));
    expect(await screen.findByText(/login failed/i)).toBeInTheDocument();
  });

  test('successful login', async () => {
    global.fetch = jest.fn(() => Promise.resolve({ ok: true, json: () => Promise.resolve({ access_token: 'token' }) })); // Mocking fetch
    render(<Login />);
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'correctpassword' } });
    fireEvent.click(screen.getByText(/login/i));
    expect(await screen.findByText(/login successful/i)).toBeInTheDocument();
  });
});
