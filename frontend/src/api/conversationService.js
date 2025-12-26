// frontend/src/api/conversationService.js

import axios from "axios";

const API_BASE_URL = "http://localhost:8000";


// ==========================================
// API CHO VIỆC QUẢN LÝ LỊCH SỬ TRÒ CHUYỆN
// ==========================================

/**
 * Lấy danh sách tất cả các cuộc trò chuyện.
 */
export const listConversations = async (limit = 50, offset = 0) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/conversations/list`, {
      params: { limit, offset, order_by: "updated_at" }
    });
    return response.data;
  } catch (error) {
    console.error("List Conversations Error:", error);
    throw error;
  }
};

/**
 * Lấy tất cả tin nhắn của một cuộc trò chuyện cụ thể.
 */
export const getMessages = async (conversationId, limit = 100) => {
  try {
    const response = await axios.get(
      `${API_BASE_URL}/conversations/${conversationId}/messages`,
      { params: { limit } }
    );
    return response.data;
  } catch (error) {
    console.error("Get Messages Error:", error);
    throw error;
  }
};

/**
 * Xóa một cuộc trò chuyện và tất cả tin nhắn liên quan.
 */
export const deleteConversation = async (conversationId) => {
  try {
    const response = await axios.delete(
      `${API_BASE_URL}/conversations/${conversationId}`
    );
    return response.data;
  } catch (error) {
    console.error("Delete Conversation Error:", error);
    throw error;
  }
};

/**
 * Tìm kiếm trong lịch sử các cuộc trò chuyện.
 */
export const searchConversations = async (query, limit = 20) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/conversations/search`, {
      params: { q: query, limit }
    });
    return response.data;
  } catch (error) {
    console.error("Search Conversations Error:", error);
    throw error;
  }
};