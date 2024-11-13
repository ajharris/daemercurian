import { render, screen } from '@testing-library/react';
import Footer from './Footer';

test('renders Footer content', () => {
    render(<Footer />);
    expect(screen.getByText(/Daemercurian Consulting/i)).toBeInTheDocument();
});
