import React from 'react';
import ServiceCard from '../components/ServiceCard';

const Services = () => {
  const services = [
    { title: 'Programming', description: 'Custom software and application development.' },
    { title: 'Communications', description: 'Strategy and solutions for effective communication.' },
    { title: 'AV Management', description: 'Advanced audio-visual management and consultation.' }
  ];

  return (
    <div>
      <h1>Our Services</h1>
      <div>
        {services.map((service, index) => (
          <ServiceCard key={index} title={service.title} description={service.description} />
        ))}
      </div>
    </div>
  );
};

export default Services;
