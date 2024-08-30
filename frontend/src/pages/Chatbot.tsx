import { useState } from 'react';
import ChatBox from '../components/ChatBox';
import InputBox from '../components/InputBox';
import '../css/Chatbot.css';

interface Message {
  text: string;
  isUser: boolean;
}

function Chatbot() {
  const [messages, setMessages] = useState<Message[]>([]);

  const sendMessage = async (message: string) => {
    // Add user message to chat
    setMessages(prev => [...prev, { text: message, isUser: true }]);

    const prompt = {
      "model": "aida_3",
      "prompt": message,
      "stream": false,
    }

    // Send message to API and get response
    try {
      const response = await fetch('http://localhost:11434/api/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(prompt),
      });
      const data: { response: string } = await response.json();

      // Add model's response to chat
      setMessages(prev => [...prev, { text: data.response, isUser: false }]);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="flex flex-col h-screen">
      <header className="p-4">
        <h1 className="text-center text-2xl font-bold">Chatbot</h1>
      </header>
      <div className="flex flex-col flex-grow p-4">
        <ChatBox messages={messages} />
      </div>
      <footer className="p-4 bg-white border-t">
        <InputBox onSend={sendMessage} />
      </footer>
    </div>
  );
}

export default Chatbot;
