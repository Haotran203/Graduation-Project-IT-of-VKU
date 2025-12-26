// frontend/src/components/Message.jsx - FIX LANGUAGE TAG

import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import "../styles.css";
import {getLanguageName} from "../utils/language.js";

/**
 * ✅ Clean language tag from content
 */
const cleanContent = (content) => {
  if (!content) return "";

  // Remove <language>XX</language> tags
  return content.replace(/<language>[a-z]{2}<\/language>\s*\n?/gi, "").trim();
};

/**
 * ✅ Extract language from content
 */
const extractLanguage = (content) => {
  if (!content) return null;

  const match = content.match(/<language>([a-z]{2})<\/language>/i);
  return match ? match[1].toLowerCase() : null;
};

export default function Message({
  role,
  content,
  model,
  mode,
  language,
}) {
  const messageClass =
    role === "user" ? "message user-message" : "message assistant-message";

  // ✅ Clean content
  const cleanedContent = cleanContent(content);

  // ✅ Extract language from content if available
  const contentLanguage = extractLanguage(content);
  const displayLanguage = contentLanguage || language;

  return (
    <div className={`${messageClass} message-animation`}>
      <div className="message-content">
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {cleanedContent}
        </ReactMarkdown>
      </div>

      {role === "assistant" && (displayLanguage || model || mode) && (
        <div className="message-meta">
          {displayLanguage && (
            <span className="badge badge-language">
              {getLanguageName(displayLanguage)}
            </span>
          )}
          {model && <span className="badge badge-model">🤖 {model}</span>}
          {mode && (
            <span className="badge badge-mode">
              {mode === "web_fallback" ? "🌐 Web Search" : "🗄️ RAG"}
            </span>
          )}
        </div>
      )}
    </div>
  );
}
