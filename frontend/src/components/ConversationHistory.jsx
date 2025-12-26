import React, { useState, useEffect, forwardRef, useImperativeHandle } from "react";
import {
  listConversations,
  deleteConversation
  // ❌ Đã xóa searchConversations vì không cần gọi API nữa
} from "../api/conversationService";
import "../styles.css";

const ConversationHistory = forwardRef(({
  currentConversationId,
  onSelectConversation,
  onNewConversation,
  onClose
}, ref) => {
  // --- STATE ĐÃ ĐƯỢC CẬP NHẬT ---
  const [allConversations, setAllConversations] = useState([]); // ✨ State mới để giữ toàn bộ danh sách gốc
  const [conversations, setConversations] = useState([]);     // State để hiển thị danh sách (đã lọc hoặc toàn bộ)

  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState("");
  const [deleting, setDeleting] = useState(null);

  useImperativeHandle(ref, () => ({
    refresh: () => {
      loadConversations();
    }
  }));

  // Tải danh sách lần đầu
  useEffect(() => {
    loadConversations();
  }, []);

  // ✨ LOGIC LIVE SEARCH MỚI BẰNG useEffect
  // Tự động lọc lại danh sách mỗi khi người dùng gõ vào ô tìm kiếm
  useEffect(() => {
    const lowercasedQuery = searchQuery.toLowerCase().trim();

    // Nếu không có query, hiển thị lại toàn bộ danh sách gốc
    if (!lowercasedQuery) {
      setConversations(allConversations);
      return;
    }

    // Thực hiện lọc trên danh sách gốc (allConversations)
    const filtered = allConversations.filter(conv => {
      const title = (conv.title || "").toLowerCase();
      const preview = (conv.preview || "").toLowerCase();
      // Tìm kiếm trong cả tiêu đề và nội dung xem trước
      return title.includes(lowercasedQuery) || preview.includes(lowercasedQuery);
    });

    setConversations(filtered); // Cập nhật danh sách hiển thị

  }, [searchQuery, allConversations]); // Chạy lại mỗi khi query hoặc danh sách gốc thay đổi


  const loadConversations = async () => {
    try {
      setLoading(true);
      const response = await listConversations(100, 0);
      const loadedConvos = response.conversations || [];

      // ✨ Cập nhật cả hai danh sách khi tải dữ liệu
      setAllConversations(loadedConvos);
      setConversations(loadedConvos);

    } catch (error) {
      console.error("Failed to load conversations:", error);
    } finally {
      setLoading(false);
    }
  };

  // ❌ HÀM handleSearch CŨ ĐÃ BỊ XÓA BỎ HOÀN TOÀN

  const handleDelete = async (conversationId, e) => {
    e.stopPropagation();
    if (!window.confirm("Bạn có chắc muốn xóa cuộc trò chuyện này?")) return;
    try {
      setDeleting(conversationId);
      await deleteConversation(conversationId);

      // ✅ Cập nhật lại danh sách gốc sau khi xóa. useEffect sẽ tự động xử lý phần còn lại.
      setAllConversations(prev => prev.filter(conv => conv.id !== conversationId));

      if (conversationId === currentConversationId) {
        onNewConversation();
      }
    } catch (error) {
      console.error("Delete failed:", error);
      alert("Không thể xóa cuộc trò chuyện");
    } finally {
      setDeleting(null);
    }
  };

  const formatDate = (dateString) => {
    // ... hàm này không đổi ...
  };

  return (
    <div className="conversation-history">
      <div className="history-header">
        <h3>📜 Lịch sử trò chuyện</h3>
        <button className="btn-close-history" onClick={onClose} title="Đóng">✕</button>
      </div>

      {/* --- CẬP NHẬT LẠI PHẦN TÌM KIẾM --- */}
      <div className="history-search">
        <input
          type="text"
          value={searchQuery}
          // Chỉ cần onChange để kích hoạt useEffect
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder="🔍 Tìm trong lịch sử..."
        />
        {/* Nút "Tìm" không còn cần thiết, nhưng có thể giữ lại cho đẹp */}
      </div>

      <button className="btn-new-conversation" onClick={onNewConversation}>➕ Cuộc trò chuyện mới</button>
      <div className="history-list">
        {loading && <div className="history-loading">⏳ Đang tải...</div>}
        {!loading && conversations.length === 0 && <div className="history-empty"><p>📭 Không tìm thấy kết quả</p><small>Thử một từ khóa khác hoặc xóa bộ lọc.</small></div>}

        {/* Phần render không đổi, nó sẽ tự động hiển thị đúng danh sách `conversations` */}
        {!loading && conversations.map((conv) => (
          <div key={conv.id} className={`history-item ${conv.id === currentConversationId ? "active" : ""}`} onClick={() => onSelectConversation(conv.id)}>
            <div className="history-item-content">
              <div className="history-item-title">{conv.title || "Untitled"}</div>
              <div className="history-item-preview">{conv.preview || "Chưa có nội dung"}</div>
              <div className="history-item-meta">
                <span className="history-item-date">{formatDate(conv.updated_at)}</span>
                <span className="history-item-count">💬 {conv.message_count || 0}</span>
              </div>
            </div>
            <button className="btn-delete-conversation" onClick={(e) => handleDelete(conv.id, e)} disabled={deleting === conv.id} title="Xóa cuộc trò chuyện">{deleting === conv.id ? "⏳" : "🗑️"}</button>
          </div>
        ))}
      </div>
    </div>
  );
});

export default ConversationHistory;
