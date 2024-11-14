// ServiceCard.js
import React from 'react';


function ServiceCard({ title, brief, onClick, isSelected }) {
    return (
        <div 
            className={`service-card ${isSelected ? 'selected' : ''}`} 
            onClick={onClick}
        >
            <h2>{title}</h2>
            <p>{brief}</p>
        </div>
    );
}

export default ServiceCard;
