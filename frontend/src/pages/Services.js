// Services.js
import React, { useState } from 'react';
import ServiceCard from '../components/ServiceCard';


const servicesData = [
    {
        title: 'Programming Solutions',
        brief: 'Custom software tailored to your business needs.',
        details: `
            We specialize in building and deploying software solutions that align with your business goals. Our expertise covers
            medical applications, web development, and integrations with platforms like Salesforce. Whether you need a new system 
            or an upgrade to an existing one, we’ll provide a solution designed to meet your specific requirements.
        `,
    },
    {
        title: 'Communication Strategy',
        brief: 'Effective communication strategies to enhance brand impact.',
        details: `
            At Daemercurian Consulting, we understand that great ideas need a strong voice. We help businesses create clear, 
            targeted communication strategies that connect with their audiences. From message development to platform selection, 
            we ensure that your brand’s voice is consistent and impactful.
        `,
    },
    {
        title: 'AV Management',
        brief: 'Professional AV setup and management for seamless operations.',
        details: `
            Our AV management services are built on decades of hands-on experience. We provide comprehensive solutions for events,
            meetings, and corporate setups, ensuring top-tier sound, visuals, and support. Leave the technical complexities to us 
            and focus on delivering your message with confidence.
        `,
    },
];

function Services() {
    const [selectedService, setSelectedService] = useState(null);

    return (
        <div className="services-container">
            <h1>Our Services</h1>
            <div className="services-cards">
                {servicesData.map((service, index) => (
                    <ServiceCard
                        key={index}
                        title={service.title}
                        brief={service.brief}
                        isSelected={index === selectedService}
                        onClick={() => setSelectedService(index === selectedService ? null : index)}
                    />
                ))}
            </div>
            {selectedService !== null && (
                <div className="service-details">
                    <h2>{servicesData[selectedService].title}</h2>
                    <p dangerouslySetInnerHTML={{ __html: servicesData[selectedService].details }} />
                </div>
            )}
        </div>
    );
}

export default Services;
