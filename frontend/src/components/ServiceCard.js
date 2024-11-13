import React from 'react';

const ServiceCard = ({ title, description }) => {
  return (
    <div className="card h-100 shadow-sm mb-4">
      <div className="card-body">
        <h5 className="card-title">{title}</h5>
        <p className="card-text">{description}</p>
      </div>
    </div>
  );
};

export default ServiceCard;
