import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-light text-center text-lg-start py-3 mt-5">
      <div className="container">
        <p className="mb-1">&copy; {new Date().getFullYear()} Daemercurian Consulting. All rights reserved.</p>
        <p>Contact us at <a href="mailto:info@daemercurian.com">info@daemercurian.com</a></p>
      </div>
    </footer>
  );
};

export default Footer;
