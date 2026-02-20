// Import necessary libraries and hooks
import React, { useState } from 'react'; // stdlib
import { useFormik } from 'formik'; // external-lib: formik
import * as Yup from 'yup'; // external-lib: yup

// Validation schema using Yup
const validationSchema = Yup.object({
  email: Yup.string() // validate email format
    .email('Invalid email address')
    .required('Email is required'),
  password: Yup.string() // validate password length
    .min(6, 'Password must be at least 6 characters')
    .required('Password is required'),
});

const Login = () => {
  const [errorMessage, setErrorMessage] = useState(''); // state to hold error messages

  // Formik form handling
  const formik = useFormik({
    initialValues: {
      email: '',
      password: '',
    },
    validationSchema,
    onSubmit: async (values) => {
      try {
        const response = await fetch('/api/login', { // API endpoint for login
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(values),
        });
        if (!response.ok) {
          throw new Error('Login failed');
        }
        const data = await response.json(); // handle successful login
        console.log('Login successful:', data);
        // Redirect or perform actions on successful login
      } catch (error) {
        setErrorMessage(error.message); // set error message on failure
      }
    },
  });

  return (
    <form onSubmit={formik.handleSubmit} className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <h2 className="text-xl mb-4">Login</h2>
      {errorMessage && <div className="text-red-500 mb-4">{errorMessage}</div>}
      <div className="mb-4">
        <label htmlFor="email" className="block text-gray-700 text-sm font-bold mb-2">Email</label>
        <input
          id="email"
          name="email"
          type="text"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          value={formik.values.email}
          className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ${formik.touched.email && formik.errors.email ? 'border-red-500' : ''}`}
        />
        {formik.touched.email && formik.errors.email ? (
          <div className="text-red-500 text-xs italic">{formik.errors.email}</div>
        ) : null}
      </div>
      <div className="mb-6">
        <label htmlFor="password" className="block text-gray-700 text-sm font-bold mb-2">Password</label>
        <input
          id="password"
          name="password"
          type="password"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          value={formik.values.password}
          className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ${formik.touched.password && formik.errors.password ? 'border-red-500' : ''}`}
        />
        {formik.touched.password && formik.errors.password ? (
          <div className="text-red-500 text-xs italic">{formik.errors.password}</div>
        ) : null}
      </div>
      <div className="flex items-center justify-between">
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Login
        </button>
      </div>
    </form>
  );
};

export default Login; // Exporting the Login component
