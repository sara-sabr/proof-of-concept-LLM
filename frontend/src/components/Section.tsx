import React from 'react';

interface SectionProps {
    children: React.ReactNode;
}

const Section: React.FC<SectionProps> = ({ children }) => {
    return <section className="section">{children}</section>;
}

export default Section;