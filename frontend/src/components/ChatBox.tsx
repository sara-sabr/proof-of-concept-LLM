interface Message {
  text: string;
  isUser: boolean;
}

interface ChatBoxProps {
  messages: Message[];
}

function ChatBox({ messages }: ChatBoxProps) {
  return (
    <div className="chat-box">
      {messages.map((message, index) => (
        <div
          key={index}
          className={`message ${message.isUser ? 'user' : 'bot'}`}
        >
          {message.text}
        </div>
      ))}
    </div>
  );
}

export default ChatBox;