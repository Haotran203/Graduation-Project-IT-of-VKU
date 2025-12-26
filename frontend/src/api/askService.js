// frontend/src/api/askService.js

import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

export const askQuestion = async (
  userId,
  tenancy,
  prompt,
  model,
  deepResearch
) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/ask/`, {
      prompt,
      model,
      deepResearch,
      user_id: userId,
      tenancy,
      top_k: 5,
      use_keyword: true,
    });

    return response.data;
  } catch (error) {
    console.error("Ask API Error:", error);
    throw error;
  }
};

export const getHealth = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/health/`);
    return response.data;
  } catch (error) {
    console.error("Health API Error:", error);
    throw error;
  }
};
