import React from 'react';
import ServiceCard from '../components/ServiceCard'; // Make sure this path is correct for your project structure
import logo from '../assets/logo.png'

const Home = () => {
  return (
    <div className="home-container">
      <section className="hero-section">
        <h1>Welcome to Daemercurian Consulting</h1>
        <p>
          At Daemercurian Consulting, we blend innovation, experience, and a commitment to helping you meet your technical and creative needs.</p>
          <p><img src={logo} alt="Daemercurian Logo" className="inline-logo" /></p>
        
      </section>

      <section className="services-overview">
        <h2>Our Services</h2>
        <p>Explore how we can assist you with a range of tailored solutions:</p>

        <div className="service-cards">
          <ServiceCard title="Programming" description="Custom programming for all platforms." />
          <ServiceCard title="AV Management" description="Expert audio-visual setup and consulting." />
          <ServiceCard title="Communications" description="Enhance your communication strategies." />
        </div>
      </section>
    </div>
  );
};

export default Home;
