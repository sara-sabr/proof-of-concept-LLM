import React from 'react';
import Section from '../components/Section';

const Home: React.FC = () => {
    return (
        <div className="home bg-white py-20 px-40 sm:px-35 lg:px-35">
            <Section>
                <h1 className="text-4xl font-bold text-gray-900 mb-4">Home</h1>
                <h5 className="text-lg text-gray-600 mb-8">Placeholder heading text</h5>
                {/* Add more content here */}
            </Section>
            <Section>
                <h2 className="text-3xl font-semibold text-gray-800 mb-6">Placeholder heading text</h2>
                {/* Add component here */}
            </Section>
            <Section>
                <h2 className="text-3xl font-semibold text-gray-800 mb-6">Contact Us</h2>
                {/* Add component here */}
            </Section>
            <Section>
                <h2 className="text-3xl font-semibold text-gray-800 mb-6">About Us</h2>
                {/* Add component here */}
            </Section>
        </div>
    );
}

export default Home;
