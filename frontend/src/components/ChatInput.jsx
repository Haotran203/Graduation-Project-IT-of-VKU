import React, { useState, useRef, useEffect } from "react";

export default function ChatInput({ onSubmit, loading }) {
  const [input, setInput] = useState("");
  const textareaRef = useRef(null);

  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    }
  }, [input]);

  const triggerSubmit = () => {
    if (input.trim() && !loading) {
      onSubmit(input);
      setInput("");
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      triggerSubmit();
    }
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    triggerSubmit();
  };

  return (
    <form onSubmit={handleFormSubmit} className="chat-input">
      <textarea
        ref={textareaRef}
        rows="1"
        value={input}
        placeholder="Nhập câu hỏi của bạn..."
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={loading}
      />
      <button type="submit" disabled={loading || !input.trim()}>
        {loading ? "⏳" : "Gửi"}
      </button>
    </form>
  );
}
