import React from 'react';
import { Link } from 'react-router-dom';

const Footer: React.FC = () => {
    return (
        <footer className="bg-gray-800 text-gray-200 py-8">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex flex-col md:flex-row justify-between items-center mb-8">
                    <div className="text-center md:text-left mb-4 md:mb-0">
                        <p>Placeholder text</p>
                    </div>
                    <div className="text-center md:text-right">
                        <p>Phone: placeholder</p>
                        <p>Email: placeholder@placeholder.com</p>
                    </div>
                </div>
                <div className="border-t border-gray-700 pt-6">
                    <ul className="flex justify-center space-x-6 list-none">
                        <li>
                            <Link to="/" className="text-gray-200 hover:text-gray-400 transition duration-300 no-underline">
                                Home
                            </Link>
                        </li>
                        <li>
                            <Link to="/chatbot" className="text-gray-200 hover:text-gray-400 transition duration-300 no-underline">
                                Chatbot
                            </Link>
                        </li>
                        <li>
                            <Link to="/contact" className="text-gray-200 hover:text-gray-400 transition duration-300 no-underline">
                                Contact
                            </Link>
                        </li>
                        <li>
                            <Link to="/about" className="text-gray-200 hover:text-gray-400 transition duration-300 no-underline">
                                About
                            </Link>
                        </li>
                    </ul>
                </div>
            </div>
        </footer>
    );
}

export default Footer;