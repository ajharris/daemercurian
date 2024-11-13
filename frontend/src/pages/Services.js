import React from 'react';
import ServiceCard from '../components/ServiceCard';

const Services = () => {
    const services = [
        { title: 'Consulting', description: 'Expert guidance tailored to your business needs.' },
        { title: 'Development', description: 'Custom software solutions for your business.' },
        { title: 'Support', description: 'Ongoing maintenance and support to ensure your success.' }
    ];

    return (
        <div className="text-center">
            <h1 className="display-4 mb-4">Our Services</h1>
            <div className="row">
                {services.map((service, index) => (
                    <div key={index} className="col-md-4">
                        <ServiceCard title={service.title} description={service.description} />
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Services;
