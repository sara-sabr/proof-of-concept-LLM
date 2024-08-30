// components/NavMenu.tsx
import React from 'react';
import { Link } from 'react-router-dom';
import Logo from "@/assets/Logo.png";

const NavBar: React.FC = () => {
    const flexBetween = "flex items-center justify-between";
    return (
        <nav className={`${flexBetween} nav-menu fixed top-0 z-30 w-full py-6`}>
            <div className={`${flexBetween} mx-auto w-5/6`}>
                <div className={`${flexBetween} w-full gap-16`}>
                    <div className="logo">
                        <Link to="/">
                            <img src={Logo} alt="Logo" />
                        </Link>
                    </div>
                    <div className={`flex justify-end w-full`}>
                        <div className={`${flexBetween} gap-8 text-md no-underline`}>
                            <Link to="/" className='text-gray-800 no-underline'>Home</Link>
                            <Link to="/chatbot" className='text-gray-800 no-underline'>Chatbot</Link>
                            <Link to="/contact" className='text-gray-800 no-underline'>Contact</Link>
                            <Link to="/about" className='text-gray-800 no-underline'>About</Link>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    );
}

export default NavBar;