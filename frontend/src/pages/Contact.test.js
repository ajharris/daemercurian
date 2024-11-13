import { render, screen, fireEvent } from '@testing-library/react';
import Contact from './Contact';

test('renders Contact form and handles submission', () => {
    render(<Contact />);
    fireEvent.change(screen.getByPlaceholderText(/Your Name/i), { target: { value: 'Test User' } });
    fireEvent.change(screen.getByPlaceholderText(/Your Email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByPlaceholderText(/Your Message/i), { target: { value: 'Hello!' } });
    fireEvent.click(screen.getByText(/Send Message/i));
    expect(screen.getByPlaceholderText(/Your Name/i).value).toBe('Test User');
});
