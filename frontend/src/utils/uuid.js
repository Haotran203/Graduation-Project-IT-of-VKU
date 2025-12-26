// frontend/src/utils/uuid.js

/**
 * Generate UUID v4
 * Simple implementation without external dependencies
 */
export const generateUUID = () => {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    const r = Math.random() * 16 | 0;
    const v = c === 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
};

/**
 * Validate UUID format
 */
export const isValidUUID = (uuid) => {
  const uuidRegex = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
  return uuidRegex.test(uuid);
};

/**
 * Get or create conversation ID from localStorage
 */
export const getOrCreateConversationId = (userId) => {
  const storageKey = `conversation_id_${userId}`;
  let conversationId = localStorage.getItem(storageKey);

  if (!conversationId || !isValidUUID(conversationId)) {
    conversationId = generateUUID();
    localStorage.setItem(storageKey, conversationId);
  }

  return conversationId;
};

/**
 * Clear conversation ID from localStorage
 */
export const clearConversationId = (userId) => {
  const storageKey = `conversation_id_${userId}`;
  localStorage.removeItem(storageKey);
};

/**
 * Create new conversation ID
 */
export const createNewConversationId = (userId) => {
  const conversationId = generateUUID();
  const storageKey = `conversation_id_${userId}`;
  localStorage.setItem(storageKey, conversationId);
  return conversationId;
};
