// src/components/ModelSelect.jsx
import React from "react";

const models = {
  openai: "OpenAI (GPT-4o-mini)",
  perplexity: "Perplexity (Sonar)",
};

export default function ModelSelect({ model, setModel, deepResearch, setDeepResearch }) {
  return (
    <div className="model-select">
      <label>Model: </label>
      <select value={model} onChange={(e) => setModel(e.target.value)}>
        {Object.entries(models).map(([key, label]) => (
          <option key={key} value={key}>
            {label}
          </option>
        ))}
      </select>

      {/* Chỉ hiện Deep Research khi chọn Perplexity */}
      {model === "perplexity" && (
        <label className="deep-research-toggle">
          <input
            type="checkbox"
            checked={deepResearch}
            onChange={(e) => setDeepResearch(e.target.checked)}
          />
          🔍 Deep Research
        </label>
      )}
    </div>
  );
}
