import { render, screen, fireEvent } from '@testing-library/react';
import Contact from './Contact';

test('renders Contact form and handles input change', () => {
    render(<Contact />);
    
    // Simulate typing into the form fields
    fireEvent.change(screen.getByLabelText(/Name/i), { target: { value: 'Test User' } });
    fireEvent.change(screen.getByLabelText(/Email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/Message/i), { target: { value: 'Hello!' } });

    // Assert that the values are set correctly before submitting
    expect(screen.getByLabelText(/Name/i).value).toBe('Test User');
    expect(screen.getByLabelText(/Email/i).value).toBe('test@example.com');
    expect(screen.getByLabelText(/Message/i).value).toBe('Hello!');
    
    // Submit the form
    fireEvent.click(screen.getByText(/Send Message/i));
    
    // Assert that the form is cleared after submission
    expect(screen.getByLabelText(/Name/i).value).toBe('');
    expect(screen.getByLabelText(/Email/i).value).toBe('');
    expect(screen.getByLabelText(/Message/i).value).toBe('');
});
