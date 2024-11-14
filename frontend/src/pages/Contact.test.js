// src/pages/Contact.test.js
import React from 'react';
import { render, screen, fireEvent, act } from '@testing-library/react';
import Contact from './Contact';
import '@testing-library/jest-dom';

test('renders Contact form and handles submission', async () => {
    render(<Contact />);

    await act(async () => {
        fireEvent.change(screen.getByPlaceholderText(/Your Name/i), { target: { value: 'Test User' } });
        fireEvent.change(screen.getByPlaceholderText(/Your Email/i), { target: { value: 'test@example.com' } });
        fireEvent.change(screen.getByPlaceholderText(/Your Message/i), { target: { value: 'Hello, this is a test message.' } });
    });

    // Check if the form fields contain the expected values
    expect(screen.getByPlaceholderText(/Your Name/i).value).toBe('Test User');
    expect(screen.getByPlaceholderText(/Your Email/i).value).toBe('test@example.com');
    expect(screen.getByPlaceholderText(/Your Message/i).value).toBe('Hello, this is a test message.');

    await act(async () => {
        fireEvent.click(screen.getByText(/Send Message/i));
    });
    

    // Assert that the response message is displayed
    expect(screen.getByText(/Thank you for reaching out!/i)).toBeInTheDocument();
});
