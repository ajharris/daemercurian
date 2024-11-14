import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Contact from './Contact';

test('renders Contact form and handles submission', async () => {
    render(<Contact />);

    // Type into the form fields
    await userEvent.type(screen.getByPlaceholderText(/Your Name/i), 'Test User');
    await userEvent.type(screen.getByPlaceholderText(/Your Email/i), 'test@example.com');
    await userEvent.type(screen.getByPlaceholderText(/Your Message/i), 'Hello!');

    // Check if the 'Your Name' field contains the expected value before submission
    expect(screen.getByPlaceholderText(/Your Name/i).value).toBe('Test User');
    expect(screen.getByPlaceholderText(/Your Email/i).value).toBe('test@example.com');
    expect(screen.getByPlaceholderText(/Your Message/i).value).toBe('Hello!');

    // Now click the submit button to trigger form clearing
    await userEvent.click(screen.getByText(/Send Message/i));

    // After submission, check if the fields are cleared
    expect(screen.getByPlaceholderText(/Your Name/i).value).toBe('');
    expect(screen.getByPlaceholderText(/Your Email/i).value).toBe('');
    expect(screen.getByPlaceholderText(/Your Message/i).value).toBe('');
});
